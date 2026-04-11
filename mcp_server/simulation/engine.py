"""Multi-agent simulation engine with round-based execution and arbiter pattern."""

import json
import re
from pathlib import Path

from simulation.llm_client import complete
from simulation.agents import Agent, extract_agents
from simulation.state import (
    WorldState,
    AgentAction,
    RoundRecord,
    initialize_default_state,
)
from simulation.report import generate_report

ACTION_TYPES = ["escalate", "de-escalate", "negotiate", "sanction", "threaten", "cooperate", "invest", "wait"]

AGENT_SYSTEM = """You are {name} in a geopolitical simulation.

{persona}

You must choose ONE action from: {actions}.
Respond with ONLY valid JSON (no markdown fences):
{{"action_type": "...", "target": "who/what", "description": "one sentence", "rationale": "one sentence"}}"""

AGENT_USER = """Scenario: {scenario}
Current date: {time_label} | Round: {round_num}/{total_rounds}

World state:
{state_desc}

Recent history:
{history}

Your memory of past decisions:
{memory}

Other actors: {other_agents}

What is your action this round?"""

ARBITER_SYSTEM = """You are the simulation arbiter. Given all agent actions this round,
determine how world state variables change. Consider:
- Direct effects of each action
- Interactions between actions (escalation + de-escalation partially cancel)
- Second-order effects (military escalation → higher oil prices)
- Historical momentum (variables don't swing wildly in one round)

Respond with ONLY valid JSON (no markdown fences):
{{"deltas": {{"variable_name": numeric_delta, ...}}, "reasoning": "2-3 sentences"}}

Keep deltas realistic: typically -10 to +10 per variable per round."""

ARBITER_USER = """Scenario: {scenario}
Round: {round_num} ({time_label})

Current state:
{state_desc}

Actions this round:
{actions_desc}

Compute state variable changes."""


def _parse_json_response(text: str, fallback: dict) -> dict:
    """Parse JSON from LLM response with fallback."""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    match = re.search(r"\{[\s\S]*\}", text)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass
    return fallback


def _compute_time_label(round_num: int, start_date: str) -> str:
    """Compute time label for a round. Simple month progression."""
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December",
    ]
    # Parse start_date like "May 2026"
    parts = start_date.split()
    if len(parts) == 2:
        try:
            month_idx = months.index(parts[0])
            year = int(parts[1])
        except (ValueError, IndexError):
            month_idx, year = 4, 2026  # default May 2026
    else:
        month_idx, year = 4, 2026

    total_months = month_idx + (round_num - 1)
    new_month = total_months % 12
    new_year = year + total_months // 12
    return f"{months[new_month]} {new_year}"


def get_agent_action(
    agent: Agent,
    scenario: str,
    state: WorldState,
    round_num: int,
    total_rounds: int,
    time_label: str,
    other_agents: list[Agent],
) -> AgentAction:
    """Get one agent's action for this round via LLM call."""
    system = AGENT_SYSTEM.format(
        name=agent.name,
        persona=agent.to_prompt_block(),
        actions=", ".join(ACTION_TYPES),
    )
    memory_str = "\n".join(agent.memory[-3:]) if agent.memory else "(First round)"
    other_names = [a.name for a in other_agents if a.name != agent.name]

    user = AGENT_USER.format(
        scenario=scenario,
        time_label=time_label,
        round_num=round_num,
        total_rounds=total_rounds,
        state_desc=state.describe(),
        history=state.history_prompt(last_n=2),
        memory=memory_str,
        other_agents=", ".join(other_names),
    )

    try:
        response = complete(system, user, temperature=0.7, max_tokens=512)
        data = _parse_json_response(response, {})
        return AgentAction(
            agent_name=agent.name,
            action_type=data.get("action_type", "wait"),
            target=data.get("target", "none"),
            description=data.get("description", "No clear action taken."),
            rationale=data.get("rationale", "Uncertainty about situation."),
        )
    except Exception:
        return AgentAction(
            agent_name=agent.name,
            action_type="wait",
            target="none",
            description="Agent could not decide (LLM call failed).",
            rationale="Technical error in simulation.",
        )


def run_arbiter(
    agent_actions: dict[str, AgentAction],
    state: WorldState,
    scenario: str,
    round_num: int,
    time_label: str,
) -> tuple[dict[str, float], str]:
    """Run the arbiter to compute state changes from all agent actions."""
    actions_desc = "\n".join(
        f"- {a.agent_name}: {a.action_type} targeting {a.target} — {a.description}"
        for a in agent_actions.values()
    )

    state_desc = "\n".join(
        f"- {v.description} ({k}): {v.value:.1f} {v.unit}"
        for k, v in state.variables.items()
    )

    user = ARBITER_USER.format(
        scenario=scenario,
        round_num=round_num,
        time_label=time_label,
        state_desc=state_desc,
        actions_desc=actions_desc,
    )

    try:
        response = complete(ARBITER_SYSTEM, user, temperature=0.3, max_tokens=1024)
        data = _parse_json_response(response, {"deltas": {}, "reasoning": "Could not parse arbiter response."})
        deltas = {k: float(v) for k, v in data.get("deltas", {}).items() if isinstance(v, (int, float))}
        reasoning = data.get("reasoning", "No reasoning provided.")
        return deltas, reasoning
    except Exception:
        return {}, "Arbiter call failed — no state changes this round."


def run_simulation(
    scenario: str,
    rounds: int = 8,
    agents: list[Agent] | None = None,
    state: WorldState | None = None,
    start_date: str = "May 2026",
    slugs: list[str] | None = None,
    variable_overrides: dict[str, float] | None = None,
) -> tuple[Path, WorldState, list[Agent]]:
    """Run a full multi-agent geopolitical simulation.

    Returns (report_path, final_state, agents).
    """
    # Phase 0: Setup
    if agents is None:
        agents = extract_agents(slugs=slugs, scenario_context=scenario)

    if state is None:
        state = initialize_default_state()

    if variable_overrides:
        for name, value in variable_overrides.items():
            if name in state.variables:
                state.variables[name].value = value

    rounds = max(1, min(rounds, 10))

    # Phase 1: Simulation rounds
    for round_num in range(1, rounds + 1):
        time_label = _compute_time_label(round_num, start_date)

        # Step A: Collect agent actions
        agent_actions: dict[str, AgentAction] = {}
        for agent in agents:
            action = get_agent_action(
                agent=agent,
                scenario=scenario,
                state=state,
                round_num=round_num,
                total_rounds=rounds,
                time_label=time_label,
                other_agents=agents,
            )
            agent_actions[agent.name] = action
            agent.memory.append(
                f"Round {round_num} ({time_label}): I chose to {action.action_type} "
                f"targeting {action.target} — {action.description}"
            )

        # Step B: Arbiter evaluates and updates state
        state_before = state.snapshot()
        deltas, reasoning = run_arbiter(agent_actions, state, scenario, round_num, time_label)
        state.apply_deltas(deltas)
        state_after = state.snapshot()

        # Step C: Record round
        state.rounds.append(RoundRecord(
            round_num=round_num,
            time_label=time_label,
            agent_actions=agent_actions,
            state_before=state_before,
            state_after=state_after,
            arbiter_reasoning=reasoning,
        ))

    # Phase 2: Generate report
    report_path = generate_report(scenario, agents, state)

    return report_path, state, agents
