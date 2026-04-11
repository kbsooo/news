"""Multi-agent geopolitical simulation engine — stateful, no LLM calls."""

from simulation.engine import setup_simulation, advance_round, save_report, get_status
from simulation.agents import Agent, extract_agents
from simulation.state import WorldState, initialize_default_state

__all__ = [
    "setup_simulation",
    "advance_round",
    "save_report",
    "get_status",
    "Agent",
    "extract_agents",
    "WorldState",
    "initialize_default_state",
]
