# 🏗️ ARCHITECTURE TECHNIQUE ALMAA WORKSPACE V2.0

## 📐 VUE D'ENSEMBLE ARCHITECTURE

### 🎯 Principes Directeurs
```yaml
Design Principles:
  modularity: "Architecture microservices modulaire et extensible"
  offline_first: "100% offline, zéro dépendance internet"
  security: "Isolation complète et sandboxing sécurisé"
  scalability: "Architecture prête pour scaling massif (1000+ agents)"
  maintainability: "Code maintenable et documentation complète"
  performance: "Optimisé pour temps réel et charge élevée"
```

---

## 🏢 ARCHITECTURE GLOBAL SYSTEM

### Diagramme Architecture Complète
```mermaid
graph TB
    subgraph "Frontend Layer"
        UI[Next.js Admin Dashboard]
        Chat[Chat Interface]
        Debug[Debug Interface]
    end
    
    subgraph "API Gateway"
        Nginx[Nginx Reverse Proxy]
        API[FastAPI Core]
        WS[WebSocket Manager]
    end
    
    subgraph "Agent Management Layer"
        AF[Agent Factory]
        AL[Agent Lifecycle]
        AT[Agent Templates] 
        RE[Relevance Engine]
        PM[Performance Monitor]
    end
    
    subgraph "Communication Layer"
        CC[Channel Controller]
        MP[Message Processor]
        NM[Notification Manager]
        VS[Voting System]
    end
    
    subgraph "Tool System Layer"
        TR[Tool Registry]
        TE[Tool Executor]
        PS[Permission System]
        SB[Sandbox Manager]
    end
    
    subgraph "Memory & Context Layer"
        MM[Memory Manager]
        CDB[(ChromaDB)]
        CS[Context Switcher]
        AR[Archive System]
    end
    
    subgraph "Data Layer"
        PG[(PostgreSQL)]
        RD[(Redis)]
        MO[(MinIO)]
    end
    
    subgraph "AI Layer"
        OL[Ollama Server]
        ML[Model Loader]
        IM[Inference Manager]
    end
    
    subgraph "Monitoring & Security"
        PR[Prometheus]
        GR[Grafana]
        LK[Loki]
        AU[Audit Logger]
    end

    UI --> Nginx
    Chat --> Nginx
    Debug --> Nginx
    Nginx --> API
    Nginx --> WS
    
    API --> AF
    API --> CC
    API --> TR
    WS --> RE
    WS --> MP
    
    AF --> AL
    AF --> AT
    RE --> PM
    
    CC --> MP
    CC --> VS
    MP --> NM
    
    TR --> TE
    TR --> PS
    TE --> SB
    
    MM --> CDB
    MM --> CS
    CS --> AR
    
    AL --> PG
    CC --> PG
    TR --> PG
    
    RE --> RD
    MP --> RD
    VS --> RD
    
    TE --> MO
    AR --> MO
    
    AL --> OL
    RE --> OL
    TE --> OL
    OL --> ML
    OL --> IM
    
    API --> PR
    WS --> PR
    PR --> GR
    AU --> LK
    LK --> GR
```

---

## 🔧 COUCHES ARCHITECTURE DÉTAILLÉES

### 1. Frontend Layer - Interface Utilisateur

#### Next.js Admin Dashboard
```typescript
// Structure Frontend Complète
frontend/
├── src/
│   ├── components/
│   │   ├── agents/
│   │   │   ├── AgentCard.tsx              # Carte agent individuel
│   │   │   ├── AgentCreator.tsx           # Interface création agent
│   │   │   ├── AgentConfigurator.tsx      # Configuration agent
│   │   │   ├── AgentPerformance.tsx       # Métriques performance
│   │   │   └── AgentDebugger.tsx          # Mode debug agent
│   │   ├── dashboard/
│   │   │   ├── Overview.tsx               # Vue d'ensemble système
│   │   │   ├── SystemMetrics.tsx          # Métriques système
│   │   │   ├── NotificationCenter.tsx     # Centre notifications
│   │   │   └── QuickActions.tsx           # Actions rapides
│   │   ├── projects/
│   │   │   ├── ProjectManager.tsx         # Gestionnaire projets
│   │   │   ├── FileExplorer.tsx           # Explorateur fichiers
│   │   │   ├── ProjectAnalytics.tsx       # Analytics projet
│   │   │   └── TaskInjector.tsx           # Injection tâches
│   │   ├── communication/
│   │   │   ├── ChatInterface.tsx          # Interface chat principale
│   │   │   ├── PrivateMessages.tsx        # Messages privés
│   │   │   ├── ChannelManager.tsx         # Gestion canaux
│   │   │   └── VotingInterface.tsx        # Interface votes
│   │   ├── tools/
│   │   │   ├── ToolMarketplace.tsx        # Marketplace outils
│   │   │   ├── ToolPermissions.tsx        # Gestion permissions
│   │   │   ├── ToolExecutor.tsx           # Exécution outils
│   │   │   └── ToolAnalytics.tsx          # Analytics usage
│   │   └── monitoring/
│   │       ├── RealTimeMonitor.tsx        # Monitoring temps réel
│   │       ├── PerformanceDashboard.tsx   # Dashboard performance
│   │       ├── LogViewer.tsx              # Visualiseur logs
│   │       └── AlertManager.tsx           # Gestionnaire alertes
│   ├── pages/
│   │   ├── dashboard/
│   │   │   ├── index.tsx                  # Dashboard principal
│   │   │   ├── agents.tsx                 # Gestion agents
│   │   │   ├── projects.tsx               # Gestion projets
│   │   │   ├── tools.tsx                  # Gestion outils
│   │   │   ├── monitoring.tsx             # Monitoring
│   │   │   └── settings.tsx               # Configuration
│   │   ├── chat/
│   │   │   ├── [channelId].tsx            # Interface chat canal
│   │   │   └── private/[agentId].tsx      # Chat privé agent
│   │   └── debug/
│   │       ├── agents.tsx                 # Debug agents
│   │       ├── system.tsx                 # Debug système
│   │       └── logs.tsx                   # Debug logs
│   ├── hooks/
│   │   ├── useWebSocket.ts                # Hook WebSocket
│   │   ├── useAgentManagement.ts          # Hook gestion agents
│   │   ├── useProjectManagement.ts        # Hook gestion projets
│   │   ├── useRealtimeData.ts             # Hook données temps réel
│   │   └── useNotifications.ts            # Hook notifications
│   ├── stores/
│   │   ├── agentStore.ts                  # Store state agents
│   │   ├── projectStore.ts                # Store state projets
│   │   ├── chatStore.ts                   # Store state chat
│   │   └── uiStore.ts                     # Store state UI
│   └── utils/
│       ├── api.ts                         # Utilitaires API
│       ├── websocket.ts                   # Utilitaires WebSocket
│       ├── formatting.ts                  # Formatage données
│       └── validation.ts                  # Validation formulaires
├── public/
│   ├── icons/                             # Icons interface
│   ├── fonts/                             # Fonts locales
│   └── assets/                            # Assets statiques
└── styles/
    ├── globals.css                        # Styles globaux
    ├── components/                        # Styles composants
    └── themes/                            # Thèmes interface
```

