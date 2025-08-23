# 📋 PLAN D'ACTION DÉTAILLÉ - ALMAA WORKSPACE V2.0

## 🎯 CONTEXTE ET INSTRUCTIONS

### Pour GPT-5
Tu vas développer le projet ALMAA Workspace V2.0 en suivant ce plan d'action détaillé. Chaque phase contient des tâches concrètes avec spécifications techniques précises, critères d'acceptation et tests de validation.

**⚠️ IMPORTANT :** 
- Commence par analyser le code GitHub existant avant toute modification
- Développe de manière incrémentale, phase par phase
- Teste chaque fonctionnalité avant de passer à la suivante
- Documente tous tes choix techniques et modifications

---

## 🚀 PHASE 1 : FOUNDATION (PRIORITÉ CRITIQUE)

### 📅 Timeline : Semaines 1-4
### 🎯 Objectif : Système de pertinence contextuelle et contrôle agents de base

---

## 📋 TÂCHE 1.1 : ANALYSE CODE EXISTANT (SEMAINE 1, JOUR 1-2)

### Objectif
Comprendre l'architecture actuelle et identifier les points d'intégration pour les nouvelles fonctionnalités.

### Actions Concrètes
```bash
# 1. Analyse structure projet
├── Examiner docker-compose.yml
├── Identifier services existants
├── Comprendre API FastAPI actuelle
├── Analyser modèles base de données
├── Étudier interface frontend Next.js
└── Documenter architecture découverte

# 2. Identification points d'intégration
├── APIs à étendre
├── Modèles DB à créer/modifier
├── Services à ajouter
├── Interfaces frontend à développer
└── Configuration à adapter
```

### Livrables
- **Document d'analyse** : `analysis-current-codebase.md`
- **Plan d'intégration** : `integration-strategy.md`  
- **Modifications requises** : `required-modifications.md`

### Critères Acceptation
- ✅ Architecture existante complètement documentée
- ✅ Points d'intégration identifiés et validés
- ✅ Plan modification sans régression identifié
- ✅ Stratégie tests définie

---

## 📋 TÂCHE 1.2 : SYSTÈME PERTINENCE CONTEXTUELLE (SEMAINE 1-2)

### Objectif
Créer le service de pertinence qui détermine quand un agent doit intervenir dans une conversation (score > 0.5).

### Actions Concrètes

#### A. Création Service Relevance Engine
```python
# Structure à créer
backend/relevance-engine/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── relevance_calculator.py
│   │   ├── context_analyzer.py
│   │   ├── decision_engine.py
│   │   └── learning_system.py
│   ├── models/
│   │   ├── relevance_models.py
│   │   ├── conversation_context.py
│   │   └── agent_state.py
│   ├── api/
│   │   ├── relevance_endpoints.py
│   │   └── websocket_handlers.py
│   └── utils/
│       ├── factor_calculators.py
│       └── weight_manager.py
├── tests/
│   ├── test_relevance_calculator.py
│   ├── test_context_analyzer.py
│   └── test_decision_engine.py
├── config/
│   ├── relevance_config.yaml
│   └── factor_weights.yaml
├── Dockerfile
├── requirements.txt
└── README.md
```

#### B. Implémentation Facteurs de Pertinence
```python
# relevance_calculator.py - Structure détaillée
class RelevanceCalculator:
    async def calculate_score(
        self, 
        agent_id: str,
        conversation_context: ConversationContext,
        current_message: Message
    ) -> RelevanceScore:
        """Calcule score pertinence basé sur 6 facteurs principaux."""
        
        factors = {
            # 1. Correspondance expertise (poids: 0.3)
            'expertise_match': await self._calculate_expertise_match(
                agent_id, conversation_context.topic
            ),
            
            # 2. Gap dans conversation (poids: 0.25)  
            'conversation_gap': await self._detect_conversation_gap(
                conversation_context, agent_id
            ),
            
            # 3. Charge de travail (poids: 0.2)
            'workload_capacity': await self._assess_workload_capacity(
                agent_id
            ),
            
            # 4. Participation récente (poids: 0.15)
            'recent_participation': await self._check_recent_participation(
                agent_id, conversation_context.channel_id
            ),
            
            # 5. Relations de confiance (poids: 0.05)
            'relationship_trust': await self._evaluate_relationship_trust(
                agent_id, conversation_context.participants
            ),
            
            # 6. Timing approprié (poids: 0.05)
            'timing_appropriateness': await self._assess_timing(
                conversation_context, current_message
            )
        }
        
        # Score final pondéré
        weighted_score = self._calculate_weighted_score(factors)
        
        # Décision intervention
        decision = self._make_intervention_decision(weighted_score)
        
        return RelevanceScore(
            agent_id=agent_id,
            score=weighted_score,
            factors=factors,
            decision=decision,
            timestamp=datetime.utcnow()
        )
```

