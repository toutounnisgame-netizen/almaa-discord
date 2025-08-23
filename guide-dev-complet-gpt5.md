# 📖 GUIDE DÉVELOPPEMENT COMPLET ALMAA WORKSPACE - POUR GPT-5

## 🎯 CONTEXTE ET OBJECTIFS

### Situation Actuelle
Tu développes avec moi la **Phase 4** du projet ALMAA Workspace, une évolution majeure d'un prototype Discord IA existant vers un assistant AGI personnel complet.

**Objectif Principal** : Créer un système multi-agents spécialisés avec :
- Système de pertinence contextuelle (agents parlent quand c'est pertinent)
- Interface admin complète avec contrôle des agents
- Outils modulaires pour productivité
- Gouvernance IA avec modération autonome
- Architecture scalable pour 100+ agents

### Utilisateur Final
- **Profil** : Chef de projet en arrêt maladie, budget 200k€, serveur 9600 TOPS prévu
- **Objectif** : Assistant AGI personnel pour tous projets (développement, écriture, créativité, analyse)
- **Contraintes** : 100% offline, sécurité maximale, temps illimité de développement
- **Use Case #1** : Agents l'aident à développer le projet ALMAA lui-même

---

## 📋 INSTRUCTIONS SPÉCIFIQUES DÉVELOPPEMENT

### ⚠️ RÈGLES CRITIQUES À RESPECTER

1. **Base Existante** : Tu pars du code existant GitHub (architecture déjà en place)
2. **Approche Incrémentale** : Améliore le code existant, pas de reconstruction complète
3. **Analyse Avant Action** : Toujours analyser le code existant avant de proposer modifications
4. **Documentation Complète** : Documente chaque modification avec commentaires détaillés
5. **Tests Inclus** : Inclus tests pour chaque nouvelle fonctionnalité
6. **Configuration Flexible** : Rends tout configurable via fichiers YAML/JSON
7. **Performance** : Optimise pour temps réel et charge élevée
8. **Sécurité** : Valide toutes les entrées, sandboxe les exécutions

### 🛠️ STACK TECHNIQUE EXISTANTE
```yaml
Backend:
  api: "FastAPI + Uvicorn"
  database: "PostgreSQL 16 + pgvector"
  cache: "Redis 7 Alpine"
  vector_db: "ChromaDB"
  storage: "MinIO S3-compatible"
  ai: "Ollama + modèles locaux"
  
Frontend:
  framework: "Next.js (Static Site Generation)"
  ui: "React + TypeScript"
  styling: "Tailwind CSS"
  state: "React hooks + Context"
  
Infrastructure:
  proxy: "Nginx Alpine"
  containers: "Docker Compose"
  monitoring: "Prometheus + Grafana"
  logging: "Loki + Grafana"
```

---

## 🎯 ROADMAP DÉVELOPPEMENT PRIORITAIRE

### PHASE 1 : FOUNDATION (Semaines 1-4) - PRIORITÉ CRITIQUE

#### Semaine 1-2 : Système de Pertinence Contextuelle
**Objectif** : Agents parlent seulement quand c'est pertinent (score > 0.5)

**Développements requis :**

1. **Service Relevance Engine**
```python
# À créer : relevance-engine/
├── src/
│   ├── relevance_calculator.py    # Calcul scores pertinence
│   ├── context_analyzer.py        # Analyse contexte conversation
│   ├── decision_engine.py         # Décision intervention agent
│   └── learning_system.py         # Apprentissage patterns
├── models/
│   └── relevance_factors.py       # Facteurs pertinence
├── api/
│   └── relevance_api.py           # API REST endpoints
└── config/
    └── relevance_config.yaml      # Configuration facteurs
```

**Facteurs de pertinence à implémenter :**
- `expertise_match` : Correspondance expertise agent / sujet conversation
- `conversation_gap` : Détection manque d'information dans conversation
- `workload_capacity` : Charge de travail actuelle agent
- `recent_participation` : Éviter participation répétée
- `relationship_trust` : Niveau confiance avec autres agents
- `timing_appropriateness` : Moment approprié pour intervenir

2. **Intégration WebSocket pour Temps Réel**
```python
# Extension WebSocket existant
websocket_manager.py:
  - add_relevance_checking()
  - integrate_decision_engine()
  - real_time_score_updates()
```

3. **Extension API FastAPI**
```python
# Nouveaux endpoints à ajouter
/api/v1/relevance/
├── POST /calculate          # Calcul score pertinence
├── GET  /scores/{agent_id}  # Scores agent
├── PUT  /thresholds         # Mise à jour seuils
└── GET  /analytics          # Analytics pertinence
```

#### Semaine 3-4 : Interface Admin Basique
**Objectif** : Dashboard avec contrôles agents essentiels

**Développements requis :**

1. **Dashboard Admin (Next.js)**
```typescript
// Composants à créer
components/admin/
├── AgentControlPanel.tsx      # Panneau contrôle principal
├── AgentCard.tsx              # Carte agent individuel
├── PauseResumeButton.tsx      # Contrôles pause/reprendre
├── TaskInjector.tsx           # Interface injection tâches
├── DebugMonitor.tsx           # Monitoring debug temps réel
├── NotificationCenter.tsx     # Centre notifications
└── SystemMetrics.tsx          # Métriques système

pages/admin/
├── dashboard.tsx              # Dashboard principal
├── agents.tsx                 # Gestion agents
└── debug.tsx                  # Interface debug
```

2. **API Extensions**
```python
# Nouveaux endpoints admin
/api/v1/admin/
├── POST /agents/{id}/pause    # Pause agent
├── POST /agents/{id}/resume   # Reprendre agent
├── POST /tasks/inject         # Injection tâche prioritaire
├── GET  /debug/{agent_id}     # Debug infos agent
└── GET  /notifications        # Notifications admin
```

### PHASE 2 : AGENT MANAGEMENT (Semaines 5-8)

#### Templates d'Agents Pré-configurés
**Objectif** : Templates spécialisés (Developer, Analyst, Moderator, etc.)

**Templates essentiels :**
```yaml
Developer Backend:
  model: "codellama:7b"
  context_size: 8192
  personality: "Rigoureux, méthodique, orienté solution"
  tools: ["git", "code-analysis", "testing", "docker"]
  system_prompt: "Tu es un expert développeur backend Python/FastAPI..."
  
Analyst Data:
  model: "llama3.1:8b"
  context_size: 16384
  personality: "Analytique, précis, synthétique"
  tools: ["data-processing", "visualization", "research"]
  system_prompt: "Tu es un expert en analyse de données..."
  
Moderator Quality:
  model: "mistral:7b"
  context_size: 8192
  personality: "Équilibré, juste, diplomatique"
  tools: ["moderation", "quality-check", "conflict-resolution"]
  system_prompt: "Tu es un superviseur qualité et médiateur..."
```

#### Communication Inter-Agents
**Objectif** : Messages privés entre agents + canaux deepthink

**Développements requis :**
1. **Messages Privés** : Système MP avec acceptation/refus
2. **Canaux Deepthink** : Canaux privés réflexion individuelle
3. **Archivage Automatique** : Archivage conversations après 48h inactivité

---

## 💻 STANDARDS DÉVELOPPEMENT

### Structure Code
```python
# Standard structure pour nouveaux services
service-name/
├── src/
│   ├── __init__.py
│   ├── main.py                    # Point d'entrée service
│   ├── core/                      # Logique métier core
│   ├── api/                       # Endpoints API REST
│   ├── models/                    # Modèles données
│   ├── services/                  # Services métier
│   ├── utils/                     # Utilitaires
│   └── exceptions/                # Exceptions personnalisées
├── tests/
│   ├── unit/                      # Tests unitaires
│   ├── integration/               # Tests intégration
│   └── fixtures/                  # Fixtures tests
├── config/
│   ├── settings.yaml              # Configuration service
│   └── logging.yaml               # Configuration logs
├── docker/
│   ├── Dockerfile                 # Image Docker
│   └── docker-compose.test.yml    # Tests Docker
├── requirements/
│   ├── base.txt                   # Dépendances base
│   └── dev.txt                    # Dépendances développement
└── README.md                      # Documentation service
```

### Standards Codage
```python
# Exemple standard fonction
async def calculate_relevance_score(
    agent_id: str,
    conversation_context: ConversationContext,
    current_message: Message
) -> RelevanceScore:
    """
    Calcule le score de pertinence pour qu'un agent intervienne.
    
    Args:
        agent_id: ID unique de l'agent
        conversation_context: Contexte conversation actuelle
        current_message: Message déclencheur
        
    Returns:
        RelevanceScore: Score et détails facteurs
        
    Raises:
        AgentNotFoundError: Si agent n'existe pas
        ContextInvalidError: Si contexte invalide
    """
    try:
        # Validation inputs
        await validate_agent_exists(agent_id)
        validate_conversation_context(conversation_context)
        
        # Récupération état agent
        agent_state = await get_agent_state(agent_id)
        
        # Calcul facteurs pertinence
        factors = await calculate_factors(
            agent_state=agent_state,
            context=conversation_context,
            message=current_message
        )
        
        # Score final pondéré
        final_score = weighted_sum(factors, agent_state.personality.weights)
        
        # Log pour debug
        logger.debug(
            f"Relevance calculated for agent {agent_id}: {final_score}",
            extra={"agent_id": agent_id, "score": final_score, "factors": factors}
        )
        
        return RelevanceScore(
            agent_id=agent_id,
            score=final_score,
            factors=factors,
            timestamp=datetime.utcnow()
        )
        
    except Exception as e:
        logger.error(f"Error calculating relevance: {e}", exc_info=True)
        raise RelevanceCalculationError(f"Failed to calculate relevance: {e}")
```

### Standards Tests
```python
# Exemple test complet
import pytest
from unittest.mock import AsyncMock, patch
from fastapi.testclient import TestClient

class TestRelevanceCalculator:
    
    @pytest.fixture
    async def sample_agent(self):
        return Agent(
            id="agent-123",
            name="Test Developer",
            type="developer",
            status="active",
            expertise=["python", "fastapi"]
        )
    
    @pytest.fixture
    def sample_conversation(self):
        return ConversationContext(
            channel_id="channel-456",
            recent_messages=[
                Message(content="How to optimize FastAPI performance?"),
                Message(content="We need better database queries")
            ],
            participants=["agent-789", "user-admin"],
            topic="performance optimization"
        )
    
    async def test_calculate_relevance_score_high_match(
        self, sample_agent, sample_conversation
    ):
        """Test score élevé quand expertise correspond parfaitement."""
        
        with patch('relevance_calculator.get_agent_state') as mock_get_state:
            mock_get_state.return_value = sample_agent
            
            result = await calculate_relevance_score(
                agent_id=sample_agent.id,
                conversation_context=sample_conversation,
                current_message=Message(content="FastAPI optimization tips?")
            )
            
            assert result.score > 0.8
            assert "expertise_match" in result.factors
            assert result.factors["expertise_match"] > 0.9
    
    async def test_calculate_relevance_score_low_match(
        self, sample_agent, sample_conversation
    ):
        """Test score faible quand pas d'expertise correspondante."""
        
        off_topic_conversation = ConversationContext(
            channel_id="channel-789",
            recent_messages=[Message(content="Best cooking recipes?")],
            topic="cooking"
        )
        
        with patch('relevance_calculator.get_agent_state') as mock_get_state:
            mock_get_state.return_value = sample_agent
            
            result = await calculate_relevance_score(
                agent_id=sample_agent.id,
                conversation_context=off_topic_conversation,
                current_message=Message(content="Recipe for pasta?")
            )
            
            assert result.score < 0.3
            assert result.factors["expertise_match"] < 0.2
    
    async def test_calculate_relevance_agent_not_found(self):
        """Test erreur quand agent n'existe pas."""
        
        with pytest.raises(AgentNotFoundError):
            await calculate_relevance_score(
                agent_id="non-existent",
                conversation_context=ConversationContext(),
                current_message=Message(content="test")
            )
```

### Standards Configuration
```yaml
# Exemple configuration service
# config/relevance_config.yaml
relevance_engine:
  thresholds:
    intervention: 0.5      # Score minimum pour intervention
    high_priority: 0.8     # Score pour intervention prioritaire
    low_priority: 0.2      # Score pour écoute passive uniquement
    
  factors:
    expertise_match:
      weight: 0.3
      enabled: true
      min_threshold: 0.1
      
    conversation_gap:
      weight: 0.25
      enabled: true
      detection_method: "semantic_similarity"
      
    workload_capacity:
      weight: 0.2
      enabled: true
      max_concurrent_tasks: 3
      
    recent_participation:
      weight: 0.15
      enabled: true
      cooldown_minutes: 30
      
    timing_appropriateness:
      weight: 0.1
      enabled: true
      avoid_interruption: true
      
  performance:
    cache_ttl: 300        # TTL cache scores (5 minutes)
    calculation_timeout: 5 # Timeout calcul (5 secondes)
    batch_size: 10        # Taille lot pour traitement
    
  logging:
    level: "INFO"
    include_factors: true
    include_scores: true
```

---

## 🗃️ BASES DE DONNÉES ET MODÈLES

### Modèles PostgreSQL Existants à Étendre
```sql
-- Extensions nécessaires pour nouveaux modèles
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgvector";

-- Nouveau schéma pour pertinence
CREATE SCHEMA IF NOT EXISTS relevance;

-- Table scores de pertinence
CREATE TABLE relevance.scores (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    agent_id UUID NOT NULL REFERENCES agents(id),
    conversation_context JSONB NOT NULL,
    score REAL NOT NULL CHECK (score >= 0 AND score <= 1),
    factors JSONB NOT NULL,
    intervention_decision BOOLEAN NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    -- Index pour performance
    INDEX idx_relevance_agent_created (agent_id, created_at DESC),
    INDEX idx_relevance_score_created (score DESC, created_at DESC)
);

-- Table historique décisions
CREATE TABLE relevance.decisions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    agent_id UUID NOT NULL REFERENCES agents(id),
    channel_id UUID NOT NULL REFERENCES channels(id),
    message_id UUID REFERENCES messages(id),
    decision_type VARCHAR(50) NOT NULL, -- 'intervene', 'observe', 'reflect'
    relevance_score REAL NOT NULL,
    factors JSONB NOT NULL,
    outcome VARCHAR(50), -- 'success', 'ignored', 'conflict'
    feedback_score REAL, -- Feedback qualité intervention
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

### Modèles Pydantic
```python
# models/relevance_models.py
from pydantic import BaseModel, Field, validator
from typing import Dict, List, Optional, Any
from datetime import datetime
from enum import Enum

class RelevanceFactor(BaseModel):
    """Facteur individuel de pertinence."""
    name: str = Field(..., description="Nom du facteur")
    value: float = Field(..., ge=0, le=1, description="Valeur du facteur [0-1]")
    weight: float = Field(..., ge=0, le=1, description="Poids du facteur [0-1]")
    explanation: Optional[str] = Field(None, description="Explication facteur")
    metadata: Dict[str, Any] = Field(default_factory=dict)

class ConversationContext(BaseModel):
    """Contexte de conversation pour calcul pertinence."""
    channel_id: str = Field(..., description="ID du canal")
    server_id: str = Field(..., description="ID du serveur")
    recent_messages: List[Dict[str, Any]] = Field(default_factory=list)
    participants: List[str] = Field(default_factory=list)
    topic: Optional[str] = Field(None, description="Sujet conversation")
    urgency_level: float = Field(0.5, ge=0, le=1, description="Niveau urgence")
    conversation_flow: str = Field("normal", description="Type de flow")

class AgentState(BaseModel):
    """État actuel d'un agent."""
    agent_id: str
    status: str = Field(..., regex="^(active|paused|working|error)$")
    current_workload: float = Field(0, ge=0, le=1, description="Charge actuelle")
    expertise_areas: List[str] = Field(default_factory=list)
    performance_score: float = Field(0.5, ge=0, le=1)
    recent_activity: Dict[str, Any] = Field(default_factory=dict)
    personality_weights: Dict[str, float] = Field(default_factory=dict)
    last_intervention: Optional[datetime] = None

class RelevanceScore(BaseModel):
    """Score de pertinence calculé."""
    agent_id: str
    score: float = Field(..., ge=0, le=1, description="Score final [0-1]")
    factors: Dict[str, RelevanceFactor] = Field(..., description="Détail facteurs")
    decision: str = Field(..., regex="^(intervene|observe|reflect)$")
    confidence: float = Field(..., ge=0, le=1, description="Confiance décision")
    explanation: str = Field(..., description="Explication décision")
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    
    @validator('factors')
    def validate_factors_sum_weights(cls, v):
        total_weight = sum(factor.weight for factor in v.values())
        if not (0.99 <= total_weight <= 1.01):  # Tolérance arrondi
            raise ValueError(f"Poids facteurs doivent sommer à 1.0, got {total_weight}")
        return v

class DecisionOutcome(BaseModel):
    """Résultat d'une décision d'intervention."""
    decision_id: str
    agent_id: str
    outcome_type: str = Field(..., regex="^(success|ignored|conflict|inappropriate)$")
    quality_score: Optional[float] = Field(None, ge=0, le=1)
    feedback: Optional[str] = None
    improvement_suggestions: List[str] = Field(default_factory=list)
    recorded_at: datetime = Field(default_factory=datetime.utcnow)
```

---

## 🔧 OUTILS ET INTÉGRATIONS

### Integration ChromaDB pour Mémoire
```python
# services/memory_service.py
import chromadb
from chromadb.config import Settings
import numpy as np
from typing import List, Dict, Any, Optional

class MemoryService:
    """Service gestion mémoire agents avec ChromaDB."""
    
    def __init__(self, chromadb_url: str):
        self.client = chromadb.HttpClient(host=chromadb_url)
        self.collections = {}
        
    async def initialize_agent_memory(self, agent_id: str) -> None:
        """Initialise mémoire pour un agent."""
        collection_name = f"agent_{agent_id}_memory"
        
        self.collections[agent_id] = self.client.create_collection(
            name=collection_name,
            metadata={"description": f"Memory for agent {agent_id}"}
        )
        
    async def store_conversation(
        self, 
        agent_id: str, 
        conversation: Dict[str, Any],
        embedding: Optional[List[float]] = None
    ) -> str:
        """Stocke conversation dans mémoire agent."""
        
        collection = self.collections.get(agent_id)
        if not collection:
            await self.initialize_agent_memory(agent_id)
            collection = self.collections[agent_id]
            
        # Génération embedding si pas fourni
        if not embedding:
            embedding = await self._generate_embedding(conversation['content'])
            
        # Stockage avec métadonnées
        doc_id = f"conv_{conversation['timestamp']}"
        collection.add(
            embeddings=[embedding],
            documents=[conversation['content']],
            metadatas=[{
                'agent_id': agent_id,
                'channel_id': conversation['channel_id'],
                'timestamp': conversation['timestamp'],
                'participants': conversation['participants'],
                'topic': conversation.get('topic', ''),
                'quality_score': conversation.get('quality_score', 0.5)
            }],
            ids=[doc_id]
        )
        
        return doc_id
        
    async def retrieve_relevant_memories(
        self, 
        agent_id: str, 
        query: str, 
        n_results: int = 5,
        filters: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """Récupère souvenirs pertinents pour contexte."""
        
        collection = self.collections.get(agent_id)
        if not collection:
            return []
            
        # Génération embedding pour requête
        query_embedding = await self._generate_embedding(query)
        
        # Construction filtres ChromaDB
        where_clause = {}
        if filters:
            where_clause.update(filters)
            
        # Recherche similarité
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results,
            where=where_clause,
            include=['documents', 'metadatas', 'distances']
        )
        
        # Formatage résultats
        memories = []
        for i, doc in enumerate(results['documents'][0]):
            memories.append({
                'content': doc,
                'metadata': results['metadatas'][0][i],
                'similarity': 1 - results['distances'][0][i],  # Distance -> similarité
                'relevance_score': self._calculate_memory_relevance(
                    results['metadatas'][0][i], 
                    query
                )
            })
            
        return sorted(memories, key=lambda x: x['relevance_score'], reverse=True)
        
    async def _generate_embedding(self, text: str) -> List[float]:
        """Génère embedding pour texte."""
        # Intégration avec sentence-transformers local
        # À implémenter selon modèle embedding choisi
        pass
        
    def _calculate_memory_relevance(
        self, 
        memory_metadata: Dict[str, Any], 
        current_context: str
    ) -> float:
        """Calcule pertinence souvenir pour contexte actuel."""
        # Facteurs : récence, similarité sujet, qualité, participants communs
        relevance_factors = {
            'recency': self._calculate_recency_factor(memory_metadata['timestamp']),
            'topic_similarity': self._calculate_topic_similarity(
                memory_metadata.get('topic', ''), 
                current_context
            ),
            'quality': memory_metadata.get('quality_score', 0.5),
            'context_match': self._calculate_context_match(
                memory_metadata, 
                current_context
            )
        }
        
        # Score pondéré
        weights = {'recency': 0.2, 'topic_similarity': 0.4, 'quality': 0.2, 'context_match': 0.2}
        return sum(factor * weights[name] for name, factor in relevance_factors.items())
```

### Integration Ollama Optimisée
```python
# services/ollama_service.py
import aiohttp
import asyncio
import json
from typing import Dict, Any, List, Optional, AsyncGenerator
import logging

logger = logging.getLogger(__name__)

class OllamaService:
    """Service optimisé pour interactions Ollama."""
    
    def __init__(self, base_url: str = "http://ollama:11434"):
        self.base_url = base_url
        self.session: Optional[aiohttp.ClientSession] = None
        self.model_cache: Dict[str, Any] = {}
        
    async def __aenter__(self):
        self.session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=300),  # 5 min timeout
            connector=aiohttp.TCPConnector(limit=10)
        )
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
            
    async def generate_response(
        self,
        model: str,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        stream: bool = False
    ) -> Dict[str, Any]:
        """Génère réponse via Ollama."""
        
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": stream,
            "options": {
                "temperature": temperature,
                "num_predict": max_tokens or -1
            }
        }
        
        if system_prompt:
            payload["system"] = system_prompt
            
        try:
            async with self.session.post(
                f"{self.base_url}/api/generate",
                json=payload
            ) as response:
                
                if response.status != 200:
                    error_text = await response.text()
                    raise OllamaError(f"Ollama error {response.status}: {error_text}")
                    
                if stream:
                    return await self._handle_streaming_response(response)
                else:
                    result = await response.json()
                    return {
                        "response": result.get("response", ""),
                        "model": model,
                        "done": result.get("done", False),
                        "context": result.get("context", []),
                        "total_duration": result.get("total_duration", 0),
                        "load_duration": result.get("load_duration", 0),
                        "prompt_eval_count": result.get("prompt_eval_count", 0),
                        "eval_count": result.get("eval_count", 0)
                    }
                    
        except asyncio.TimeoutError:
            logger.error(f"Timeout calling Ollama for model {model}")
            raise OllamaTimeoutError(f"Timeout after 300s for model {model}")
        except Exception as e:
            logger.error(f"Error calling Ollama: {e}", exc_info=True)
            raise OllamaError(f"Failed to generate response: {e}")
            
    async def _handle_streaming_response(
        self, 
        response: aiohttp.ClientResponse
    ) -> AsyncGenerator[Dict[str, Any], None]:
        """Gère réponse streaming Ollama."""
        async for line in response.content:
            if line:
                try:
                    data = json.loads(line.decode('utf-8'))
                    yield data
                except json.JSONDecodeError:
                    continue
                    
    async def list_models(self) -> List[Dict[str, Any]]:
        """Liste modèles disponibles."""
        try:
            async with self.session.get(f"{self.base_url}/api/tags") as response:
                if response.status == 200:
                    result = await response.json()
                    return result.get("models", [])
                else:
                    logger.error(f"Failed to list models: {response.status}")
                    return []
        except Exception as e:
            logger.error(f"Error listing models: {e}")
            return []
            
    async def load_model(self, model: str) -> bool:
        """Charge modèle en mémoire si pas déjà fait."""
        if model in self.model_cache:
            return True
            
        try:
            # Test génération simple pour charger modèle
            await self.generate_response(
                model=model,
                prompt="Hello",
                max_tokens=1
            )
            self.model_cache[model] = True
            return True
        except Exception as e:
            logger.error(f"Failed to load model {model}: {e}")
            return False
            
    async def health_check(self) -> Dict[str, Any]:
        """Vérification santé service Ollama."""
        try:
            async with self.session.get(f"{self.base_url}/api/tags") as response:
                return {
                    "status": "healthy" if response.status == 200 else "unhealthy",
                    "response_time": response.headers.get("X-Response-Time", "N/A"),
                    "models_available": len(await self.list_models())
                }
        except Exception as e:
            return {
                "status": "unhealthy",
                "error": str(e)
            }