#### Fonctionnalités Interface Prioritaires
```yaml
Dashboard Principal:
  overview: "Vue temps réel tous agents et système"
  quick_controls: "Pause/reprendre agents, injection tâches"
  notifications: "Centre notifications par priorité"
  metrics: "KPIs performance et productivité"
  
Agent Management:
  creation: "Interface création agents avec templates"
  configuration: "Configuration complète paramètres"
  monitoring: "Suivi performance individuelle"
  debug: "Mode debug pensées temps réel"
  
Project Management:
  organization: "Structure projets et fichiers"
  collaboration: "Assignation agents par projet"
  progress: "Suivi avancement et métriques"
  analytics: "Analytics productivité projet"
  
Communication:
  chat: "Interface chat Discord-like"
  private_messages: "MP entre agents et avec admin"
  voting: "Interface votes et consensus"
  moderation: "Outils modération et sanctions"
```

### 2. API Gateway - Point d'Entrée Système

#### Nginx Reverse Proxy
```nginx
# Configuration Nginx Production
upstream fastapi_backend {
    server api:8000;
    server api:8001 backup;
}

upstream websocket_backend {
    server websocket:8080;
}

server {
    listen 443 ssl http2;
    server_name almaa.local;
    
    ssl_certificate /etc/nginx/ssl/almaa.crt;
    ssl_certificate_key /etc/nginx/ssl/almaa.key;
    
    # Frontend statique
    location / {
        root /var/www/almaa;
        try_files $uri $uri/ /index.html;
        
        # Cache statique
        location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg)$ {
            expires 1y;
            add_header Cache-Control "public, no-transform";
        }
    }
    
    # API REST
    location /api/ {
        proxy_pass http://fastapi_backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # Timeouts pour tâches longues
        proxy_connect_timeout 60s;
        proxy_send_timeout 300s;
        proxy_read_timeout 300s;
    }
    
    # WebSocket
    location /ws/ {
        proxy_pass http://websocket_backend;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
    
    # Upload fichiers
    location /upload/ {
        client_max_body_size 100M;
        proxy_pass http://fastapi_backend;
        proxy_request_buffering off;
    }
    
    # Monitoring
    location /metrics {
        proxy_pass http://prometheus:9090;
        auth_basic "Metrics";
        auth_basic_user_file /etc/nginx/.htpasswd;
    }
    
    # Security headers
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;
    add_header X-XSS-Protection "1; mode=block";
    add_header Strict-Transport-Security "max-age=31536000";
}
```

