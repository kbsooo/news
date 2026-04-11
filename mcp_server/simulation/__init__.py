"""Multi-agent geopolitical simulation engine."""

from simulation.engine import run_simulation
from simulation.agents import Agent, extract_agents
from simulation.state import WorldState, initialize_default_state

__all__ = [
    "run_simulation",
    "Agent",
    "extract_agents",
    "WorldState",
    "initialize_default_state",
]