class OllamaError(Exception):
    """Exception Ollama générale."""
    pass

class OllamaTimeoutError(OllamaError):
    """Exception timeout Ollama."""
    pass
```

---

## 📊 MONITORING ET DEBUGGING

### Logging Structuré
```python
# core/logging_config.py
import logging
import json
from datetime import datetime
from typing import Dict, Any
import sys

class StructuredLogger:
    """Logger structuré pour debugging et monitoring."""
    
    def __init__(self, name: str, level: str = "INFO"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(getattr(logging, level.upper()))
        
        # Handler console avec format structuré
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(StructuredFormatter())
        self.logger.addHandler(handler)
        
    def debug(self, message: str, **kwargs):
        self._log("DEBUG", message, **kwargs)
        
    def info(self, message: str, **kwargs):
        self._log("INFO", message, **kwargs)
        
    def warning(self, message: str, **kwargs):
        self._log("WARNING", message, **kwargs)
        
    def error(self, message: str, **kwargs):
        self._log("ERROR", message, **kwargs)
        
    def _log(self, level: str, message: str, **kwargs):
        extra = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": level,
            "message": message,
            **kwargs
        }
        self.logger.log(getattr(logging, level), json.dumps(extra))

class StructuredFormatter(logging.Formatter):
    """Formateur pour logs JSON structurés."""
    
    def format(self, record):
        if hasattr(record, 'msg') and record.msg.startswith('{'):
            # Déjà formaté JSON
            return record.msg
        else:
            # Format standard → JSON
            return json.dumps({
                "timestamp": datetime.utcnow().isoformat(),
                "level": record.levelname,
                "logger": record.name,
                "message": record.getMessage(),
                "module": record.module,
                "function": record.funcName,
                "line": record.lineno
            })

