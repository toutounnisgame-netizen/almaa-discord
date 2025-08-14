"""
Factory for instantiating agents with predefined personalities.

This module provides a helper function to create a list of
BaseAgent instances with distinct personas.  Additional personas can
easily be added by modifying the PERSONAS dictionary.
"""

from __future__ import annotations

from typing import List, Dict, Any

from .base_agent import BaseAgent
from .message_bus import MessageBus


# Define a mapping of agent names to their personalities
PERSONAS: Dict[str, str] = {
    "Scientist": "A methodical and curious researcher who relies on data and experiments.",
    "Engineer": "A practical problem solver who focuses on building and optimizing systems.",
    "Visionary": "A creative thinker who imagines bold futures and big‑picture solutions.",
    "Critic": "A sceptical analyst who challenges assumptions and seeks flaws in arguments.",
    "Optimist": "An encouraging and positive voice who inspires cooperation and belief in success.",
}


def create_default_agents(
    bus: MessageBus,
    model: str = "llama3.1:8b",
    ollama_base_url: str | None = None,
    chroma_host: str | None = None,
    chroma_port: int | None = None,
) -> List[BaseAgent]:
    """
    Instantiate a list of BaseAgent objects using the predefined
    PERSONAS.  Additional keyword arguments can be passed through to
    BaseAgent.
    """
    agents: List[BaseAgent] = []
    for name, persona in PERSONAS.items():
        agents.append(
            BaseAgent(
                name=name,
                persona=persona,
                bus=bus,
                model=model,
                ollama_base_url=ollama_base_url,
                chroma_host=chroma_host,
                chroma_port=chroma_port,
            )
        )
    return agents