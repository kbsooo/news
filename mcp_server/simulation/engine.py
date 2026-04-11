"""Simulation state machine — driven by the host LLM, no internal LLM calls.

The host LLM (Claude Code, ChatGPT, Gemini, etc.) does all the reasoning.
This module only manages state, records rounds, and generates prompts.
"""

import json
from dataclasses import dataclass, field
from pathlib import Path

from simulation.agents import Agent, extract_agents
from simulation.state import (
    WorldState,
    AgentAction,
    RoundRecord,
    initialize_default_state,
)


ACTION_TYPES = ["escalate", "de-escalate", "negotiate", "sanction", "threaten", "cooperate", "invest", "wait"]


@dataclass
class Simulation:
    """A simulation session. Holds all state between MCP tool calls."""
    scenario: str
    agents: list[Agent]
    state: WorldState
    total_rounds: int
    current_round: int = 0
    start_date: str = "May 2026"
    completed: bool = False

    def time_label(self, round_num: int) -> str:
        months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December",
        ]
        parts = self.start_date.split()
        try:
            month_idx = months.index(parts[0])
            year = int(parts[1])
        except (ValueError, IndexError):
            month_idx, year = 4, 2026
        total = month_idx + (round_num - 1)
        return f"{months[total % 12]} {year + total // 12}"


# Global simulation store (one active simulation at a time)
_active_sim: Simulation | None = None


def setup_simulation(
    scenario: str,
    rounds: int = 8,
    slugs: list[str] | None = None,
    variable_overrides: dict[str, float] | None = None,
    start_date: str = "May 2026",
) -> str:
    """Initialize a simulation and return the full context for the host LLM.

    Returns a structured prompt that tells the host LLM:
    - Who the agents are (with personas from wiki)
    - What the world state is
    - How to play round 1
    """
    global _active_sim

    agents = extract_agents(slugs=slugs)
    if not agents:
        return "Error: No agents found. Provide entity page slugs or check wiki for entity pages with geopolitical tags."

    state = initialize_default_state()
    if variable_overrides:
        for name, value in variable_overrides.items():
            if name in state.variables:
                state.variables[name].value = value

    rounds = max(1, min(rounds, 10))

    _active_sim = Simulation(
        scenario=scenario,
        agents=agents,
        state=state,
        total_rounds=rounds,
        start_date=start_date,
    )

    # Build the setup prompt for the host LLM
    agent_blocks = "\n\n".join(a.to_prompt_block() for a in agents)
    agent_names = ", ".join(a.name for a in agents)

    return f"""# Simulation Initialized

## Scenario
{scenario}

## Agents ({len(agents)})
{agent_blocks}

## World State (April 2026 baseline)
{state.describe()}

## Rules
- {rounds} rounds, each representing ~1 month (starting {start_date})
- Each round: decide what EACH agent does
- Action types: {', '.join(ACTION_TYPES)}
- After deciding all actions, also determine how state variables change

## Next Step — Choose Your Mode

### Mode A: Subagent Simulation (Recommended — emergent behavior)
Call `sim_agents_decide()` to get per-agent prompts, then spawn **parallel subagents** — one per agent. Each agent decides independently without seeing others' choices. This produces genuinely emergent outcomes.

### Mode B: Single-pass (Faster, less emergent)
Decide all agents yourself and call `sim_advance` directly with JSON:
```json
{{
  "actions": {{
    "Agent Name": {{"action_type": "...", "target": "...", "description": "..."}}
  }},
  "state_deltas": {{"oil_price_brent": 5.0, "nato_cohesion": -3.0}},
  "reasoning": "..."
}}
```"""