# Usage dans services
logger = StructuredLogger("relevance-engine")

# Exemples logging
logger.info("Calculating relevance score", 
            agent_id="agent-123", 
            channel_id="channel-456", 
            factors_count=5)

logger.error("Failed to retrieve agent state", 
             agent_id="agent-123", 
             error="AgentNotFound", 
             stack_trace=traceback.format_exc())
```

### Métriques Prometheus
```python
# monitoring/metrics.py
from prometheus_client import Counter, Histogram, Gauge, Info
import time
from functools import wraps
from typing import Callable, Any

# Métriques globales
REQUEST_COUNT = Counter(
    'almaa_requests_total',
    'Total requests by endpoint and method',
    ['method', 'endpoint', 'status']
)

REQUEST_DURATION = Histogram(
    'almaa_request_duration_seconds',
    'Request duration in seconds',
    ['method', 'endpoint']
)

AGENT_STATES = Gauge(
    'almaa_agent_states',
    'Number of agents by state',
    ['state']
)

RELEVANCE_SCORES = Histogram(
    'almaa_relevance_scores',
    'Distribution of relevance scores',
    ['agent_type']
)

OLLAMA_REQUESTS = Counter(
    'almaa_ollama_requests_total',
    'Total requests to Ollama',
    ['model', 'status']
)

