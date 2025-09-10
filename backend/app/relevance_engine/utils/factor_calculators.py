"""
factor_calculators
------------------

Ce module regroupe des fonctions asynchrones destinées à calculer
individuellement chaque facteur de pertinence.  Dans cette version de
démo, chaque fonction renvoie zéro après une petite pause pour simuler
un calcul.  Lors de l’implémentation complète, les fonctions devront
analyser le contexte, l’état de l’agent et le message pour retourner
des valeurs entre 0 et 1.
"""

from __future__ import annotations

import asyncio
from typing import Any


async def expertise_match(agent_id: str, topic: str) -> float:
    await asyncio.sleep(0)  # placeholder
    return 0.0


async def conversation_gap(context: Any, agent_id: str) -> float:
    await asyncio.sleep(0)
    return 0.0


async def workload_capacity(agent_id: str) -> float:
    await asyncio.sleep(0)
    return 0.0


async def recent_participation(agent_id: str, channel_id: str) -> float:
    await asyncio.sleep(0)
    return 0.0


async def relationship_trust(agent_id: str, participants: list) -> float:
    await asyncio.sleep(0)
    return 0.0


async def timing_appropriateness(context: Any, current_message: Any) -> float:
    await asyncio.sleep(0)
    return 0.0