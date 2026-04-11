"""Generate bilingual simulation report as wiki page."""

import re
from datetime import date
from pathlib import Path

from simulation.llm_client import complete
from simulation.agents import Agent
from simulation.state import WorldState


WIKI_DIR = Path(__file__).parent.parent.parent / "wiki"
SIM_DIR = WIKI_DIR / "simulations"


def _slugify(text: str) -> str:
    """Convert scenario text to a filename slug."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text.strip())
    return text[:60].rstrip("-")


def _format_state_table(state: WorldState) -> str:
    """Format initial → final state as markdown table."""
    if not state.rounds:
        return "(No rounds completed)"

    first = state.rounds[0].state_before
    last = state.rounds[-1].state_after
    lines = ["| Variable | Initial | Final | Change |", "|----------|---------|-------|--------|"]

    for key in state.variables:
        init_val = first.get(key, 0)
        final_val = last.get(key, 0)
        delta = final_val - init_val
        sign = "+" if delta >= 0 else ""
        desc = state.variables[key].description
        lines.append(f"| {desc} | {init_val:.1f} | {final_val:.1f} | {sign}{delta:.1f} |")

    return "\n".join(lines)


def _format_rounds(state: WorldState) -> str:
    """Format round-by-round summary."""
    lines = []
    for r in state.rounds:
        lines.append(f"\n### Round {r.round_num}: {r.time_label}\n")
        lines.append("**Actions:**")
        for name, action in r.agent_actions.items():
            lines.append(f"- **{name}**: {action.action_type} → {action.description}")
        lines.append(f"\n**State impact:** {r.arbiter_reasoning}")

        # Show key variable changes
        changes = []
        for key in r.state_before:
            before = r.state_before[key]
            after = r.state_after.get(key, before)
            if abs(after - before) > 0.5:
                desc = state.variables[key].description if key in state.variables else key
                sign = "+" if after > before else ""
                changes.append(f"{desc}: {sign}{after - before:.1f}")
        if changes:
            lines.append(f"Key changes: {'; '.join(changes)}")

    return "\n".join(lines)


def _generate_analysis(scenario: str, agents: list[Agent], state: WorldState) -> str:
    """One LLM call to synthesize analysis from simulation results."""
    rounds_summary = []
    for r in state.rounds:
        actions = "; ".join(f"{a.agent_name}: {a.action_type}" for a in r.agent_actions.values())
        rounds_summary.append(f"Round {r.round_num} ({r.time_label}): {actions} → {r.arbiter_reasoning}")

    first_state = state.rounds[0].state_before if state.rounds else {}
    last_state = state.rounds[-1].state_after if state.rounds else {}

    system = """You are a geopolitical analyst synthesizing simulation results.
Write 3-5 paragraphs analyzing: key trends, surprising outcomes, critical turning points,
and overall assessment. Be specific — reference agent actions and state changes.
End with a confidence assessment (low/medium/high) and key uncertainties."""

    user = f"""Scenario: {scenario}
Agents: {', '.join(a.name for a in agents)}
Rounds: {len(state.rounds)}

Round summaries:
{chr(10).join(rounds_summary)}

State changes (initial → final):
{chr(10).join(f'  {k}: {first_state.get(k, 0):.1f} → {last_state.get(k, 0):.1f}' for k in state.variables)}

Write your analysis."""

    return complete(system, user, temperature=0.5, max_tokens=2048)


def _translate_to_korean(english_text: str) -> str:
    """Translate the report body to Korean via one LLM call."""
    system = """Translate the following English text to Korean.
Preserve all markdown formatting, tables, bold/italic, and [[wikilinks]].
Use Korean display text for wikilinks where helpful (e.g., [[iran|이란]]).
Translate naturally, not literally."""

    return complete(system, english_text, temperature=0.3, max_tokens=4096)


def generate_report(
    scenario: str,
    agents: list[Agent],
    state: WorldState,
) -> Path:
    """Generate bilingual simulation report and save to wiki/simulations/."""
    SIM_DIR.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()

    slug = f"sim-{_slugify(scenario)}-{today}"
    filepath = SIM_DIR / f"{slug}.md"

    # Determine confidence from analysis
    analysis = _generate_analysis(scenario, agents, state)

    # Determine confidence level from analysis text
    confidence = "medium"
    analysis_lower = analysis.lower()
    if "high confidence" in analysis_lower:
        confidence = "high"
    elif "low confidence" in analysis_lower:
        confidence = "low"

    # Build English report
    agent_names = [a.name for a in agents]
    based_on = list(set(a.slug for a in agents))
    variable_names = list(state.variables.keys())

    frontmatter = f"""---
title: "Simulation: {scenario}"
type: simulation
date: {today}
scenario: "{scenario}"
variables: {variable_names}
confidence: {confidence}
based_on: {based_on}
rounds: {len(state.rounds)}
agents: {agent_names}
---"""

    agent_section = "\n".join(f"- **{a.name}** ({a.agent_type}): {'; '.join(a.primary_objectives[:2])}" for a in agents)
    state_table = _format_state_table(state)
    rounds_section = _format_rounds(state)

    english_body = f"""# Simulation: {scenario}

## Scenario
{scenario}

## Agents ({len(agents)})
{agent_section}

## Key Variables (Initial → Final)
{state_table}

## Round-by-Round Summary
{rounds_section}

## Analysis
{analysis}

## See Also
{chr(10).join(f'- [[{s}]]' for s in based_on)}"""

    # Translate to Korean (only the body, not frontmatter/See Also)
    korean_body = _translate_to_korean(english_body.split("## See Also")[0])

    # Assemble full file
    full_content = f"""{frontmatter}

{english_body}

---

{korean_body}"""

    filepath.write_text(full_content, encoding="utf-8")
    return filepath