OLLAMA_DURATION = Histogram(
    'almaa_ollama_duration_seconds',
    'Ollama request duration',
    ['model']
)

MEMORY_OPERATIONS = Counter(
    'almaa_memory_operations_total',
    'Memory operations',
    ['operation', 'agent_id']
)

# Décorateurs pour métriques automatiques
def track_requests(endpoint: str = None):
    """Décorateur pour tracker requêtes HTTP."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            endpoint_name = endpoint or func.__name__
            start_time = time.time()
            
            try:
                result = await func(*args, **kwargs)
                REQUEST_COUNT.labels(
                    method='POST',  # À adapter selon contexte
                    endpoint=endpoint_name,
                    status='success'
                ).inc()
                return result
            except Exception as e:
                REQUEST_COUNT.labels(
                    method='POST',
                    endpoint=endpoint_name,
                    status='error'
                ).inc()
                raise
            finally:
                REQUEST_DURATION.labels(
                    method='POST',
                    endpoint=endpoint_name
                ).observe(time.time() - start_time)
                
        return wrapper
    return decorator

def track_ollama_calls(model: str):
    """Décorateur pour tracker appels Ollama."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time.time()
            
            try:
                result = await func(*args, **kwargs)
                OLLAMA_REQUESTS.labels(model=model, status='success').inc()
                return result
            except Exception:
                OLLAMA_REQUESTS.labels(model=model, status='error').inc()
                raise
            finally:
                OLLAMA_DURATION.labels(model=model).observe(time.time() - start_time)
                
        return wrapper
    return decorator