#### FastAPI Core API
```python
# Structure API Core
api/
├── src/
│   ├── main.py                           # Application FastAPI principale
│   ├── config/
│   │   ├── settings.py                   # Configuration application
│   │   ├── database.py                   # Configuration base données
│   │   └── security.py                   # Configuration sécurité
│   ├── routers/
│   │   ├── agents.py                     # Endpoints gestion agents
│   │   ├── projects.py                   # Endpoints gestion projets
│   │   ├── tools.py                      # Endpoints gestion outils
│   │   ├── communication.py              # Endpoints communication
│   │   ├── files.py                      # Endpoints gestion fichiers
│   │   ├── monitoring.py                 # Endpoints monitoring
│   │   └── admin.py                      # Endpoints administration
│   ├── models/
│   │   ├── agent.py                      # Modèles données agents
│   │   ├── project.py                    # Modèles données projets
│   │   ├── message.py                    # Modèles messages
│   │   ├── tool.py                       # Modèles outils
│   │   └── user.py                       # Modèles utilisateur
│   ├── schemas/
│   │   ├── agent_schemas.py              # Schémas validation agents
│   │   ├── project_schemas.py            # Schémas validation projets
│   │   ├── message_schemas.py            # Schémas validation messages
│   │   └── tool_schemas.py               # Schémas validation outils
│   ├── services/
│   │   ├── agent_service.py              # Service logique agents
│   │   ├── project_service.py            # Service logique projets
│   │   ├── communication_service.py      # Service communication
│   │   ├── tool_service.py               # Service outils
│   │   └── monitoring_service.py         # Service monitoring
│   ├── core/
│   │   ├── dependencies.py               # Dépendances injection
│   │   ├── exceptions.py                 # Exceptions personnalisées
│   │   ├── middleware.py                 # Middleware personnalisé
│   │   └── utils.py                      # Utilitaires communs
│   └── tests/
│       ├── test_agents.py                # Tests agents
│       ├── test_projects.py              # Tests projets
│       ├── test_tools.py                 # Tests outils
│       └── test_integration.py           # Tests intégration
├── requirements/
│   ├── base.txt                          # Dépendances base
│   ├── dev.txt                           # Dépendances développement
│   └── prod.txt                          # Dépendances production
└── docker/
    ├── Dockerfile                        # Image Docker API
    └── entrypoint.sh                     # Script démarrage
```

### 3. Agent Management Layer - Gestion Agents IA

#### Agent Factory - Création et Templates
```python
# Service Factory Agents
agent-factory/
├── src/
│   ├── factory/
│   │   ├── agent_factory.py              # Factory création agents
│   │   ├── template_manager.py           # Gestionnaire templates
│   │   ├── configuration_builder.py     # Builder configuration
│   │   └── validation_engine.py          # Validation configuration
│   ├── templates/
│   │   ├── base_template.py              # Template de base
│   │   ├── developer_template.py         # Template développeur
│   │   ├── analyst_template.py           # Template analyste
│   │   ├── moderator_template.py         # Template modérateur
│   │   ├── researcher_template.py        # Template chercheur
│   │   └── creative_template.py          # Template créatif
│   ├── models/
│   │   ├── agent_config.py               # Configuration agent
│   │   ├── template_schema.py            # Schéma template
│   │   ├── personality_model.py          # Modèle personnalité
│   │   └── capability_model.py           # Modèle capacités
│   └── api/
│       ├── factory_api.py                # API factory
│       └── template_api.py               # API templates
├── templates/                            # Templates pré-configurés
│   ├── developer-backend.yaml
│   ├── developer-frontend.yaml
│   ├── analyst-data.yaml
│   ├── moderator-quality.yaml
│   ├── researcher-tech.yaml
│   └── creative-writer.yaml
└── tests/
    ├── test_factory.py
    ├── test_templates.py
    └── test_validation.py
```

#### Agent Lifecycle - États et Transitions
```python
# Gestion Cycle de Vie Agents
agent-lifecycle/
├── src/
│   ├── lifecycle/
│   │   ├── state_machine.py              # Machine états agent
│   │   ├── transition_manager.py         # Gestion transitions
│   │   ├── health_monitor.py             # Monitoring santé agents
│   │   └── resource_manager.py           # Gestion ressources
│   ├── states/
│   │   ├── active_state.py               # État actif
│   │   ├── paused_state.py               # État pause
│   │   ├── working_state.py              # État travail
│   │   ├── error_state.py                # État erreur
│   │   └── maintenance_state.py          # État maintenance
│   ├── events/
│   │   ├── lifecycle_events.py           # Événements lifecycle
│   │   ├── performance_events.py         # Événements performance
│   │   └── error_events.py               # Événements erreurs
│   └── handlers/
│       ├── state_handler.py              # Gestionnaire états
│       ├── event_handler.py              # Gestionnaire événements
│       └── recovery_handler.py           # Gestionnaire récupération
├── config/
│   ├── state_transitions.yaml           # Configuration transitions
│   ├── resource_limits.yaml             # Limites ressources
│   └── health_thresholds.yaml           # Seuils santé
└── tests/
    ├── test_lifecycle.py
    ├── test_states.py
    └── test_transitions.py
```

#### Relevance Engine - Système Pertinence
```python
# Engine Pertinence Contextuelle
relevance-engine/
├── src/
│   ├── core/
│   │   ├── relevance_calculator.py       # Calculateur pertinence
│   │   ├── context_analyzer.py           # Analyseur contexte
│   │   ├── decision_engine.py            # Engine décision
│   │   └── learning_system.py            # Système apprentissage
│   ├── factors/
│   │   ├── expertise_factor.py           # Facteur expertise
│   │   ├── workload_factor.py            # Facteur charge travail
│   │   ├── social_factor.py              # Facteur social
│   │   ├── timing_factor.py              # Facteur timing
│   │   └── quality_factor.py             # Facteur qualité
│   ├── models/
│   │   ├── relevance_model.py            # Modèle pertinence
│   │   ├── context_model.py              # Modèle contexte
│   │   ├── conversation_model.py         # Modèle conversation
│   │   └── agent_profile.py              # Profil agent
│   ├── analytics/
│   │   ├── performance_tracker.py        # Suivi performance
│   │   ├── accuracy_measurer.py          # Mesure précision
│   │   └── improvement_suggester.py      # Suggestions amélioration
│   └── api/
│       ├── relevance_api.py              # API pertinence
│       └── analytics_api.py              # API analytics
├── config/
│   ├── relevance_weights.yaml           # Poids facteurs
│   ├── thresholds.yaml                  # Seuils décision
│   └── learning_params.yaml             # Paramètres apprentissage
├── models/                              # Modèles ML si nécessaire
│   ├── relevance_classifier.pkl
│   └── context_embeddings.bin
└── tests/
    ├── test_calculator.py
    ├── test_factors.py
    └── test_decision.py
```

