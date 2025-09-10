"""
agent_state
-----------

Modèle décrivant l’état courant d’un agent.  Il peut être utilisé
par le moteur de pertinence pour évaluer la charge de travail,
la participation récente, etc.  Cette version est minimale et sert
de point d’extension.
"""

from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class AgentState(BaseModel):
    agent_id: str = Field(..., description="Identifiant unique de l’agent")
    workload: float = Field(0.0, ge=0.0, le=1.0, description="Charge de travail actuelle")
    last_participation: Optional[str] = Field(None, description="Horodatage de la dernière participation")
    trust_level: float = Field(1.0, ge=0.0, le=1.0, description="Niveau de confiance envers les autres agents")