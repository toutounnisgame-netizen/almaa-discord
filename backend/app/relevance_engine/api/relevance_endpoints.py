"""
relevance_endpoints
-------------------

Ce module expose les endpoints REST du moteur de pertinence.  Ils
permettent de calculer un score pour un agent, de récupérer
l’historique de ses scores et de modifier les seuils.  Les
implémentations sont simplifiées et devront être complétées.
"""

from __future__ import annotations

from typing import List, Dict, Any
from fastapi import APIRouter, HTTPException

from ..core.relevance_calculator import RelevanceCalculator
from ..models.relevance_models import RelevanceScore, RelevanceThresholds, RelevanceConfig
from ..models.conversation_context import ConversationContext


router = APIRouter()
calculator = RelevanceCalculator()

# In-memory storage for demo
_scores_history: Dict[str, List[RelevanceScore]] = {}
_thresholds = RelevanceThresholds()


@router.post("/calculate", response_model=RelevanceScore)
async def calculate_relevance(agent_id: str, context: ConversationContext, message: Dict[str, Any]) -> RelevanceScore:
    """
    Calcule le score de pertinence pour un agent donné.  Les paramètres
    ``context`` et ``message`` sont des modèles Pydantic convertis par
    FastAPI.  Les résultats sont stockés en mémoire et retournés au
    client.
    """
    score = await calculator.calculate_score(agent_id, context, message)
    _scores_history.setdefault(agent_id, []).append(score)
    return score


@router.get("/agents/{agent_id}/scores", response_model=List[RelevanceScore])
async def get_agent_scores(agent_id: str, limit: int = 100) -> List[RelevanceScore]:
    """Renvoie l’historique des scores d’un agent (limité à ``limit`` entrées)."""
    history = _scores_history.get(agent_id, [])
    return history[-limit:]


@router.put("/thresholds", response_model=RelevanceConfig)
async def update_thresholds(thresholds: RelevanceThresholds) -> RelevanceConfig:
    """Met à jour les seuils de pertinence utilisés par le moteur."""
    global _thresholds
    _thresholds = thresholds
    return RelevanceConfig(thresholds=_thresholds, factor_weights={})