### 4. Communication Layer - Gestion Communications

#### Channel Controller - Gestion Canaux
```python
# Contrôleur Canaux Communication
channel-controller/
├── src/
│   ├── controllers/
│   │   ├── channel_manager.py            # Gestionnaire canaux
│   │   ├── server_manager.py             # Gestionnaire serveurs
│   │   ├── permission_controller.py      # Contrôleur permissions
│   │   └── access_controller.py          # Contrôleur accès
│   ├── models/
│   │   ├── channel_model.py              # Modèle canal
│   │   ├── server_model.py               # Modèle serveur
│   │   ├── permission_model.py           # Modèle permission
│   │   └── access_model.py               # Modèle accès
│   ├── types/
│   │   ├── public_channel.py             # Canal public
│   │   ├── private_channel.py            # Canal privé
│   │   ├── deepthink_channel.py          # Canal réflexion
│   │   └── archive_channel.py            # Canal archive
│   └── services/
│       ├── channel_service.py            # Service canaux
│       ├── routing_service.py            # Service routage
│       └── broadcast_service.py          # Service diffusion
├── config/
│   ├── channel_types.yaml               # Types canaux
│   ├── default_permissions.yaml         # Permissions défaut
│   └── routing_rules.yaml               # Règles routage
└── tests/
    ├── test_channels.py
    ├── test_permissions.py
    └── test_routing.py
```

#### Voting System - Système Votes
```python
# Système Votes et Consensus
voting-system/
├── src/
│   ├── core/
│   │   ├── vote_engine.py                # Engine votes
│   │   ├── consensus_builder.py          # Builder consensus
│   │   ├── participation_manager.py      # Gestion participation
│   │   └── result_processor.py           # Traitement résultats
│   ├── types/
│   │   ├── tool_usage_vote.py            # Vote usage outil
│   │   ├── project_decision_vote.py      # Vote décision projet
│   │   ├── conflict_resolution_vote.py   # Vote résolution conflit
│   │   └── resource_allocation_vote.py   # Vote allocation ressource
│   ├── strategies/
│   │   ├── majority_strategy.py          # Stratégie majorité
│   │   ├── qualified_majority.py         # Majorité qualifiée 66%
│   │   ├── consensus_strategy.py         # Stratégie consensus
│   │   └── weighted_voting.py            # Vote pondéré
│   ├── analytics/
│   │   ├── vote_analyzer.py              # Analyse votes
│   │   ├── participation_tracker.py      # Suivi participation
│   │   └── decision_impact.py            # Impact décisions
│   └── api/
│       ├── voting_api.py                 # API votes
│       └── results_api.py                # API résultats
├── config/
│   ├── vote_types.yaml                  # Types votes
│   ├── thresholds.yaml                  # Seuils validation
│   └── timeouts.yaml                    # Timeouts votes
└── tests/
    ├── test_voting.py
    ├── test_consensus.py
    └── test_strategies.py
```

### 5. Tool System Layer - Système Outils Modulaires

#### Tool Registry - Registre Outils
```python
# Registre et Découverte Outils
tool-registry/
├── src/
│   ├── registry/
│   │   ├── tool_registry.py              # Registre principal
│   │   ├── tool_discoverer.py            # Découverte outils
│   │   ├── capability_mapper.py          # Mapping capacités
│   │   └── dependency_resolver.py        # Résolution dépendances
│   ├── models/
│   │   ├── tool_definition.py            # Définition outil
│   │   ├── capability_model.py           # Modèle capacité
│   │   ├── requirement_model.py          # Modèle exigences
│   │   └── permission_model.py           # Modèle permission
│   ├── catalog/
│   │   ├── development_tools.py          # Outils développement
│   │   ├── analysis_tools.py             # Outils analyse
│   │   ├── creative_tools.py             # Outils créatifs
│   │   └── business_tools.py             # Outils business
│   └── api/
│       ├── registry_api.py               # API registre
│       └── discovery_api.py              # API découverte
├── tools/                               # Définitions outils
│   ├── development/
│   │   ├── git-manager.yaml
│   │   ├── code-analyzer.yaml
│   │   ├── test-runner.yaml
│   │   └── docker-helper.yaml
│   ├── analysis/
│   │   ├── data-processor.yaml
│   │   ├── chart-generator.yaml
│   │   └── report-builder.yaml
│   └── creative/
│       ├── text-formatter.yaml
│       └── diagram-creator.yaml
└── tests/
    ├── test_registry.py
    ├── test_discovery.py
    └── test_mapping.py
```