# Exemple usage
@track_requests('calculate_relevance')
async def calculate_relevance_score(agent_id: str, context: Any) -> float:
    # Logique calcul...
    score = 0.75
    RELEVANCE_SCORES.labels(agent_type='developer').observe(score)
    return score
```

---

## ⚠️ SÉCURITÉ ET VALIDATION

### Validation Inputs
```python
# core/validation.py
from pydantic import BaseModel, validator, ValidationError
from typing import Any, Dict, List, Optional
import re
import html

class InputValidator:
    """Validateur inputs sécurisé."""
    
    @staticmethod
    def sanitize_string(value: str) -> str:
        """Sanitise chaîne de caractères."""
        if not isinstance(value, str):
            raise ValueError("Input must be string")
            
        # HTML escaping
        sanitized = html.escape(value)
        
        # Suppression caractères dangereux
        sanitized = re.sub(r'[<>"\']', '', sanitized)
        
        # Limitation longueur
        if len(sanitized) > 10000:
            raise ValueError("String too long (max 10000 chars)")
            
        return sanitized.strip()
    
    @staticmethod
    def validate_agent_id(agent_id: str) -> str:
        """Valide format ID agent."""
        if not re.match(r'^[a-zA-Z0-9_-]{1,50}$', agent_id):
            raise ValueError("Invalid agent ID format")
        return agent_id
    
    @staticmethod
    def validate_model_name(model: str) -> str:
        """Valide nom modèle Ollama."""
        allowed_models = [
            "llama3.1:8b", "codellama:7b", "mistral:7b", 
            "phi3:3.8b", "gemma:2b", "qwen:4b"
        ]
        if model not in allowed_models:
            raise ValueError(f"Model {model} not allowed")
        return model
    
    @staticmethod
    def validate_file_path(path: str) -> str:
        """Valide chemin fichier sécurisé."""
        # Empêche path traversal
        if '..' in path or path.startswith('/'):
            raise ValueError("Invalid file path")
            
        # Caractères autorisés
        if not re.match(r'^[a-zA-Z0-9_/.-]+$', path):
            raise ValueError("Invalid characters in path")
            
        return path

