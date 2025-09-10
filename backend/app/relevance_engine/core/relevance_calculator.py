"""
relevance_calculator
====================

Ce module expose la classe ``RelevanceCalculator`` responsable du calcul
d’un score de pertinence à partir de plusieurs facteurs.  Cette
implémentation est un squelette : elle renvoie pour l’instant un
score aléatoire et des facteurs vides.  Lors du développement
complet, chaque facteur devra être calculé de manière asynchrone et
pondéré selon les valeurs définies dans ``config/factor_weights.yaml``.
"""

from __future__ import annotations

import random
import datetime as dt
from typing import Dict, Any

from ..models.relevance_models import RelevanceScore
from ..models.conversation_context import ConversationContext


class RelevanceCalculator:
    """Calculateur de pertinence minimal.

    Pour l’instant, tous les facteurs renvoient 0 et le score final est
    une valeur aléatoire.  Les méthodes privées (préfixées par ``_``)
    devraient être remplacées par des implémentations concrètes calculant
    chacune des six composantes décrites dans les spécifications.
    """

    async def calculate_score(
        self,
        agent_id: str,
        conversation_context: ConversationContext,
        current_message: Dict[str, Any],
    ) -> RelevanceScore:
        """Calcule et retourne un score de pertinence.

        Args:
            agent_id: Identifiant unique de l’agent évalué.
            conversation_context: Contexte de la conversation en cours.
            current_message: Message en cours de traitement.

        Returns:
            RelevanceScore: score global, dictionnaire de facteurs et décision.
        """
        # TODO : appeler chacune des méthodes de calcul de facteurs
        factors: Dict[str, float] = {}
        # Génère un score aléatoire entre 0 et 1 à des fins de démonstration
        score = random.random()
        # Décision en fonction du seuil 0.5 (à paramétrer dans config)
        decision = "intervene" if score >= 0.5 else "observe"
        return RelevanceScore(
            agent_id=agent_id,
            score=score,
            factors=factors,
            decision=decision,
            timestamp=dt.datetime.utcnow(),
        )