def advance_round(decisions_json: str) -> str:
    """Process one round of decisions and advance the simulation.

    The host LLM provides all agent actions and state deltas.
    This function records them and returns the prompt for the next round.
    """
    global _active_sim
    if _active_sim is None:
        return "Error: No active simulation. Call sim_setup first."

    if _active_sim.completed:
        return "Simulation is already complete. Call sim_save to generate the report."

    # Parse decisions
    try:
        data = json.loads(decisions_json)
    except json.JSONDecodeError:
        return "Error: Invalid JSON. Please provide valid JSON with 'actions', 'state_deltas', and 'reasoning'."

    actions_data = data.get("actions", {})
    deltas = data.get("state_deltas", {})
    reasoning = data.get("reasoning", "")

    _active_sim.current_round += 1
    round_num = _active_sim.current_round
    time_label = _active_sim.time_label(round_num)

    # Record agent actions
    agent_actions: dict[str, AgentAction] = {}
    for agent in _active_sim.agents:
        action_data = actions_data.get(agent.name, {})
        action = AgentAction(
            agent_name=agent.name,
            action_type=action_data.get("action_type", "wait"),
            target=action_data.get("target", "none"),
            description=action_data.get("description", "No action specified."),
            rationale=action_data.get("rationale", ""),
        )
        agent_actions[agent.name] = action
        agent.memory.append(
            f"Round {round_num} ({time_label}): {action.action_type} → {action.description}"
        )

    # Apply state changes
    state_before = _active_sim.state.snapshot()
    float_deltas = {}
    for k, v in deltas.items():
        try:
            float_deltas[k] = float(v)
        except (ValueError, TypeError):
            pass
    _active_sim.state.apply_deltas(float_deltas)
    state_after = _active_sim.state.snapshot()

    # Record round
    _active_sim.state.rounds.append(RoundRecord(
        round_num=round_num,
        time_label=time_label,
        agent_actions=agent_actions,
        state_before=state_before,
        state_after=state_after,
        arbiter_reasoning=reasoning,
    ))

    # Check if simulation is complete
    if round_num >= _active_sim.total_rounds:
        _active_sim.completed = True
        return _build_completion_summary()

    # Build next round prompt
    return _build_next_round_prompt()


def _build_next_round_prompt() -> str:
    """Build the prompt for the host LLM to decide the next round."""
    sim = _active_sim
    next_round = sim.current_round + 1
    time_label = sim.time_label(next_round)

    # Agent memories
    memory_blocks = []
    for agent in sim.agents:
        recent = agent.memory[-3:] if agent.memory else ["(no history)"]
        memory_blocks.append(f"**{agent.name}:** {'; '.join(recent)}")

    return f"""# Round {next_round}/{sim.total_rounds} — {time_label}

## Current World State
{sim.state.describe()}

## Recent History
{sim.state.history_prompt(last_n=2)}

## Agent Memories
{chr(10).join(memory_blocks)}

## Your Task
Decide what each agent does this round, considering their persona, the current state, and recent history. Then determine state variable changes.

Provide JSON with `actions`, `state_deltas`, and `reasoning` — then call `sim_advance`."""


def _build_completion_summary() -> str:
    """Build summary when all rounds are complete."""
    sim = _active_sim
    first = sim.state.rounds[0].state_before
    last = sim.state.rounds[-1].state_after

    state_changes = []
    for key in sim.state.variables:
        init_val = first.get(key, 0)
        final_val = last.get(key, 0)
        delta = final_val - init_val
        sign = "+" if delta >= 0 else ""
        desc = sim.state.variables[key].description
        state_changes.append(f"- {desc}: {init_val:.1f} → {final_val:.1f} ({sign}{delta:.1f})")

    round_summaries = []
    for r in sim.state.rounds:
        actions = "; ".join(f"{a.agent_name}: {a.action_type}" for a in r.agent_actions.values())
        round_summaries.append(f"**Round {r.round_num} ({r.time_label}):** {actions}")

    return f"""# Simulation Complete — {sim.total_rounds} Rounds

## Scenario
{sim.scenario}

## State Changes (Initial → Final)
{chr(10).join(state_changes)}

## Round Summary
{chr(10).join(round_summaries)}

## Next Step
Call `sim_save` with your analysis (BOTH English and Korean) to generate the bilingual wiki report.

Provide a JSON with:
```json
{{
  "analysis": "3-5 paragraphs English analysis: trends, surprises, turning points, confidence",
  "analysis_ko": "3-5문단 한국어 분석: 추세, 의외의 결과, 전환점, 신뢰도",
  "confidence": "low|medium|high"
}}
```"""