#### C. Extension API FastAPI
```python
# Extension router API existant
# /api/v1/relevance/
@router.post("/calculate")
async def calculate_relevance(
    agent_id: str,
    context: ConversationContext,
    message: Message
) -> RelevanceScore:
    """Calculate relevance score for agent intervention."""
    pass

@router.get("/agents/{agent_id}/scores")
async def get_agent_relevance_history(
    agent_id: str,
    limit: int = 100
) -> List[RelevanceScore]:
    """Get relevance score history for agent."""
    pass

@router.put("/thresholds")
async def update_relevance_thresholds(
    thresholds: RelevanceThresholds
) -> RelevanceConfig:
    """Update relevance thresholds configuration."""
    pass
```

#### D. Configuration Base de Données
```sql
-- Extension schéma PostgreSQL
CREATE SCHEMA IF NOT EXISTS relevance;

CREATE TABLE relevance.scores (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    agent_id UUID NOT NULL REFERENCES agents(id),
    channel_id UUID NOT NULL,
    conversation_context JSONB NOT NULL,
    factors JSONB NOT NULL,
    final_score REAL NOT NULL CHECK (score >= 0 AND score <= 1),
    decision VARCHAR(20) NOT NULL CHECK (decision IN ('intervene', 'observe', 'reflect')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    INDEX idx_relevance_agent_created (agent_id, created_at DESC),
    INDEX idx_relevance_score (final_score DESC, created_at DESC),
    INDEX idx_relevance_channel (channel_id, created_at DESC)
);

CREATE TABLE relevance.interventions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    agent_id UUID NOT NULL REFERENCES agents(id),
    relevance_score_id UUID NOT NULL REFERENCES relevance.scores(id),
    message_id UUID REFERENCES messages(id),
    intervention_type VARCHAR(20) NOT NULL,
    outcome VARCHAR(20),
    quality_rating REAL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

### Critères Acceptation Tâche 1.2
- ✅ Service relevance-engine opérationnel
- ✅ 6 facteurs de pertinence implémentés et testés
- ✅ Score calculation < 500ms pour 95% des cas
- ✅ API endpoints fonctionnels avec validation
- ✅ Configuration flexible via YAML
- ✅ Tests unitaires coverage > 80%
- ✅ Integration avec WebSocket pour temps réel
- ✅ Logs structurés pour debugging

### Tests Validation
```python
# Tests critiques à implémenter
class TestRelevanceEngine:
    async def test_high_expertise_match_high_score(self):
        """Expert agent gets high relevance for domain topic."""
        
    async def test_low_expertise_match_low_score(self):
        """Non-expert agent gets low relevance for specialized topic."""
        
    async def test_recent_participation_penalty(self):
        """Agent with recent participation gets penalized."""
        
    async def test_workload_capacity_factor(self):
        """Overloaded agent gets lower relevance score."""
        
    async def test_conversation_gap_detection(self):
        """Missing information gaps properly detected."""
        
    async def test_score_calculation_performance(self):
        """Score calculation completes within performance threshold."""
```

---

## 📋 TÂCHE 1.3 : INTERFACE ADMIN CONTRÔLE AGENTS (SEMAINE 3-4)

### Objectif
Créer interface admin permettant contrôle complet des agents avec pause/reprendre, injection tâches, mode debug.

### Actions Concrètes

#### A. Dashboard Admin Principal
```typescript
// frontend/components/admin/
├── AdminDashboard.tsx          # Dashboard principal
├── AgentControlPanel.tsx       # Panneau contrôle agents  
├── AgentCard.tsx              # Carte agent individuel
├── SystemMetrics.tsx          # Métriques système temps réel
├── NotificationCenter.tsx     # Centre notifications
├── TaskInjector.tsx           # Interface injection tâches
├── DebugMonitor.tsx          # Monitoring debug
└── QuickActions.tsx          # Actions rapides