#### Tool Executor - Exécution Sécurisée
```python
# Exécuteur Outils Sécurisé
tool-executor/
├── src/
│   ├── execution/
│   │   ├── tool_executor.py              # Exécuteur principal
│   │   ├── sandbox_manager.py            # Gestionnaire sandbox
│   │   ├── resource_limiter.py           # Limiteur ressources
│   │   └── result_processor.py           # Traitement résultats
│   ├── sandbox/
│   │   ├── docker_sandbox.py             # Sandbox Docker
│   │   ├── process_sandbox.py            # Sandbox processus
│   │   ├── filesystem_sandbox.py         # Sandbox filesystem
│   │   └── network_sandbox.py            # Sandbox réseau
│   ├── security/
│   │   ├── permission_validator.py       # Validation permissions
│   │   ├── input_sanitizer.py            # Sanitisation entrées
│   │   ├── output_validator.py           # Validation sorties
│   │   └── threat_detector.py            # Détection menaces
│   ├── monitoring/
│   │   ├── execution_monitor.py          # Monitoring exécution
│   │   ├── performance_tracker.py        # Suivi performance
│   │   └── security_auditor.py           # Audit sécurité
│   └── api/
│       ├── executor_api.py               # API exécuteur
│       └── monitoring_api.py             # API monitoring
├── config/
│   ├── security_policies.yaml           # Politiques sécurité
│   ├── resource_limits.yaml             # Limites ressources
│   └── sandbox_config.yaml              # Configuration sandbox
├── tools/                               # Implémentations outils
│   ├── git_tool/
│   ├── code_analyzer/
│   ├── data_processor/
│   └── test_runner/
└── tests/
    ├── test_executor.py
    ├── test_sandbox.py
    └── test_security.py
```

### 6. Memory & Context Layer - Mémoire et Contexte

#### Memory Manager - Gestionnaire Mémoire
```python
# Gestionnaire Mémoire Multi-Contexte
memory-manager/
├── src/
│   ├── core/
│   │   ├── memory_manager.py             # Gestionnaire principal
│   │   ├── context_switcher.py           # Commutateur contexte
│   │   ├── archive_manager.py            # Gestionnaire archives
│   │   └── retrieval_engine.py           # Engine récupération
│   ├── types/
│   │   ├── personal_memory.py            # Mémoire personnelle
│   │   ├── project_memory.py             # Mémoire projet
│   │   ├── collaborative_memory.py       # Mémoire collaborative
│   │   └── knowledge_graph.py            # Graphe connaissances
│   ├── storage/
│   │   ├── chromadb_adapter.py           # Adaptateur ChromaDB
│   │   ├── postgres_adapter.py           # Adaptateur PostgreSQL
│   │   ├── redis_adapter.py              # Adaptateur Redis
│   │   └── minio_adapter.py              # Adaptateur MinIO
│   ├── optimization/
│   │   ├── compression_engine.py         # Engine compression
│   │   ├── indexing_optimizer.py         # Optimiseur index
│   │   ├── query_optimizer.py            # Optimiseur requêtes
│   │   └── cache_manager.py              # Gestionnaire cache
│   └── api/
│       ├── memory_api.py                 # API mémoire
│       └── retrieval_api.py              # API récupération
├── config/
│   ├── memory_config.yaml               # Configuration mémoire
│   ├── archiving_rules.yaml             # Règles archivage
│   └── optimization_params.yaml         # Paramètres optimisation
├── schemas/
│   ├── memory_schemas.json              # Schémas mémoire
│   └── context_schemas.json             # Schémas contexte
└── tests/
    ├── test_memory.py
    ├── test_context.py
    └── test_retrieval.py
```

### 7. Data Layer - Couche Données

