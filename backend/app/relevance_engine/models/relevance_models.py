"""
Modèles Pydantic pour la pertinence
-----------------------------------

Ces classes définissent la structure des objets manipulés par le moteur
de pertinence et exposés via l’API.  Elles pourront être enrichies
avec des validations plus poussées et des descriptions.
"""

from __future__ import annotations

import datetime as dt
from typing import Dict, Optional
from pydantic import BaseModel, Field


class RelevanceScore(BaseModel):
    agent_id: str = Field(..., description="Identifiant de l’agent")
    score: float = Field(..., ge=0.0, le=1.0, description="Score global de pertinence")
    factors: Dict[str, float] = Field(default_factory=dict, description="Score de chaque facteur")
    decision: str = Field(..., description="Décision prise (intervene/observe/reflect)")
    timestamp: dt.datetime = Field(..., description="Horodatage du calcul")


class RelevanceThresholds(BaseModel):
    intervene: float = Field(0.5, ge=0.0, le=1.0, description="Seuil pour intervenir")
    observe: float = Field(0.0, ge=0.0, le=1.0, description="Seuil pour observer")


class RelevanceConfig(BaseModel):
    thresholds: RelevanceThresholds
    factor_weights: Dict[str, float]