class SecureRequest(BaseModel):
    """Base pour requêtes sécurisées."""
    
    class Config:
        validate_assignment = True
        extra = "forbid"  # Empêche champs supplémentaires
        
    @validator('*', pre=True)
    def sanitize_strings(cls, v):
        if isinstance(v, str):
            return InputValidator.sanitize_string(v)
        return v
```

### Sandbox Exécution
```python
# security/sandbox.py
import docker
import tempfile
import os
import shutil
from typing import Dict, Any, Optional
import asyncio
from pathlib import Path

class DockerSandbox:
    """Sandbox Docker pour exécution sécurisée outils."""
    
    def __init__(self):
        self.client = docker.from_env()
        self.base_image = "python:3.11-alpine"
        self.network_name = "almaa_sandbox"
        
    async def execute_tool(
        self,
        tool_name: str,
        code: str,
        files: Dict[str, str] = None,
        env_vars: Dict[str, str] = None,
        timeout: int = 300
    ) -> Dict[str, Any]:
        """Exécute outil dans sandbox sécurisé."""
        
        # Création environnement temporaire
        with tempfile.TemporaryDirectory() as tmp_dir:
            workspace = Path(tmp_dir)
            
            # Écriture fichiers
            if files:
                for filename, content in files.items():
                    file_path = workspace / filename
                    file_path.parent.mkdir(parents=True, exist_ok=True)
                    file_path.write_text(content)
            
            # Script principal
            main_script = workspace / "main.py"
            main_script.write_text(code)
            
            # Configuration container
            container_config = {
                'image': self.base_image,
                'command': f'python /workspace/main.py',
                'working_dir': '/workspace',
                'volumes': {
                    str(workspace): {
                        'bind': '/workspace',
                        'mode': 'rw'
                    }
                },
                'environment': env_vars or {},
                'network_mode': self.network_name,
                'mem_limit': '512m',
                'cpu_quota': 50000,  # 50% CPU
                'security_opt': ['no-new-privileges'],
                'cap_drop': ['ALL'],
                'read_only': True,
                'tmpfs': {'/tmp': 'noexec,nosuid,size=100m'},
                'detach': True,
                'remove': True
            }
            
            try:
                # Exécution container
                container = self.client.containers.run(**container_config)
                
                # Attente avec timeout
                result = await asyncio.wait_for(
                    self._wait_container_completion(container),
                    timeout=timeout
                )
                
                return result
                
            except asyncio.TimeoutError:
                # Timeout → kill container
                try:
                    container.kill()
                except:
                    pass
                return {
                    'success': False,
                    'error': f'Tool execution timeout after {timeout}s',
                    'stdout': '',
                    'stderr': '',
                    'exit_code': -1
                }
            except Exception as e:
                return {
                    'success': False,
                    'error': f'Sandbox execution error: {e}',
                    'stdout': '',
                    'stderr': '',
                    'exit_code': -1
                }
    
    async def _wait_container_completion(self, container) -> Dict[str, Any]:
        """Attend complétion container et récupère résultats."""
        
        # Attente fin exécution
        exit_code = container.wait()['StatusCode']
        
        # Récupération logs
        logs = container.logs()
        stdout = logs.decode('utf-8', errors='ignore')
        
        # Récupération fichiers output si existants
        output_files = {}
        try:
            # Exemple : récupération fichier résultats
            output_tar = container.get_archive('/workspace/output')[0]
            # Processing tar si nécessaire...
        except:
            pass
        
        return {
            'success': exit_code == 0,
            'exit_code': exit_code,
            'stdout': stdout,
            'stderr': '',  # Docker combine stdout/stderr
            'output_files': output_files,
            'execution_time': 0  # À calculer si nécessaire
        }
    
    def setup_network(self):
        """Configure réseau isolé pour sandboxes."""
        try:
            # Réseau sans accès internet
            self.client.networks.create(
                name=self.network_name,
                driver="bridge",
                internal=True,  # Pas d'accès externe
                options={
                    "com.docker.network.bridge.enable_icc": "false"  # Isolation inter-containers
                }
            )
        except docker.errors.APIError as e:
            if "already exists" not in str(e):
                raise