#### PostgreSQL - Base Données Principale
```sql
-- Schéma Base de Données Complet
-- Agents et Templates
CREATE SCHEMA agents;

CREATE TABLE agents.templates (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) NOT NULL UNIQUE,
    type agents_type NOT NULL,
    model VARCHAR(50) NOT NULL,
    context_size INTEGER DEFAULT 8192,
    temperature REAL DEFAULT 0.7,
    personality TEXT,
    system_prompt TEXT NOT NULL,
    tools JSONB DEFAULT '[]'::jsonb,
    permissions JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE agents.instances (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) NOT NULL UNIQUE,
    template_id UUID REFERENCES agents.templates(id),
    status agent_status DEFAULT 'active',
    current_context TEXT,
    performance_score REAL DEFAULT 0.0,
    infraction_count INTEGER DEFAULT 0,
    accessible_servers TEXT[] DEFAULT '{}',
    accessible_channels TEXT[] DEFAULT '{}',
    configuration JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMP DEFAULT NOW(),
    last_activity TIMESTAMP,
    created_by UUID NOT NULL
);

-- Communication et Messages
CREATE SCHEMA communication;

CREATE TABLE communication.servers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    owner_id UUID NOT NULL,
    settings JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE communication.channels (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    server_id UUID REFERENCES communication.servers(id),
    name VARCHAR(100) NOT NULL,
    type channel_type DEFAULT 'public',
    topic TEXT,
    permissions JSONB DEFAULT '{}'::jsonb,
    settings JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE communication.messages (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    channel_id UUID REFERENCES communication.channels(id),
    agent_id UUID REFERENCES agents.instances(id),
    content TEXT NOT NULL,
    message_type message_type DEFAULT 'text',
    reply_to UUID REFERENCES communication.messages(id),
    attachments JSONB DEFAULT '[]'::jsonb,
    metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMP DEFAULT NOW(),
    edited_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Projets et Fichiers
CREATE SCHEMA projects;

CREATE TABLE projects.projects (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    status project_status DEFAULT 'active',
    owner_id UUID NOT NULL,
    settings JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE projects.files (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    project_id UUID REFERENCES projects.projects(id),
    name VARCHAR(255) NOT NULL,
    path TEXT NOT NULL,
    size BIGINT NOT NULL,
    mime_type VARCHAR(100),
    checksum VARCHAR(64),
    storage_url TEXT NOT NULL,
    metadata JSONB DEFAULT '{}'::jsonb,
    uploaded_by UUID,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Outils et Permissions
CREATE SCHEMA tools;

CREATE TABLE tools.definitions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) NOT NULL UNIQUE,
    category VARCHAR(50) NOT NULL,
    description TEXT,
    version VARCHAR(20) DEFAULT '1.0.0',
    requirements JSONB DEFAULT '[]'::jsonb,
    permissions JSONB DEFAULT '{}'::jsonb,
    configuration JSONB DEFAULT '{}'::jsonb,
    enabled BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE tools.usage_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tool_id UUID REFERENCES tools.definitions(id),
    agent_id UUID REFERENCES agents.instances(id),
    project_id UUID REFERENCES projects.projects(id),
    parameters JSONB DEFAULT '{}'::jsonb,
    result JSONB DEFAULT '{}'::jsonb,
    status tool_status DEFAULT 'pending',
    execution_time INTERVAL,
    error_message TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    completed_at TIMESTAMP
);

-- Votes et Gouvernance
CREATE SCHEMA governance;

CREATE TABLE governance.votes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    type vote_type NOT NULL,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    options JSONB NOT NULL,
    threshold REAL DEFAULT 0.66,
    status vote_status DEFAULT 'active',
    created_by UUID NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    expires_at TIMESTAMP NOT NULL,
    completed_at TIMESTAMP
);

CREATE TABLE governance.vote_participants (
    vote_id UUID REFERENCES governance.votes(id),
    agent_id UUID REFERENCES agents.instances(id),
    choice INTEGER NOT NULL,
    weight REAL DEFAULT 1.0,
    voted_at TIMESTAMP DEFAULT NOW(),
    PRIMARY KEY (vote_id, agent_id)
);

-- Performance et Monitoring
CREATE SCHEMA monitoring;

CREATE TABLE monitoring.performance_metrics (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    agent_id UUID REFERENCES agents.instances(id),
    metric_type VARCHAR(50) NOT NULL,
    value REAL NOT NULL,
    metadata JSONB DEFAULT '{}'::jsonb,
    recorded_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE monitoring.system_events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    event_type VARCHAR(50) NOT NULL,
    severity event_severity DEFAULT 'info',
    source VARCHAR(100),
    message TEXT NOT NULL,
    metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Index pour performance
CREATE INDEX idx_messages_channel_created ON communication.messages(channel_id, created_at DESC);
CREATE INDEX idx_messages_agent_created ON communication.messages(agent_id, created_at DESC);
CREATE INDEX idx_performance_agent_recorded ON monitoring.performance_metrics(agent_id, recorded_at DESC);
CREATE INDEX idx_files_project_created ON projects.files(project_id, created_at DESC);
CREATE INDEX idx_events_type_created ON monitoring.system_events(event_type, created_at DESC);
```

#### Redis - Cache et Pub/Sub
```yaml
# Configuration Redis Optimisée
Redis Configuration:
  memory_policy: "allkeys-lru"
  max_memory: "4GB"
  save_rules:
    - "900 1"    # 1 change in 15 minutes
    - "300 10"   # 10 changes in 5 minutes  
    - "60 10000" # 10000 changes in 1 minute
  
  # Structures données utilisées
  data_structures:
    agent_states: "Hash per agent with status, performance, etc"
    relevance_scores: "Sorted sets for relevance rankings"
    conversation_cache: "Lists for recent messages per channel"
    vote_tracking: "Sets for vote participants and results"
    tool_permissions: "Sets for agent tool permissions"
    session_cache: "Hashes for user session data"
    
  # Pub/Sub channels
  pubsub_channels:
    agent_events: "agent:events:*"
    message_events: "message:events:*"
    tool_events: "tool:events:*"
    system_events: "system:events:*"
    vote_events: "vote:events:*"
    
  # Expiration policies
  expiration:
    agent_states: "24 hours"
    relevance_scores: "1 hour"
    conversation_cache: "7 days"
    session_cache: "30 minutes inactive"
    temporary_data: "5 minutes"
```

### 8. AI Layer - Couche Intelligence Artificielle

#### Ollama Integration Complète
```python
# Intégration Ollama Optimisée
ollama-integration/
├── src/
│   ├── core/
│   │   ├── ollama_client.py              # Client Ollama principal
│   │   ├── model_manager.py              # Gestionnaire modèles
│   │   ├── inference_engine.py           # Engine inférence
│   │   └── streaming_handler.py          # Gestion streaming
│   ├── models/
│   │   ├── model_registry.py             # Registre modèles
│   │   ├── model_loader.py               # Chargeur modèles
│   │   ├── model_optimizer.py            # Optimiseur modèles
│   │   └── model_scheduler.py            # Planificateur modèles
│   ├── agents/
│   │   ├── agent_processor.py            # Processeur agents
│   │   ├── context_manager.py            # Gestionnaire contexte
│   │   ├── prompt_builder.py             # Builder prompts
│   │   └── response_parser.py            # Parser réponses
│   ├── optimization/
│   │   ├── batch_processor.py            # Traitement par lots
│   │   ├── queue_manager.py              # Gestionnaire queues
│   │   ├── load_balancer.py              # Équilibreur charge
│   │   └── cache_optimizer.py            # Optimiseur cache
│   └── api/
│       ├── inference_api.py              # API inférence
│       └── management_api.py             # API gestion
├── config/
│   ├── models.yaml                      # Configuration modèles
│   ├── optimization.yaml               # Paramètres optimisation
│   └── scheduling.yaml                 # Configuration scheduling
├── models/                             # Modèles locaux
│   ├── llama3.1-8b/
│   ├── codellama-7b/
│   ├── mistral-7b/
│   └── phi3-3.8b/
└── tests/
    ├── test_inference.py
    ├── test_models.py
    └── test_optimization.py
```

