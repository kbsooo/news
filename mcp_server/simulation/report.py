"""Generate simulation report as wiki page — no LLM calls."""

import re
from datetime import date
from pathlib import Path

from simulation.agents import Agent
from simulation.state import WorldState


WIKI_DIR = Path(__file__).parent.parent.parent / "wiki"
SIM_DIR = WIKI_DIR / "simulations"


def _slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text.strip())
    return text[:60].rstrip("-")


def generate_report(
    scenario: str,
    agents: list[Agent],
    state: WorldState,
    analysis: str = "",
    confidence: str = "medium",
) -> Path:
    """Generate simulation report and save to wiki/simulations/.

    The analysis text is provided by the host LLM — this function just
    assembles the markdown. No LLM calls.
    """
    SIM_DIR.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()

    slug = f"sim-{_slugify(scenario)}-{today}"
    filepath = SIM_DIR / f"{slug}.md"

    agent_names = [a.name for a in agents]
    based_on = list(set(a.slug for a in agents))

    # Frontmatter
    frontmatter = f"""---
title: "Simulation: {scenario}"
type: simulation
date: {today}
scenario: "{scenario}"
confidence: {confidence}
based_on: {based_on}
rounds: {len(state.rounds)}
agents: {agent_names}
---"""

    # Agents section
    agent_section = "\n".join(
        f"- **{a.name}** ({a.agent_type})"
        for a in agents
    )

    # State table
    if state.rounds:
        first = state.rounds[0].state_before
        last = state.rounds[-1].state_after
        table_lines = ["| Variable | Initial | Final | Change |", "|----------|---------|-------|--------|"]
        for key, var in state.variables.items():
            i = first.get(key, 0)
            f_val = last.get(key, 0)
            d = f_val - i
            sign = "+" if d >= 0 else ""
            table_lines.append(f"| {var.description} | {i:.1f} | {f_val:.1f} | {sign}{d:.1f} |")
        state_table = "\n".join(table_lines)
    else:
        state_table = "(No rounds completed)"

    # Rounds section
    rounds_lines = []
    for r in state.rounds:
        rounds_lines.append(f"\n### Round {r.round_num}: {r.time_label}\n")
        rounds_lines.append("**Actions:**")
        for name, action in r.agent_actions.items():
            rounds_lines.append(f"- **{name}**: {action.action_type} → {action.description}")
        if r.arbiter_reasoning:
            rounds_lines.append(f"\n**Impact:** {r.arbiter_reasoning}")

        changes = []
        for key in r.state_before:
            before = r.state_before[key]
            after = r.state_after.get(key, before)
            if abs(after - before) > 0.5:
                desc = state.variables[key].description if key in state.variables else key
                sign = "+" if after > before else ""
                changes.append(f"{desc}: {sign}{after - before:.1f}")
        if changes:
            rounds_lines.append(f"Key changes: {'; '.join(changes)}")

    rounds_section = "\n".join(rounds_lines)

    # Full report
    content = f"""{frontmatter}

# Simulation: {scenario}

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

## Confidence: {confidence}

## See Also
{chr(10).join(f'- [[{s}]]' for s in based_on)}"""

    filepath.write_text(content, encoding="utf-8")
    return filepath