```

---

## 🚀 DÉPLOIEMENT ET TESTS

### Scripts de Développement
```bash
#!/bin/bash
# scripts/dev-setup.sh

set -e

echo "🚀 Setting up ALMAA Workspace development environment..."

# Vérification Docker
if ! command -v docker &> /dev/null; then
    echo "❌ Docker required but not installed"
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose required but not installed"
    exit 1
fi

# Création réseaux Docker
echo "📡 Creating Docker networks..."
docker network create almaa-network 2>/dev/null || echo "Network already exists"
docker network create almaa-sandbox --internal 2>/dev/null || echo "Sandbox network already exists"

# Variables environnement
if [ ! -f .env ]; then
    echo "⚙️ Creating environment configuration..."
    cat > .env << EOF
# Database
DB_PASSWORD=$(openssl rand -base64 32)
POSTGRES_USER=almaa
POSTGRES_DB=almaa

# MinIO
MINIO_ACCESS_KEY=almaa-admin
MINIO_SECRET_KEY=$(openssl rand -base64 32)

# Monitoring
GRAFANA_PASSWORD=$(openssl rand -base64 16)

# Security
JWT_SECRET_KEY=$(openssl rand -base64 64)
ENCRYPTION_KEY=$(openssl rand -base64 32)

# Development
DEBUG=true
LOG_LEVEL=DEBUG
ENVIRONMENT=development
EOF
    echo "✅ Environment configuration created (.env)"