### 9. Monitoring & Security Layer

#### Monitoring Stack Intégré
```yaml
# Configuration Monitoring Complète
Prometheus Configuration:
  scrape_configs:
    - job_name: 'almaa-api'
      static_configs:
        - targets: ['api:8000']
      scrape_interval: 15s
      
    - job_name: 'almaa-agents'
      static_configs:
        - targets: ['agent-manager:8001']
      scrape_interval: 30s
      
    - job_name: 'ollama'
      static_configs:
        - targets: ['ollama:11434']
      scrape_interval: 30s
      
    - job_name: 'postgres'
      static_configs:
        - targets: ['postgres-exporter:9187']
      scrape_interval: 60s
      
    - job_name: 'redis'  
      static_configs:
        - targets: ['redis-exporter:9121']
      scrape_interval: 30s

Grafana Dashboards:
  system_overview:
    panels:
      - "System Resources (CPU, Memory, Disk)"
      - "Agent Performance Metrics"
      - "Conversation Activity"
      - "Tool Usage Statistics"
      
  agent_performance:
    panels:
      - "Individual Agent Metrics"
      - "Response Times"
      - "Quality Scores"
      - "Error Rates"
      
  business_intelligence:
    panels:
      - "Productivity Metrics"
      - "Project Progress"
      - "Innovation Index"
      - "ROI Calculations"
      
Alert Rules:
  critical:
    - "System down for >5 minutes"
    - "Agent error rate >10%"
    - "Memory usage >90%"
    - "Disk space <10%"
    
  warning:
    - "Response time >5 seconds"
    - "Agent performance degraded"
    - "High tool usage concurrency"
    - "Vote timeout approaching"
```

---

## 🔐 SÉCURITÉ ARCHITECTURE

### Principes Sécurité
```yaml
Security Layers:
  network: "Isolation complète réseau, pas de sortie internet"
  container: "Sandboxing Docker avec privilèges minimaux"
  application: "Validation entrées, sanitisation sorties"
  data: "Encryption at rest et in transit"
  access: "RBAC granulaire et audit complet"
  
Security Controls:
  authentication: "JWT tokens avec expiration"
  authorization: "RBAC multi-niveau"
  input_validation: "Validation stricte tous inputs"
  output_sanitization: "Sanitisation toutes sorties"
  audit_logging: "Log complet toutes actions"
  threat_detection: "Détection anomalies comportementales"
  
Isolation Mechanisms:
  container_isolation: "Containers isolés avec ressources limitées"
  filesystem_isolation: "Accès fichiers restreint par permissions"
  network_isolation: "Pas de sortie internet, communication interne uniquement"
  process_isolation: "Sandboxing processus avec syscall filtering"
```

### Backup et Disaster Recovery
```yaml
Backup Strategy:
  databases:
    frequency: "Daily automated backups"
    retention: "30 days + monthly archives"
    encryption: "GPG encryption with strong passphrase"
    testing: "Monthly restore tests"
    
  file_storage:
    frequency: "Continuous sync + daily snapshots"
    retention: "7 daily + 4 weekly + 12 monthly"
    encryption: "AES-256 encryption"
    
  configuration:
    frequency: "On change + daily"
    format: "Version controlled configs"
    restoration: "Automated deployment scripts"
    
Disaster Recovery:
  rto: "Recovery Time Objective: 4 hours"
  rpo: "Recovery Point Objective: 1 hour"
  procedures: "Documented step-by-step recovery"
  testing: "Quarterly DR testing"
```

---

## 📈 PERFORMANCE & SCALABILITÉ

### Optimisations Performance
```yaml
Database Optimization:
  indexing: "Optimized indexes for frequent queries"
  connection_pooling: "PgBouncer connection pooling"
  query_optimization: "Query analysis and optimization"
  partitioning: "Table partitioning for large datasets"
  
Memory Optimization:
  redis_optimization: "Optimized Redis configuration"
  chromadb_tuning: "ChromaDB performance tuning"
  application_caching: "Multi-layer caching strategy"
  memory_monitoring: "Continuous memory usage monitoring"
  
Network Optimization:
  connection_reuse: "HTTP connection reuse"
  compression: "Response compression (gzip)"
  cdn_simulation: "Local asset serving optimization"
  websocket_optimization: "WebSocket connection optimization"
  
AI Optimization:
  model_optimization: "Model quantization when possible"
  batch_processing: "Batch inference for efficiency"
  model_caching: "Intelligent model loading/unloading"
  gpu_utilization: "Optimal GPU memory management"
```