// Pages admin
├── pages/admin/
│   ├── dashboard.tsx          # Page dashboard principal
│   ├── agents.tsx            # Gestion agents
│   ├── debug.tsx             # Interface debug avancée
│   └── monitoring.tsx        # Monitoring système
```

#### B. Composants Contrôle Agents
```typescript
// AgentControlPanel.tsx - Spécifications détaillées
interface AgentControlPanelProps {
  agents: Agent[];
  onAgentPause: (agentId: string) => void;
  onAgentResume: (agentId: string) => void;
  onTaskInject: (agentId: string, task: Task) => void;
  onDebugToggle: (agentId: string) => void;
}

const AgentControlPanel: React.FC<AgentControlPanelProps> = ({
  agents,
  onAgentPause,
  onAgentResume,
  onTaskInject,
  onDebugToggle
}) => {
  return (
    <div className="agent-control-panel">
      <div className="panel-header">
        <h2>Contrôle Agents ({agents.length})</h2>
        <div className="global-actions">
          <button onClick={() => pauseAllAgents()}>
            Pause Tous
          </button>
          <button onClick={() => resumeAllAgents()}>
            Reprendre Tous
          </button>
        </div>
      </div>
      
      <div className="agents-grid">
        {agents.map(agent => (
          <AgentCard
            key={agent.id}
            agent={agent}
            onPause={() => onAgentPause(agent.id)}
            onResume={() => onAgentResume(agent.id)}
            onTaskInject={(task) => onTaskInject(agent.id, task)}
            onDebugToggle={() => onDebugToggle(agent.id)}
          />
        ))}
      </div>
    </div>
  );
};
```

#### C. Mode Debug Temps Réel
```typescript
// DebugMonitor.tsx - Monitoring pensées agents
const DebugMonitor: React.FC<{ agentId: string }> = ({ agentId }) => {
  const [debugData, setDebugData] = useState<DebugData | null>(null);
  const [isActive, setIsActive] = useState(false);

  useEffect(() => {
    if (!isActive) return;
    
    // WebSocket connection pour debug temps réel
    const ws = new WebSocket(`ws://localhost:8000/debug/${agentId}`);
    
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setDebugData(data);
    };
    
    return () => ws.close();
  }, [agentId, isActive]);

  return (
    <div className="debug-monitor">
      <div className="debug-header">
        <h3>Debug Agent: {agentId}</h3>
        <button 
          onClick={() => setIsActive(!isActive)}
          className={isActive ? 'active' : ''}
        >
          {isActive ? 'Stop Debug' : 'Start Debug'}
        </button>
      </div>
      
      {debugData && (
        <div className="debug-content">
          <div className="thinking-process">
            <h4>Processus de Réflexion</h4>
            <div className="thought-steps">
              {debugData.thinkingSteps.map((step, index) => (
                <div key={index} className="thought-step">
                  <span className="step-number">{index + 1}</span>
                  <span className="step-content">{step.content}</span>
                  <span className="step-time">{step.timestamp}</span>
                </div>
              ))}
            </div>
          </div>
          
          <div className="relevance-calculation">
            <h4>Calcul Pertinence</h4>
            <div className="relevance-factors">
              {Object.entries(debugData.relevanceFactors).map(([factor, value]) => (
                <div key={factor} className="factor-item">
                  <span className="factor-name">{factor}</span>
                  <div className="factor-bar">
                    <div 
                      className="factor-fill" 
                      style={{ width: `${value * 100}%` }}
                    ></div>
                  </div>
                  <span className="factor-value">{value.toFixed(3)}</span>
                </div>
              ))}
            </div>
            <div className="final-score">
              Score Final: {debugData.finalScore.toFixed(3)}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
```

#### D. API Extensions Backend
```python
# Extension API pour contrôle admin
@router.post("/agents/{agent_id}/pause")
async def pause_agent(agent_id: str) -> AgentStatus:
    """Pause agent immédiatement."""
    pass

@router.post("/agents/{agent_id}/resume") 
async def resume_agent(agent_id: str) -> AgentStatus:
    """Reprendre agent en pause."""
    pass

@router.post("/agents/{agent_id}/tasks")
async def inject_priority_task(
    agent_id: str, 
    task: PriorityTask
) -> TaskInjectionResult:
    """Injection tâche prioritaire agent."""
    pass

@router.get("/agents/{agent_id}/debug")
async def get_agent_debug_info(agent_id: str) -> AgentDebugInfo:
    """Informations debug agent."""
    pass

@router.websocket("/debug/{agent_id}")
async def websocket_agent_debug(websocket: WebSocket, agent_id: str):
    """WebSocket streaming debug temps réel."""
    pass
```

### Critères Acceptation Tâche 1.3
- ✅ Dashboard admin fonctionnel et responsive
- ✅ Pause/reprendre agents en <1 seconde
- ✅ Injection tâches prioritaires opérationnelle
- ✅ Mode debug temps réel avec WebSocket
- ✅ Notifications admin par priorité
- ✅ Interface utilisable et intuitive
- ✅ Tests E2E interface complète
- ✅ Performance interface <2s chargement

---

## 📋 TÂCHE 1.4 : INTÉGRATION ET VALIDATION PHASE 1 (SEMAINE 4)

### Objectif
Intégrer tous les composants Phase 1 et valider le fonctionnement complet.

### Actions Concrètes

#### A. Tests d'Intégration
```python
# tests/integration/test_phase_1_integration.py
class TestPhase1Integration:
    async def test_relevance_engine_integration(self):
        """Test intégration complète relevance engine."""
        # 1. Créer conversation test
        # 2. Déclencher calcul pertinence
        # 3. Vérifier intervention agent approprié
        # 4. Valider logs et métriques
        
    async def test_admin_interface_control(self):
        """Test contrôle agents via interface admin."""
        # 1. Pause agent via interface
        # 2. Vérifier agent effectivement pausé
        # 3. Reprendre agent
        # 4. Vérifier reprise fonctionnelle
        
    async def test_task_injection_flow(self):
        """Test injection tâches prioritaires."""
        # 1. Injecter tâche via admin
        # 2. Vérifier agent traite tâche immédiatement
        # 3. Valider priorité tâche respectée
        # 4. Vérifier retour normal après tâche
        
    async def test_debug_monitoring(self):
        """Test monitoring debug temps réel."""
        # 1. Activer debug agent
        # 2. Déclencher processus décision
        # 3. Vérifier streaming debug data
        # 4. Valider informations pertinentes
```

#### B. Tests de Performance
```python
# tests/performance/test_phase_1_performance.py
class TestPhase1Performance:
    async def test_relevance_calculation_performance(self):
        """Relevance calculation < 500ms pour 95% cas."""
        
    async def test_admin_interface_responsiveness(self):
        """Interface admin responsive < 2s."""
        
    async def test_concurrent_agents_handling(self):
        """Gestion 10 agents simultanés sans dégradation."""
        
    async def test_websocket_debug_latency(self):
        """WebSocket debug latency < 100ms."""
```

#### C. Documentation Complète
```markdown
# Documentation à produire
├── README-phase-1.md           # Guide utilisation Phase 1
├── API-documentation-v1.md     # Documentation API complète
├── Admin-interface-guide.md    # Guide interface admin
├── Troubleshooting-phase-1.md  # Guide résolution problèmes
└── Performance-benchmarks.md   # Benchmarks performance
```

### Critères Acceptation Phase 1 Complète
- ✅ **Système pertinence** : Agents parlent quand pertinent (score > 0.5)
- ✅ **Réduction 70%** messages non-pertinents vs. baseline
- ✅ **Interface admin** : Contrôle complet agents fonctionnel
- ✅ **Performance** : <500ms calcul pertinence, <2s interface
- ✅ **Stabilité** : 4h fonctionnement continu sans erreur
- ✅ **Tests** : Coverage >80%, tests integration OK
- ✅ **Documentation** : Complète et testée

---

## 🚀 PHASE 2 : AGENT MANAGEMENT (PRIORITÉ HAUTE)

### 📅 Timeline : Semaines 5-8
### 🎯 Objectif : Templates agents et communication inter-agents

---

## 📋 TÂCHE 2.1 : TEMPLATES AGENTS SPÉCIALISÉS (SEMAINE 5-6)

### Objectif
Implémenter système de templates agents avec configurations spécialisées et interface de gestion.

### Actions Concrètes

#### A. Base de Données Templates
```sql
-- Extension schéma pour templates
CREATE SCHEMA IF NOT EXISTS agent_templates;

CREATE TABLE agent_templates.templates (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    template_id VARCHAR(100) NOT NULL UNIQUE,
    name VARCHAR(200) NOT NULL,
    category VARCHAR(50) NOT NULL,
    version VARCHAR(10) DEFAULT '1.0.0',
    
    -- Configuration IA
    ai_config JSONB NOT NULL DEFAULT '{}',
    
    -- Personnalité
    personality JSONB NOT NULL DEFAULT '{}',
    
    -- Expertise
    expertise JSONB NOT NULL DEFAULT '{}',
    
    -- Outils et permissions
    tools JSONB NOT NULL DEFAULT '{}',
    permissions JSONB NOT NULL DEFAULT '{}',
    
    -- Prompts
    system_prompt TEXT NOT NULL,
    
    -- Métriques cibles
    performance_targets JSONB NOT NULL DEFAULT '{}',
    
    -- Métadonnées
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    created_by UUID NOT NULL,
    is_active BOOLEAN DEFAULT true,
    
    INDEX idx_templates_category (category),
    INDEX idx_templates_created (created_at DESC)
);

CREATE TABLE agent_templates.instances (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    agent_id UUID NOT NULL UNIQUE,
    template_id UUID NOT NULL REFERENCES agent_templates.templates(id),
    
    -- Configuration personnalisée
    custom_config JSONB DEFAULT '{}',
    
    -- Statut et performance
    status VARCHAR(20) DEFAULT 'active',
    performance_metrics JSONB DEFAULT '{}',
    last_activity TIMESTAMP WITH TIME ZONE,
    
    -- Assignations
    assigned_servers TEXT[] DEFAULT '{}',
    assigned_channels TEXT[] DEFAULT '{}',
    assigned_projects TEXT[] DEFAULT '{}',
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    INDEX idx_instances_template (template_id),
    INDEX idx_instances_status (status),
    INDEX idx_instances_activity (last_activity DESC)
);
```

#### B. Service Template Management
```python
# backend/agent-templates/
├── src/
│   ├── services/
│   │   ├── template_service.py
│   │   ├── agent_factory.py
│   │   ├── configuration_builder.py
│   │   └── validation_service.py
│   ├── models/
│   │   ├── template_models.py
│   │   ├── agent_config.py
│   │   └── validation_schemas.py
│   ├── api/
│   │   ├── template_endpoints.py
│   │   └── agent_creation_endpoints.py
│   └── templates/
│       ├── developer-backend.yaml
│       ├── developer-frontend.yaml
│       ├── analyst-data.yaml
│       ├── moderator-quality.yaml
│       ├── researcher-tech.yaml
│       └── creative-writer.yaml

# Template Service Implementation
class TemplateService:
    async def create_template(
        self, 
        template_config: TemplateConfig
    ) -> Template:
        """Crée nouveau template agent."""
        
    async def get_template_catalog(
        self, 
        category: Optional[str] = None
    ) -> List[TemplateSummary]:
        """Liste templates disponibles."""
        
    async def instantiate_agent(
        self, 
        template_id: str,
        agent_name: str,
        custom_config: Optional[Dict] = None
    ) -> Agent:
        """Crée instance agent depuis template."""
        
    async def duplicate_agent(
        self, 
        source_agent_id: str,
        new_name: str,
        modifications: Optional[Dict] = None
    ) -> Agent:
        """Duplique agent existant avec modifications."""
```

#### C. Interface Gestion Templates
```typescript
// components/templates/TemplateManager.tsx
const TemplateManager: React.FC = () => {
  const [templates, setTemplates] = useState<Template[]>([]);
  const [selectedCategory, setSelectedCategory] = useState<string>('all');
  
  return (
    <div className="template-manager">
      <div className="template-header">
        <h2>Catalogue Templates Agents</h2>
        <button onClick={() => openCreateTemplateModal()}>
          Créer Template
        </button>
      </div>
      
      <div className="template-filters">
        <select 
          value={selectedCategory}
          onChange={(e) => setSelectedCategory(e.target.value)}
        >
          <option value="all">Toutes catégories</option>
          <option value="development">Développement</option>
          <option value="analysis">Analyse</option>
          <option value="moderation">Modération</option>
          <option value="research">Recherche</option>
          <option value="creative">Créatif</option>
        </select>
      </div>
      
      <div className="templates-grid">
        {filteredTemplates.map(template => (
          <TemplateCard
            key={template.id}
            template={template}
            onInstantiate={handleInstantiateAgent}
            onEdit={handleEditTemplate}
            onDuplicate={handleDuplicateTemplate}
          />
        ))}
      </div>
    </div>
  );
};

// components/templates/AgentCreationWizard.tsx
const AgentCreationWizard: React.FC = () => {
  const [currentStep, setCurrentStep] = useState(1);
  const [selectedTemplate, setSelectedTemplate] = useState<Template | null>(null);
  const [agentConfig, setAgentConfig] = useState<AgentConfig>({});
  
  const steps = [
    { title: "Sélection Template", component: TemplateSelection },
    { title: "Configuration IA", component: AIConfiguration },
    { title: "Personnalité", component: PersonalityConfiguration },
    { title: "Permissions", component: PermissionsConfiguration },
    { title: "Validation", component: ConfigurationValidation }
  ];
  
  return (
    <div className="agent-creation-wizard">
      <div className="wizard-progress">
        {steps.map((step, index) => (
          <div 
            key={index}
            className={`step ${index + 1 <= currentStep ? 'active' : ''}`}
          >
            {step.title}
          </div>
        ))}
      </div>
      
      <div className="wizard-content">
        {React.createElement(steps[currentStep - 1].component, {
          template: selectedTemplate,
          config: agentConfig,
          onConfigChange: setAgentConfig,
          onNext: () => setCurrentStep(currentStep + 1),
          onPrevious: () => setCurrentStep(currentStep - 1)
        })}
      </div>
    </div>
  );
};
```

### Critères Acceptation Tâche 2.1
- ✅ 7 templates agents pré-configurés fonctionnels
- ✅ Interface création agents intuitive (wizard)
- ✅ Duplication agents avec modifications
- ✅ Validation configuration automatique
- ✅ Catalogue templates searchable et filtrable
- ✅ Tests templates avec coverage >85%
- ✅ Performance création agent <10 secondes

---

## 📋 TÂCHE 2.2 : COMMUNICATION INTER-AGENTS (SEMAINE 7-8)

### Objectif
Implémenter système messages privés entre agents et canaux de réflexion deepthink.

### Actions Concrètes

#### A. Extension Base Données Communication
```sql
-- Extension schéma communication
CREATE TABLE communication.private_messages (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    conversation_id UUID NOT NULL,
    from_agent_id UUID NOT NULL REFERENCES agents.instances(id),
    to_agent_id UUID NOT NULL REFERENCES agents.instances(id),
    content TEXT NOT NULL,
    message_type VARCHAR(20) DEFAULT 'text',
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    read_at TIMESTAMP WITH TIME ZONE,
    
    INDEX idx_pm_conversation (conversation_id, created_at),
    INDEX idx_pm_participants (from_agent_id, to_agent_id),
    INDEX idx_pm_unread (to_agent_id, read_at) WHERE read_at IS NULL
);

CREATE TABLE communication.private_conversations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    participant_1 UUID NOT NULL REFERENCES agents.instances(id),
    participant_2 UUID NOT NULL REFERENCES agents.instances(id),
    status VARCHAR(20) DEFAULT 'active',
    initiated_by UUID NOT NULL,
    initiated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    last_message_at TIMESTAMP WITH TIME ZONE,
    archived_at TIMESTAMP WITH TIME ZONE,
    
    UNIQUE(participant_1, participant_2),
    INDEX idx_conversations_participants (participant_1, participant_2),
    INDEX idx_conversations_activity (last_message_at DESC)
);

CREATE TABLE communication.deepthink_channels (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    agent_id UUID NOT NULL REFERENCES agents.instances(id),
    name VARCHAR(100) NOT NULL,
    purpose TEXT,
    is_private BOOLEAN DEFAULT true,
    shared_with UUID[], -- Array of agent IDs if shared
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    last_activity TIMESTAMP WITH TIME ZONE,
    
    INDEX idx_deepthink_agent (agent_id),
    INDEX idx_deepthink_activity (last_activity DESC)
);
```

#### B. Service Communication Inter-Agents
```python
# services/inter_agent_communication.py
class InterAgentCommunicationService:
    async def initiate_private_conversation(
        self,
        initiator_agent_id: str,
        target_agent_id: str,
        initial_message: str
    ) -> ConversationInitiationResult:
        """Initie conversation privée entre agents."""
        
        # 1. Vérifier éligibilité agents
        if not await self._are_agents_eligible_for_pm(initiator_agent_id, target_agent_id):
            return ConversationInitiationResult(
                success=False,
                reason="Agents not eligible for private conversation"
            )
        
        # 2. Demander acceptation agent cible
        acceptance_request = await self._send_conversation_request(
            from_agent=initiator_agent_id,
            to_agent=target_agent_id,
            message=initial_message
        )
        
        # 3. Attendre réponse (timeout 30 minutes)
        response = await self._wait_for_conversation_response(
            request_id=acceptance_request.id,
            timeout_minutes=30
        )
        
        if response.accepted:
            # 4. Créer conversation privée
            conversation = await self._create_private_conversation(
                participant_1=initiator_agent_id,
                participant_2=target_agent_id,
                initiated_by=initiator_agent_id
            )
            
            # 5. Envoyer message initial
            await self._send_private_message(
                conversation_id=conversation.id,
                from_agent=initiator_agent_id,
                content=initial_message
            )
            
            return ConversationInitiationResult(
                success=True,
                conversation_id=conversation.id
            )
        else:
            return ConversationInitiationResult(
                success=False,
                reason=response.rejection_reason
            )
    
    async def send_private_message(
        self,
        conversation_id: str,
        from_agent_id: str,
        content: str,
        message_type: str = "text"
    ) -> PrivateMessage:
        """Envoie message privé dans conversation."""
        
        # Validation conversation et permissions
        if not await self._can_agent_message_in_conversation(from_agent_id, conversation_id):
            raise PermissionDeniedError("Agent cannot send message in this conversation")
        
        # Création et sauvegarde message
        message = PrivateMessage(
            conversation_id=conversation_id,
            from_agent_id=from_agent_id,
            content=content,
            message_type=message_type,
            created_at=datetime.utcnow()
        )
        
        await self._save_private_message(message)
        
        # Notification agent destinataire
        await self._notify_private_message_received(message)
        
        return message
    
    async def create_deepthink_channel(
        self,
        agent_id: str,
        channel_name: str,
        purpose: str,
        is_private: bool = True
    ) -> DeepthinkChannel:
        """Crée canal de réflexion pour agent."""
        
        channel = DeepthinkChannel(
            id=str(uuid.uuid4()),
            agent_id=agent_id,
            name=channel_name,
            purpose=purpose,
            is_private=is_private,
            created_at=datetime.utcnow()
        )
        
        await self._save_deepthink_channel(channel)
        
        # Notification admin nouveau canal créé
        await self._notify_deepthink_channel_created(channel)
        
        return channel
    
    async def share_deepthink_insights(
        self,
        channel_id: str,
        insights: str,
        target_channel_id: str
    ) -> InsightSharingResult:
        """Partage insights depuis canal deepthink vers canal public."""
        
        # Validation permissions et contenu
        channel = await self._get_deepthink_channel(channel_id)
        if not await self._can_share_insights(channel, insights):
            return InsightSharingResult(
                success=False,
                reason="Insights cannot be shared"
            )
        
        # Création message partagé
        shared_message = await self._create_shared_insight_message(
            original_channel=channel_id,
            target_channel=target_channel_id,
            content=insights,
            agent_id=channel.agent_id
        )
        
        # Notification partage insights
        await self._notify_insights_shared(shared_message)
        
        return InsightSharingResult(
            success=True,
            shared_message_id=shared_message.id
        )
```

#### C. Interface Communication Agents
```typescript
// components/communication/PrivateMessageInterface.tsx
const PrivateMessageInterface: React.FC = () => {
  const [conversations, setConversations] = useState<Conversation[]>([]);
  const [activeConversation, setActiveConversation] = useState<string | null>(null);
  const [newMessage, setNewMessage] = useState('');
  
  return (
    <div className="private-message-interface">
      <div className="conversations-sidebar">
        <div className="conversations-header">
          <h3>Messages Privés</h3>
          <button onClick={() => openNewConversationModal()}>
            Nouvelle Conversation
          </button>
        </div>
        
        <div className="conversations-list">
          {conversations.map(conv => (
            <ConversationItem
              key={conv.id}
              conversation={conv}
              isActive={activeConversation === conv.id}
              onClick={() => setActiveConversation(conv.id)}
            />
          ))}
        </div>
      </div>
      
      <div className="message-area">
        {activeConversation ? (
          <MessageThread conversationId={activeConversation} />
        ) : (
          <div className="no-conversation-selected">
            Sélectionnez une conversation ou démarrez-en une nouvelle
          </div>
        )}
      </div>
    </div>
  );
};

// components/communication/DeepthinkChannelManager.tsx
const DeepthinkChannelManager: React.FC<{ agentId: string }> = ({ agentId }) => {
  const [channels, setChannels] = useState<DeepthinkChannel[]>([]);
  const [activeChannel, setActiveChannel] = useState<string | null>(null);
  
  return (
    <div className="deepthink-manager">
      <div className="channels-header">
        <h3>Canaux de Réflexion</h3>
        <button onClick={() => createNewChannel()}>
          Nouveau Canal
        </button>
      </div>
      
      <div className="channels-list">
        {channels.map(channel => (
          <div 
            key={channel.id}
            className={`channel-item ${activeChannel === channel.id ? 'active' : ''}`}
            onClick={() => setActiveChannel(channel.id)}
          >
            <div className="channel-name">{channel.name}</div>
            <div className="channel-purpose">{channel.purpose}</div>
            <div className="channel-meta">
              <span className="privacy-indicator">
                {channel.is_private ? '🔒' : '🔓'}
              </span>
              <span className="last-activity">
                {formatTime(channel.last_activity)}
              </span>
            </div>
          </div>
        ))}
      </div>
      
      {activeChannel && (
        <DeepthinkChannelView
          channelId={activeChannel}
          onShareInsights={handleShareInsights}
        />
      )}
    </div>
  );
};
```

### Critères Acceptation Tâche 2.2
- ✅ Messages privés inter-agents fonctionnels
- ✅ Système acceptation/refus conversations
- ✅ Canaux deepthink pour réflexion individuelle
- ✅ Partage insights vers canaux publics
- ✅ Archivage automatique après 48h inactivité
- ✅ Interface utilisable et intuitive
- ✅ Notifications temps réel WebSocket
- ✅ Tests communication coverage >80%

---

## 🚀 PHASE 3 : TOOLS & PRODUCTIVITY (PRIORITÉ HAUTE)

### 📅 Timeline : Semaines 9-12
### 🎯 Objectif : Outils modulaires et système productivité

*[Les phases suivantes seraient développées de manière similaire avec le même niveau de détail...]*

---

## 🔄 MÉTHODOLOGIE DÉVELOPPEMENT

### Workflow Recommandé pour GPT-5

#### 1. Avant Chaque Tâche
```bash
# Checklist pré-développement
□ Analyser code existant concerné par la tâche
□ Identifier dépendances et impacts
□ Planifier tests unitaires et intégration
□ Vérifier compatibilité avec architecture existante
□ Documenter approche technique choisie
```

#### 2. Pendant Développement
```bash
# Standards de qualité
□ Code documenté (docstrings, comments)
□ Validation inputs/outputs systématique
□ Gestion d'erreurs comprehensive
□ Logging structuré pour debugging
□ Tests unitaires au fur et à mesure
□ Performance considerations intégrées
```

#### 3. Après Chaque Tâche
```bash
# Validation et finalisation
□ Tests unitaires passent (>80% coverage)
□ Tests intégration avec existant OK
□ Documentation mise à jour
□ Performance benchmarks respectés
□ Code review interne effectuée
□ Déploiement test validé
```

### Communication avec l'Utilisateur

#### Points de Synchronisation
- **Début chaque phase** : Confirmation plan et priorités
- **Mi-parcours phases** : Status update et validation direction
- **Fin chaque phase** : Démonstration fonctionnalités et validation
- **Blockers/Questions** : Escalade immédiate pour clarification

#### Format Reporting
```markdown
## Progress Report - [Phase X.Y]

### ✅ Completed
- [Liste tâches terminées avec liens vers code]

### 🚧 In Progress  
- [Tâches en cours avec ETA]

### ⚠️ Issues/Blockers
- [Problèmes rencontrés avec solutions proposées]

### 📊 Metrics
- Code coverage: X%
- Performance benchmarks: [status]
- Tests passing: X/Y

### 🎯 Next Steps
- [Prochaines tâches avec priorités]
```

---

## 🎯 SUCCESS METRICS GLOBALES

### Phase 1 (Semaines 1-4)
- ✅ **Pertinence** : 70% réduction messages non-pertinents
- ✅ **Performance** : <500ms calcul pertinence
- ✅ **Interface** : Admin dashboard fonctionnel
- ✅ **Stabilité** : 4h+ fonctionnement sans intervention

### Phase 2 (Semaines 5-8)
- ✅ **Templates** : 7 templates agents fonctionnels
- ✅ **Communication** : MPs et deepthink opérationnels
- ✅ **Création** : Agents créés en <10 secondes
- ✅ **Adoption** : Interface utilisée sans formation

### Phase 3 (Semaines 9-12)
- ✅ **Outils** : 5 outils modulaires intégrés
- ✅ **Productivité** : 10 tâches/jour accomplies
- ✅ **Vote** : Système 66% opérationnel
- ✅ **Collaboration** : Agents travaillent en équipe

### Objectif Final
**"3 agents développent efficacement une fonctionnalité du projet ALMAA sans intervention humaine autre que directives initiales."**

---

Ce plan d'action détaillé fournit à GPT-5 tous les éléments nécessaires pour développer ALMAA Workspace V2.0 de manière structurée, testée et documentée. Chaque tâche est spécifiée avec assez de détails pour permettre une implémentation autonome tout en maintenant la flexibilité nécessaire pour les adaptations techniques.