fi

# Génération certificats SSL auto-signés
if [ ! -d "nginx/ssl" ]; then
    echo "🔐 Generating SSL certificates..."
    mkdir -p nginx/ssl
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
        -keyout nginx/ssl/almaa.key \
        -out nginx/ssl/almaa.crt \
        -subj "/C=FR/ST=Local/L=Local/O=ALMAA/CN=almaa.local"
    echo "✅ SSL certificates generated"
fi

# Build images développement
echo "🏗️ Building development images..."
docker-compose -f docker-compose.dev.yml build

# Initialisation base de données
echo "🗃️ Initializing database..."
docker-compose -f docker-compose.dev.yml up -d postgres redis
sleep 10

# Migrations
docker-compose -f docker-compose.dev.yml exec postgres psql -U almaa -d almaa -c "
CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";
CREATE EXTENSION IF NOT EXISTS \"pgvector\";
"

# Test connexions
echo "🔍 Testing connections..."
docker-compose -f docker-compose.dev.yml up -d ollama chromadb minio
sleep 15

# Validation Ollama
echo "Testing Ollama..."
curl -sf http://localhost:11434/api/tags > /dev/null && echo "✅ Ollama OK" || echo "❌ Ollama failed"

# Validation ChromaDB
echo "Testing ChromaDB..."
curl -sf http://localhost:8000/api/v1/heartbeat > /dev/null && echo "✅ ChromaDB OK" || echo "❌ ChromaDB failed"

# Validation MinIO
echo "Testing MinIO..."
curl -sf http://localhost:9001 > /dev/null && echo "✅ MinIO OK" || echo "❌ MinIO failed"

# Démarrage complet
echo "🚀 Starting complete development environment..."
docker-compose -f docker-compose.dev.yml up -d

echo ""
echo "🎉 Development environment ready!"
echo "📊 Admin Dashboard: https://localhost (admin/admin)"
echo "📊 Grafana: http://localhost:3000 (admin/$(grep GRAFANA_PASSWORD .env | cut -d'=' -f2))"
echo "🗃️ MinIO Console: http://localhost:9001 (almaa-admin/SECRET)"
echo "🔧 API Docs: http://localhost:8000/docs"
echo ""
echo "📝 Next steps:"
echo "1. Load Ollama models: docker-compose exec ollama ollama pull llama3.1:8b"
echo "2. Run tests: ./scripts/run-tests.sh"
echo "3. View logs: docker-compose logs -f"
```

### Tests Automatisés
```bash
#!/bin/bash
# scripts/run-tests.sh

set -e

echo "🧪 Running ALMAA Workspace test suite..."

# Tests unitaires Python
echo "📋 Running Python unit tests..."
docker-compose -f docker-compose.test.yml run --rm api pytest tests/unit/ -v --cov=src --cov-report=term-missing

# Tests intégration
echo "📋 Running integration tests..."
docker-compose -f docker-compose.test.yml run --rm api pytest tests/integration/ -v

# Tests frontend
echo "📋 Running frontend tests..."
docker-compose -f docker-compose.test.yml run --rm frontend npm test

# Tests end-to-end
echo "📋 Running E2E tests..."
docker-compose -f docker-compose.test.yml run --rm e2e-tests

# Vérifications sécurité
echo "🔒 Running security checks..."
docker-compose -f docker-compose.test.yml run --rm security-scanner

# Tests performance
echo "⚡ Running performance tests..."
docker-compose -f docker-compose.test.yml run --rm load-tests

# Nettoyage
echo "🧹 Cleaning up test environment..."
docker-compose -f docker-compose.test.yml down -v

echo "✅ All tests passed!"
```

---

## 📖 CONCLUSION POUR GPT-5

Ce guide complet te donne tous les éléments nécessaires pour développer ALMAA Workspace V2.0 avec succès :

### 🎯 **Priorités Absolues**
1. **Système de Pertinence** → Agents parlent quand c'est pertinent
2. **Interface Admin** → Contrôle complet des agents
3. **Templates Agents** → Spécialisation et configuration
4. **Communication Inter-Agents** → MPs et canaux deepthink

### 🛠️ **Standards Qualité**
- Code documenté et testé
- Validation sécurisée de tous inputs
- Logging structuré pour debugging
- Métriques Prometheus intégrées
- Configuration flexible YAML

### 🚀 **Approche Recommandée**
1. **Analyse Code Existant** → Comprendre l'architecture actuelle
2. **Développement Incrémental** → Extensions pas reconstruction
3. **Tests Continus** → Validation à chaque étape
4. **Documentation** → Explique chaque choix technique

### 💬 **Communication**
- Pose des questions sur l'architecture existante
- Explique tes choix techniques
- Signale les compromis ou limitations
- Propose des améliorations d'architecture

**Ensemble, nous allons créer l'assistant AGI personnel le plus avancé et sécurisé possible ! 🚀**