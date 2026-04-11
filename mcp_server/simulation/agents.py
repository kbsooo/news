"""Agent persona extraction from wiki entity pages — no LLM calls, pure parsing."""

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from wiki_parser import list_pages, load_page, extract_english_section, extract_wikilinks


@dataclass
class Faction:
    name: str
    description: str
    influence: str  # from wiki text: dominant, influential, marginal, etc.


@dataclass
class Agent:
    name: str
    slug: str
    agent_type: str  # state, leader, organization, bloc
    summary: str = ""
    factions: list[Faction] = field(default_factory=list)
    key_points: list[str] = field(default_factory=list)
    relationships: list[str] = field(default_factory=list)
    memory: list[str] = field(default_factory=list)

    def to_prompt_block(self) -> str:
        """Render agent as a prompt section for the host LLM."""
        lines = [f"### {self.name} ({self.agent_type})\n"]
        if self.summary:
            lines.append(self.summary)

        if self.factions:
            lines.append("\n**Internal factions:**")
            for f in self.factions:
                lines.append(f"- {f.name} ({f.influence}): {f.description}")

        if self.key_points:
            lines.append("\n**Key points:**")
            for p in self.key_points:
                lines.append(f"- {p}")

        if self.relationships:
            lines.append("\n**Relationships:**")
            for r in self.relationships:
                lines.append(f"- {r}")

        return "\n".join(lines)


GEOPOLITICAL_TAGS = {
    "geopolitics", "middle-east", "military", "energy", "asia",
    "united-states", "great-power", "alliance", "nato", "europe",
    "war", "oil", "defence", "security",
}

# Entity slugs that are better as state variables than as agents
NON_AGENT_ENTITIES = {"strait-of-hormuz", "monte-dei-paschi-di-siena"}


def _extract_sections(text: str) -> dict[str, str]:
    """Split markdown into heading → content sections."""
    sections: dict[str, str] = {}
    current_heading = ""
    current_lines: list[str] = []

    for line in text.split("\n"):
        if line.startswith("## "):
            if current_heading:
                sections[current_heading] = "\n".join(current_lines).strip()
            current_heading = line.lstrip("# ").strip()
            current_lines = []
        else:
            current_lines.append(line)

    if current_heading:
        sections[current_heading] = "\n".join(current_lines).strip()

    return sections


def _extract_bullet_points(text: str, max_items: int = 8) -> list[str]:
    """Extract bullet points from markdown text."""
    points = []
    for line in text.split("\n"):
        line = line.strip()
        if line.startswith("- ") or line.startswith("* "):
            clean = line.lstrip("-* ").strip()
            if clean and len(clean) > 10:
                points.append(clean)
    return points[:max_items]


def _extract_factions(sections: dict[str, str]) -> list[Faction]:
    """Try to extract factions from section content."""
    factions = []
    # Look for faction-related sections
    for heading, content in sections.items():
        heading_lower = heading.lower()
        if any(kw in heading_lower for kw in ["faction", "internal"]):
            # Parse top-level bullet points with bold labels as factions
            for match in re.finditer(r"^- \*\*([^*]+)\*\*[:\s]*([^\n]+)", content, re.MULTILINE):
                name = match.group(1).strip()
                desc = match.group(2).strip()
                # Skip if name is too long (likely not a faction name)
                if len(name) > 40:
                    continue
                # Try to detect influence level
                influence = "influential"
                desc_lower = desc.lower()
                if any(w in desc_lower for w in ["dominant", "hold influential", "in control", "most senior"]):
                    influence = "dominant"
                elif any(w in desc_lower for w in ["excluded", "marginal", "limited"]):
                    influence = "marginal"
                factions.append(Faction(name=name, description=desc[:200], influence=influence))

    return factions[:5]  # Cap at 5 factions


def _guess_agent_type(page) -> str:
    """Guess agent type from tags and title."""
    tags = set(t.lower() for t in page.tags)
    title = page.title.lower()

    if any(t in tags for t in {"leadership", "leader"}):
        return "leader"
    if any(name in title for name in ["trump", "netanyahu", "xi", "putin", "hassabis"]):
        return "leader"
    if any(t in tags for t in {"nato", "alliance"}):
        return "bloc"
    if any(t in tags for t in {"banking", "finance", "industry"}):
        return "organization"
    return "state"


def extract_single_agent(slug: str) -> Agent | None:
    """Extract an agent from a wiki page using pure parsing (no LLM)."""
    page = load_page(slug)
    if not page:
        return None

    english = extract_english_section(page.content)
    sections = _extract_sections(english)
    links = extract_wikilinks(english)

    # First paragraph as summary (up to 300 chars)
    first_para = ""
    for line in english.split("\n"):
        line = line.strip()
        if line and not line.startswith("#") and not line.startswith("---"):
            first_para = line[:300]
            break

    # Extract factions
    factions = _extract_factions(sections)

    # Collect key points from all sections
    key_points = []
    for heading, content in sections.items():
        heading_lower = heading.lower()
        if "see also" in heading_lower:
            continue
        points = _extract_bullet_points(content, max_items=3)
        for p in points:
            key_points.append(f"[{heading}] {p}")

    # Extract relationships from wikilinks
    relationships = [f"Connected to: [[{link}]]" for link in links[:8]]

    return Agent(
        name=page.title,
        slug=slug,
        agent_type=_guess_agent_type(page),
        summary=first_para,
        factions=factions,
        key_points=key_points[:12],
        relationships=relationships,
    )


def extract_agents(slugs: list[str] | None = None) -> list[Agent]:
    """Extract agents from wiki entity pages. No LLM calls.

    If slugs is None, auto-selects geopolitical entities based on tags.
    """
    if slugs:
        agents = []
        for s in slugs:
            a = extract_single_agent(s)
            if a:
                agents.append(a)
        return agents

    # Auto-select: entity pages with geopolitical tags
    agents = []
    for page in list_pages(exclude={"index", "log"}):
        if page.type != "entity":
            continue
        if page.slug in NON_AGENT_ENTITIES:
            continue
        page_tags = set(t.lower() for t in page.tags)
        if page_tags & GEOPOLITICAL_TAGS:
            a = extract_single_agent(page.slug)
            if a:
                agents.append(a)

    return agents
