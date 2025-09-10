"""
weight_manager
--------------

Gestionnaire des poids des facteurs de pertinence.  Il charge les
poids depuis un fichier YAML et expose une méthode pour les mettre
à jour dynamiquement.  Dans cette version de démonstration, les poids
sont codés en dur et la lecture de YAML est omise pour éviter les
dépendances supplémentaires.  Cette abstraction permettra de
facilement remplacer les valeurs par des paramètres configurables.
"""

from __future__ import annotations

from typing import Dict


class WeightManager:
    def __init__(self) -> None:
        # Poids par défaut (doivent être alignés avec les spécifications)
        self.weights: Dict[str, float] = {
            "expertise_match": 0.3,
            "conversation_gap": 0.25,
            "workload_capacity": 0.2,
            "recent_participation": 0.15,
            "relationship_trust": 0.05,
            "timing_appropriateness": 0.05,
        }

    def get_weights(self) -> Dict[str, float]:
        return self.weights.copy()

    def update_weights(self, new_weights: Dict[str, float]) -> None:
        self.weights.update(new_weights)