"""
context_analyzer
================

Ce module offre des outils pour dériver un ``ConversationContext`` à
partir de l’historique des messages.  Pour le moment, la classe est
réduite au strict nécessaire.  Lors du développement complet, le
contexte devra inclure des informations telles que le sujet de la
conversation, les participants, le canal, la charge de travail de
l’agent et d’autres métadonnées nécessaires au calcul de pertinence.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class ConversationContext:
    """Structure minimaliste représentant le contexte d’une conversation."""

    channel_id: str
    topic: str
    participants: List[str]
    messages: List[Dict[str, Any]]

    @classmethod
    def from_history(cls, channel_id: str, history: List[Dict[str, Any]]) -> "ConversationContext":
        """
        Construit un ``ConversationContext`` à partir de l’historique.

        Args:
            channel_id: identifiant du canal de conversation.
            history: liste des messages échangés.

        Returns:
            ConversationContext: contexte simplifié contenant le sujet
            (déterminé naïvement à partir du premier message) et les
            participants uniques.
        """
        topic = history[0]["content"][:50] if history else ""
        participants = list({m["sender"] for m in history}) if history else []
        return cls(channel_id=channel_id, topic=topic, participants=participants, messages=history)