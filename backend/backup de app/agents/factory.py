from __future__ import annotations
from typing import List, Dict, Any
from .base_agent import BaseAgent
from .message_bus import MessageBus

PERSONAS: Dict[str, str] = {
    "Scientist": "A methodical researcher",
    "Engineer": "A practical problem solver",
    "Visionary": "A creative thinker",
}

def create_default_agents(bus: MessageBus, **kwargs) -> List[BaseAgent]:
    agents: List[BaseAgent] = []
    for name, persona in PERSONAS.items():
        agents.append(BaseAgent(name=name, persona=persona, bus=bus, **kwargs))
    return agents