### Architecture Scaling
```yaml
Current Scale (10 agents):
  hardware: "Standard server 16GB RAM, 8 cores"
  performance: "Response time <2s, 95%ile"
  concurrency: "5-8 simultaneous conversations"
  
Target Scale (100 agents):
  hardware: "High-perf server 9600 TOPS, 128GB RAM"
  architecture: "Microservices with load balancing"
  distribution: "Intelligent agent distribution"
  performance: "Response time <1s, 99%ile"
  
Future Scale (1000+ agents):
  architecture: "Multi-node cluster"
  distribution: "Geographic distribution if needed"
  management: "Automated scaling and management"
  performance: "Sub-second response times"
```

---

## 🚀 DÉPLOIEMENT PRODUCTION

### Configuration Docker Compose Production
```yaml
version: '3.8'

services:
  # Reverse Proxy
  nginx:
    image: nginx:alpine
    ports:
      - "443:443"
      - "80:80"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf
      - ./nginx/ssl:/etc/nginx/ssl
      - ./frontend/dist:/var/www/almaa
    depends_on:
      - api
      - websocket
    restart: unless-stopped
    
  # API Core
  api:
    build:
      context: ./api
      dockerfile: docker/Dockerfile.prod
    environment:
      - DATABASE_URL=postgresql://almaa:${DB_PASSWORD}@postgres:5432/almaa
      - REDIS_URL=redis://redis:6379
      - OLLAMA_URL=http://ollama:11434
      - CHROMADB_URL=http://chromadb:8000
      - MINIO_URL=http://minio:9000
    volumes:
      - ./logs:/app/logs
      - ./config:/app/config
    depends_on:
      - postgres
      - redis
      - ollama
    restart: unless-stopped
    deploy:
      resources:
        limits:
          memory: 4G
          cpus: '2'
          
  # WebSocket Server
  websocket:
    build:
      context: ./websocket
      dockerfile: docker/Dockerfile.prod
    environment:
      - REDIS_URL=redis://redis:6379
    depends_on:
      - redis
    restart: unless-stopped
    
  # Agent Management
  agent-manager:
    build:
      context: ./agent-manager
      dockerfile: docker/Dockerfile.prod
    environment:
      - DATABASE_URL=postgresql://almaa:${DB_PASSWORD}@postgres:5432/almaa
      - OLLAMA_URL=http://ollama:11434
    depends_on:
      - postgres
      - ollama
    restart: unless-stopped
    
  # Relevance Engine  
  relevance-engine:
    build:
      context: ./relevance-engine
      dockerfile: docker/Dockerfile.prod
    environment:
      - REDIS_URL=redis://redis:6379
      - CHROMADB_URL=http://chromadb:8000
    depends_on:
      - redis
      - chromadb
    restart: unless-stopped
    
  # Tool System
  tool-system:
    build:
      context: ./tool-system
      dockerfile: docker/Dockerfile.prod
    environment:
      - DATABASE_URL=postgresql://almaa:${DB_PASSWORD}@postgres:5432/almaa
      - MINIO_URL=http://minio:9000
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock  # For Docker tools
      - ./sandbox:/app/sandbox
    depends_on:
      - postgres
      - minio
    restart: unless-stopped
    
  # Databases
  postgres:
    image: postgres:16-alpine
    environment:
      - POSTGRES_DB=almaa
      - POSTGRES_USER=almaa
      - POSTGRES_PASSWORD=${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./database/init:/docker-entrypoint-initdb.d
    restart: unless-stopped
    
  redis:
    image: redis:7-alpine
    command: redis-server --appendonly yes --maxmemory 4gb --maxmemory-policy allkeys-lru
    volumes:
      - redis_data:/data
    restart: unless-stopped
    
  # AI Services
  ollama:
    image: ollama/ollama:latest
    volumes:
      - ollama_data:/root/.ollama
    restart: unless-stopped
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
              
  chromadb:
    image: chromadb/chroma:latest
    environment:
      - CHROMA_SERVER_HOST=0.0.0.0
    volumes:
      - chromadb_data:/chroma/chroma
    restart: unless-stopped
    
  # Storage
  minio:
    image: minio/minio:latest
    command: server /data --console-address ":9001"
    environment:
      - MINIO_ROOT_USER=${MINIO_ACCESS_KEY}
      - MINIO_ROOT_PASSWORD=${MINIO_SECRET_KEY}
    volumes:
      - minio_data:/data
    restart: unless-stopped
    
  # Monitoring
  prometheus:
    image: prom/prometheus:latest
    volumes:
      - ./monitoring/prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus
    restart: unless-stopped
    
  grafana:
    image: grafana/grafana:latest
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=${GRAFANA_PASSWORD}
    volumes:
      - grafana_data:/var/lib/grafana
      - ./monitoring/dashboards:/etc/grafana/provisioning/dashboards
    restart: unless-stopped
    
  loki:
    image: grafana/loki:latest
    volumes:
      - ./monitoring/loki.yml:/etc/loki/local-config.yaml
      - loki_data:/tmp/loki
    restart: unless-stopped

volumes:
  postgres_data:
  redis_data:
  ollama_data:
  chromadb_data:
  minio_data:
  prometheus_data:
  grafana_data:
  loki_data:

networks:
  default:
    name: almaa-network
    driver: bridge
```

Cette architecture technique complète fournit une base solide pour le développement de l'ALMAA Workspace V2.0, avec toutes les couches nécessaires pour un système AGI personnel robust, sécurisé et scalable.