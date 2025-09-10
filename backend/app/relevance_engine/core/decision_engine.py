"""
decision_engine
================

Ce module prend un ``RelevanceScore`` et décide de l’action à
entreprendre.  Dans cette version minimaliste, la décision est prise
directement dans ``RelevanceCalculator`` et ce module expose une
fonction qui pourra être étendue pour inclure davantage de logique
(par exemple, prise en compte de l’état de l’agent, du seuil
personnalisé, etc.).
"""

from __future__ import annotations

from ..models.relevance_models import RelevanceScore


def decide_action(score: RelevanceScore, threshold: float = 0.5) -> str:
    """Retourne l’action à entreprendre en fonction du score.

    Args:
        score: objet RelevanceScore.
        threshold: seuil au‑dessus duquel l’agent doit intervenir.

    Returns:
        str: ``"intervene"`` si le score est supérieur ou égal au seuil,
        ``"observe"`` sinon.  Cette fonction pourra retourner d’autres
        valeurs telles que ``"reflect"`` dans des versions ultérieures.
    """
    return "intervene" if score.score >= threshold else "observe"