"""World state tracking for multi-agent simulation."""

from dataclasses import dataclass, field


@dataclass
class StateVariable:
    name: str
    value: float
    unit: str
    description: str
    min_val: float = 0.0
    max_val: float = 100.0


@dataclass
class AgentAction:
    agent_name: str
    action_type: str  # escalate, de-escalate, negotiate, sanction, threaten, cooperate, invest, wait
    target: str
    description: str
    rationale: str


@dataclass
class RoundRecord:
    round_num: int
    time_label: str
    agent_actions: dict[str, AgentAction]
    state_before: dict[str, float]
    state_after: dict[str, float]
    arbiter_reasoning: str


@dataclass
class WorldState:
    variables: dict[str, StateVariable] = field(default_factory=dict)
    rounds: list[RoundRecord] = field(default_factory=list)

    def snapshot(self) -> dict[str, float]:
        """Current values as a flat dict."""
        return {k: v.value for k, v in self.variables.items()}

    def apply_deltas(self, deltas: dict[str, float]) -> None:
        """Apply arbiter-computed changes, clamping to min/max."""
        for name, delta in deltas.items():
            if name in self.variables:
                var = self.variables[name]
                var.value = max(var.min_val, min(var.max_val, var.value + delta))

    def describe(self) -> str:
        """Render current state as readable text for prompts."""
        lines = []
        for k, v in self.variables.items():
            lines.append(f"- {v.description}: {v.value:.1f} {v.unit}")
        return "\n".join(lines)

    def history_prompt(self, last_n: int = 2) -> str:
        """Render recent rounds as concise prompt text."""
        if not self.rounds:
            return "(No previous rounds)"
        recent = self.rounds[-last_n:]
        lines = []
        for r in recent:
            lines.append(f"\n**Round {r.round_num} ({r.time_label}):**")
            for name, action in r.agent_actions.items():
                lines.append(f"  - {name}: {action.action_type} → {action.description}")
            lines.append(f"  Result: {r.arbiter_reasoning}")
        return "\n".join(lines)


def initialize_default_state() -> WorldState:
    """Create default world state from wiki knowledge (April 2026 baseline)."""
    return WorldState(
        variables={
            "oil_price_brent": StateVariable(
                "oil_price_brent", 95.0, "$/barrel",
                "Brent crude oil price",
                min_val=40.0, max_val=200.0,
            ),
            "hormuz_throughput": StateVariable(
                "hormuz_throughput", 10.0, "ships/day",
                "Strait of Hormuz daily ship transit",
                min_val=0.0, max_val=130.0,
            ),
            "nato_cohesion": StateVariable(
                "nato_cohesion", 30.0, "0-100",
                "NATO alliance cohesion (Article 5 credibility)",
            ),
            "iran_nuclear_progress": StateVariable(
                "iran_nuclear_progress", 40.0, "0-100",
                "Iran's progress toward nuclear weapon capability",
            ),
            "us_credibility": StateVariable(
                "us_credibility", 35.0, "0-100",
                "US credibility as a reliable security partner",
            ),
            "gulf_stability": StateVariable(
                "gulf_stability", 25.0, "0-100",
                "Gulf states' economic and security stability",
            ),
            "china_influence": StateVariable(
                "china_influence", 60.0, "0-100",
                "China's geopolitical influence and leverage",
            ),
            "market_stress": StateVariable(
                "market_stress", 65.0, "0-100",
                "Global financial market stress level",
            ),
            "food_security": StateVariable(
                "food_security", 40.0, "0-100",
                "Global food security (100=fully secure)",
            ),
            "lebanon_tension": StateVariable(
                "lebanon_tension", 80.0, "0-100",
                "Israel-Lebanon/Hizbullah conflict intensity",
            ),
        }
    )
