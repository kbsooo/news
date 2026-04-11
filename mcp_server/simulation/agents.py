"""Agent persona extraction from wiki entity pages."""

import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from wiki_parser import list_pages, load_page, extract_english_section

from simulation.llm_client import complete


@dataclass
class Faction:
    name: str
    objectives: list[str]
    influence: str  # dominant, influential, marginal


@dataclass
class Agent:
    name: str
    slug: str
    agent_type: str  # state, leader, organization, bloc
    factions: list[Faction] = field(default_factory=list)
    primary_objectives: list[str] = field(default_factory=list)
    constraints: list[str] = field(default_factory=list)
    behavioral_tendencies: list[str] = field(default_factory=list)
    relationships: dict[str, str] = field(default_factory=dict)
    recent_actions: list[str] = field(default_factory=list)
    memory: list[str] = field(default_factory=list)

    def to_prompt_block(self) -> str:
        """Render agent as a concise prompt section for simulation rounds."""
        lines = [f"**{self.name}** ({self.agent_type})"]

        if self.factions:
            factions_str = "; ".join(
                f"{f.name} ({f.influence}): {', '.join(f.objectives[:2])}"
                for f in self.factions
            )
            lines.append(f"Internal factions: {factions_str}")

        if self.primary_objectives:
            lines.append(f"Objectives: {'; '.join(self.primary_objectives[:4])}")

        if self.constraints:
            lines.append(f"Constraints: {'; '.join(self.constraints[:3])}")

        if self.behavioral_tendencies:
            lines.append(f"Tendencies: {'; '.join(self.behavioral_tendencies[:3])}")

        if self.relationships:
            rels = "; ".join(f"{k}: {v}" for k, v in list(self.relationships.items())[:5])
            lines.append(f"Relationships: {rels}")

        if self.recent_actions:
            lines.append(f"Recent actions: {'; '.join(self.recent_actions[:3])}")

        return "\n".join(lines)


GEOPOLITICAL_TAGS = {
    "geopolitics", "middle-east", "military", "energy", "asia",
    "united-states", "great-power", "alliance", "nato", "europe",
    "war", "chokepoint", "oil", "defence", "security",
}

EXTRACTION_SYSTEM = """You extract structured agent personas from wiki pages for a geopolitical simulation.
Return ONLY valid JSON matching the schema below. Be concise — each field 1-2 sentences max.
Do NOT include markdown code fences or any text outside the JSON object."""

EXTRACTION_USER = """Extract an agent persona from this wiki page for the following simulation scenario:
{scenario}

Wiki page content:
{content}

Return JSON:
{{
  "name": "agent display name",
  "agent_type": "state|leader|organization|bloc",
  "factions": [{{"name": "...", "objectives": ["..."], "influence": "dominant|influential|marginal"}}],
  "primary_objectives": ["objective 1", "objective 2", "objective 3"],
  "constraints": ["constraint 1", "constraint 2"],
  "behavioral_tendencies": ["tendency 1", "tendency 2"],
  "relationships": {{"other_agent": "relationship description"}},
  "recent_actions": ["action 1", "action 2"]
}}"""


def _parse_agent_json(text: str, slug: str) -> dict:
    """Parse LLM response as JSON, with fallback regex extraction."""
    # Try direct parse
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    # Try extracting JSON block from response
    match = re.search(r"\{[\s\S]*\}", text)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass
    # Fallback: minimal agent
    return {
        "name": slug.replace("-", " ").title(),
        "agent_type": "state",
        "factions": [],
        "primary_objectives": ["Protect national interests"],
        "constraints": ["Limited information"],
        "behavioral_tendencies": ["Cautious"],
        "relationships": {},
        "recent_actions": [],
    }


def extract_single_agent(slug: str, scenario_context: str = "") -> Agent:
    """Extract a structured agent persona from a wiki page via one LLM call."""
    page = load_page(slug)
    if not page:
        raise ValueError(f"Wiki page not found: {slug}")

    english = extract_english_section(page.content)
    # Truncate to ~3000 chars to control token cost
    if len(english) > 3000:
        english = english[:3000] + "\n...(truncated)"

    scenario = scenario_context or "general geopolitical scenario"
    user_prompt = EXTRACTION_USER.format(scenario=scenario, content=english)

    response = complete(EXTRACTION_SYSTEM, user_prompt, temperature=0.3, max_tokens=1024)
    data = _parse_agent_json(response, slug)

    factions = [
        Faction(
            name=f.get("name", "Unknown"),
            objectives=f.get("objectives", []),
            influence=f.get("influence", "influential"),
        )
        for f in data.get("factions", [])
    ]

    return Agent(
        name=data.get("name", slug.replace("-", " ").title()),
        slug=slug,
        agent_type=data.get("agent_type", "state"),
        factions=factions,
        primary_objectives=data.get("primary_objectives", []),
        constraints=data.get("constraints", []),
        behavioral_tendencies=data.get("behavioral_tendencies", []),
        relationships=data.get("relationships", {}),
        recent_actions=data.get("recent_actions", []),
    )


def extract_agents(
    slugs: list[str] | None = None,
    scenario_context: str = "",
) -> list[Agent]:
    """Extract agents from wiki entity pages.

    If slugs is None, auto-selects geopolitical entities based on tags.
    """
    if slugs:
        return [extract_single_agent(s, scenario_context) for s in slugs]

    # Auto-select: entity pages with geopolitical tags
    agents = []
    for page in list_pages(exclude={"index", "log"}):
        if page.type != "entity":
            continue
        page_tags = set(t.lower() for t in page.tags)
        if page_tags & GEOPOLITICAL_TAGS:
            agents.append(extract_single_agent(page.slug, scenario_context))

    return agents
