"""
websocket_handlers
------------------

Gestionnaires WebSocket pour diffuser les scores de pertinence en temps
rétel.  Pour l’instant, le serveur envoie périodiquement un score
aléatoire pour démontrer le fonctionnement.  Lors de
l’implémentation complète, ce module devra publier les scores
calculés en temps réel pour l’agent spécifié.
"""

from __future__ import annotations

import asyncio
import random
from typing import Any
from fastapi import WebSocket, WebSocketDisconnect


async def relevance_websocket(websocket: WebSocket, agent_id: str) -> None:
    """WebSocket streaming simulé pour les scores de pertinence."""
    await websocket.accept()
    try:
        while True:
            # Envoie un score aléatoire toutes les 5 secondes pour démonstration
            await asyncio.sleep(5)
            score = random.random()
            payload: Any = {
                "agent_id": agent_id,
                "score": score,
                "decision": "intervene" if score >= 0.5 else "observe",
                "timestamp": ""
            }
            await websocket.send_json(payload)
    except WebSocketDisconnect:
        return