def get_agent_prompts() -> str:
    """Generate independent prompts for each agent — designed for parallel subagent spawning.

    Returns a JSON array of per-agent prompt objects. The host LLM should
    spawn one subagent per agent, each receiving ONLY its own prompt.
    Agents cannot see each other's prompts or decisions.

    This is what enables emergent behavior: genuine independence.
    """
    if _active_sim is None:
        return json.dumps({"error": "No active simulation. Call sim_setup first."})

    if _active_sim.completed:
        return json.dumps({"error": "Simulation complete. Call sim_save."})

    sim = _active_sim
    next_round = sim.current_round + 1
    time_label = sim.time_label(next_round)

    prompts = []
    for agent in sim.agents:
        # Each agent gets: its own wiki identity, world state, history, its own memory
        # It does NOT get other agents' personas or memories
        other_names = [a.name for a in sim.agents if a.name != agent.name]
        memory_str = "\n".join(f"- {m}" for m in agent.memory[-3:]) if agent.memory else "(This is your first round)"

        prompt = f"""You are **{agent.name}** in a geopolitical simulation.

## Your Identity
{agent.to_prompt_block()}

## Scenario
{sim.scenario}

## Current Date: {time_label} (Round {next_round}/{sim.total_rounds})

## World State
{sim.state.describe()}

## Recent Events
{sim.state.history_prompt(last_n=2)}

## Your Past Decisions
{memory_str}

## Other Actors in This Simulation
{', '.join(other_names)}
(You do NOT know what they are deciding this round.)

## Your Task
Choose ONE action. Action types: {', '.join(ACTION_TYPES)}

Think from YOUR perspective only. Consider your objectives, constraints, relationships, and what you know about the current situation. You do NOT know what other actors will decide.

Respond with ONLY this JSON:
```json
{{
  "agent_name": "{agent.name}",
  "action_type": "one of the action types above",
  "target": "who or what you're acting on",
  "description": "one sentence describing your action",
  "rationale": "one sentence explaining why"
}}
```"""
        prompts.append({
            "agent_name": agent.name,
            "agent_slug": agent.slug,
            "prompt": prompt,
        })

    return json.dumps({
        "round": next_round,
        "total_rounds": sim.total_rounds,
        "time_label": time_label,
        "num_agents": len(prompts),
        "agent_prompts": prompts,
        "instructions": (
            "Spawn one subagent per agent IN PARALLEL. "
            "Each subagent receives ONLY its own prompt — they cannot see each other. "
            "Collect all responses, then call sim_advance with the combined actions + your arbiter state_deltas."
        ),
    }, ensure_ascii=False)


def save_report(analysis_json: str) -> str:
    """Save the simulation report to wiki/simulations/."""
    global _active_sim
    if _active_sim is None:
        return "Error: No active simulation."

    try:
        data = json.loads(analysis_json)
    except json.JSONDecodeError:
        return (
            "Error: Invalid JSON. Provide:\n"
            '{"analysis": "English analysis...", "analysis_ko": "한국어 분석...", "confidence": "low|medium|high"}'
        )

    analysis = data.get("analysis", "No analysis provided.")
    analysis_ko = data.get("analysis_ko", "")
    confidence = data.get("confidence", "medium")

    from simulation.report import generate_report
    path = generate_report(
        scenario=_active_sim.scenario,
        agents=_active_sim.agents,
        state=_active_sim.state,
        analysis=analysis,
        analysis_ko=analysis_ko,
        confidence=confidence,
    )

    # Reset
    _active_sim = None

    return f"Report saved: `{path.relative_to(path.parent.parent.parent)}`\nOpen in Obsidian or read with `wiki_read`."


def get_status() -> str:
    """Return status of active simulation and list of completed ones."""
    lines = []

    if _active_sim:
        lines.append(f"**Active simulation:** {_active_sim.scenario}")
        lines.append(f"  Round {_active_sim.current_round}/{_active_sim.total_rounds}")
        lines.append(f"  Agents: {', '.join(a.name for a in _active_sim.agents)}")
        lines.append("")

    # List completed simulations
    sim_dir = Path(__file__).parent.parent.parent / "wiki" / "simulations"
    if sim_dir.exists():
        files = sorted(sim_dir.glob("*.md"))
        if files:
            lines.append(f"**Completed simulations ({len(files)}):**")
            for f in files:
                text = f.read_text(encoding="utf-8")
                scenario = "Unknown"
                for line in text.split("\n")[:15]:
                    if line.startswith("scenario:"):
                        scenario = line.split(":", 1)[1].strip().strip('"')
                        break
                lines.append(f"  - `{f.stem}`: {scenario}")

    if not lines:
        lines.append("No active or completed simulations.")

    return "\n".join(lines)
