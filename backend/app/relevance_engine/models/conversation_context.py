"""
conversation_context.py
-----------------------

Pydantic model représentant le contexte de conversation utilisé par
le moteur de pertinence.  Ce modèle est aligné sur la classe
``ConversationContext`` définie dans ``core/context_analyzer.py``.
"""

from __future__ import annotations

from typing import List, Dict, Any
from pydantic import BaseModel, Field


class ConversationContext(BaseModel):
    channel_id: str = Field(..., description="Identifiant du canal")
    topic: str = Field("", description="Sujet estimé de la conversation")
    participants: List[str] = Field(default_factory=list, description="Liste des participants")
    messages: List[Dict[str, Any]] = Field(default_factory=list, description="Historique des messages")