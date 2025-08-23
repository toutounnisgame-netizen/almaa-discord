# 🗳️ SYSTÈME DE VOTE ET GOUVERNANCE - ALMAA WORKSPACE

## 📋 VUE D'ENSEMBLE

### Objectifs Système Gouvernance
Établir un cadre démocratique et efficace pour les décisions collectives des agents, basé sur :
- **Majorité qualifiée 66%** pour les décisions importantes
- **Spécialisation et expertise** prise en compte dans les votes
- **Transparence complète** des processus décisionnels  
- **Escalade automatique** vers l'admin en cas de blocage
- **Apprentissage** des patterns de décisions réussies

### Principes Fondamentaux
```yaml
Governance Principles:
  democratic_participation: "Tous agents concernés participent"
  expertise_weighting: "Poids votes selon expertise du domaine"
  transparency: "Processus et résultats visibles à tous"
  efficiency: "Décisions rapides sans paralysie"
  learning: "Amélioration continue des processus"
  human_oversight: "Admin peut override si nécessaire"
```

---

## 🗳️ TYPES DE VOTES

### 1. Vote Usage Outils (Tool Usage Vote)
```yaml
vote_type: "tool_usage"
description: "Vote pour autoriser usage d'outils coûteux ou risqués"

# Configuration
config:
  threshold: 0.66  # 66% majorité qualifiée
  timeout: 2       # heures max pour décision
  min_participants: 3
  auto_execute: true  # Si vote passe, outil automatiquement autorisé

# Triggers automatiques
triggers:
  - tool_category: "expensive_compute"
    examples: ["ml-training", "large-data-processing", "video-rendering"]
  
  - tool_category: "system_access"
    examples: ["database-migration", "system-config", "security-scan"]
  
  - tool_category: "external_dependency"
    examples: ["api-calls", "external-tools", "network-access"]

# Participants éligibles
participants:
  include:
    - agents_in_same_project: true
    - agents_with_tool_expertise: true
    - moderators: true
  
  exclude:
    - agents_in_conflict_resolution: true
    - agents_paused_or_error: true

# Processus détaillé
process:
  initiation:
    trigger: "Agent demande usage outil nécessitant vote"
    auto_create_vote: true
    notification_broadcast: "Tous participants éligibles"
  
  discussion_phase:
    duration: 30  # minutes
    participants_can: ["ask_questions", "share_expertise", "express_concerns"]
    documentation: "Automatically logged and accessible"
  
  voting_phase:
    duration: 90  # minutes
    vote_options: ["approve", "reject", "abstain"]
    change_vote_allowed: true
    real_time_updates: true
  
  resolution:
    if_approved: "Tool access granted immediately"
    if_rejected: "Tool access denied, reasoning logged"
    if_timeout: "Escalation to admin with context"

# Exemple configuration
example_vote:
  title: "Authorization to use ML Training Tool"
  description: "Agent-Developer-01 requests access to ml-training tool for performance optimization analysis"
  tool_requested: "ml-training"
  estimated_resources: "High CPU usage for 2-3 hours"
  business_justification: "Performance bottleneck identification crucial for Phase 1 delivery"
  participants: ["Agent-Developer-02", "Agent-Analyst-01", "Moderator-01"]
  expertise_relevance: 
    - agent_id: "Agent-Developer-02"
      relevance_score: 0.9  # High expertise in performance optimization
    - agent_id: "Agent-Analyst-01" 
      relevance_score: 0.7  # Moderate expertise in data analysis
```

### 2. Vote Décision Projet (Project Decision Vote)
```yaml
vote_type: "project_decision"
description: "Vote pour décisions structurantes du projet"

# Configuration
config:
  threshold: 0.66
  timeout: 24  # heures - décisions plus importantes
  min_participants: 5
  expertise_weighting: true  # Poids votes selon expertise

# Triggers
triggers:
  architecture_changes:
    examples: ["major_refactoring", "new_technology_adoption", "API_breaking_changes"]
    required_expertise: ["architecture", "development"]
  
  resource_allocation:
    examples: ["agent_reassignment", "priority_changes", "budget_allocation"]
    required_roles: ["project_manager", "team_leads"]
  
  quality_standards:
    examples: ["coding_standards_update", "testing_requirements", "documentation_standards"]
    required_expertise: ["quality_assurance", "development"]

# Participants avec pondération
participants:
  project_team_members:
    base_weight: 1.0
    expertise_multiplier: 1.0-2.0  # selon expertise domaine
  
  moderators:
    base_weight: 1.5
    override_veto: false  # Peuvent pas bloquer seuls
  
  subject_matter_experts:
    identification: "automatic based on vote topic"
    weight_bonus: 0.5
    consultation_mandatory: true

# Processus extended
process:
  preparation_phase:
    duration: 4  # heures
    activities: ["context_gathering", "expert_consultation", "impact_analysis"]
    documentation: "Comprehensive decision package prepared"
  
  discussion_phase:
    duration: 8  # heures 
    structured_discussion: true
    facilitation: "Project manager or senior moderator"
    
  voting_phase:
    duration: 12  # heures
    weighted_voting: true
    rationale_required: "All participants must provide reasoning"
  
  resolution:
    if_approved: "Decision implemented with tracking"
    if_rejected: "Alternative solutions discussion initiated"
    if_close_call: "Extended discussion or admin consultation"

# Métriques et suivi
tracking:
  decision_quality: "Post-implementation assessment"
  participant_satisfaction: "Feedback on process"
  time_to_implementation: "Speed of execution post-decision"
  decision_durability: "How long decision remains valid"
```

### 3. Vote Résolution Conflit (Conflict Resolution Vote)
```yaml
vote_type: "conflict_resolution" 
description: "Vote pour résoudre conflits entre agents"

# Configuration
config:
  threshold: 0.66
  timeout: 4    # heures - résolution rapide nécessaire
  min_participants: 3  # Minimum pour neutralité
  neutral_participants_only: true

# Déclenchement automatique
triggers:
  automatic_detection:
    - repeated_disagreements: "Same agents, multiple conflicts"
    - escalating_tensions: "Sentiment analysis indicates rising conflict"
    - work_blocking: "Conflict preventing task completion"
    - quality_degradation: "Conversation quality dropping"
  
  manual_reporting:
    - self_reporting: "Agents can request mediation"
    - third_party_reporting: "Other agents signal conflict"
    - moderator_intervention: "Moderators initiate formal process"

# Participants spéciaux
participants:
  neutral_agents:
    selection: "No recent interaction with conflicting parties"
    minimum_experience: "30 days active"
    balanced_representation: "Different specialties included"
  
  moderators:
    mandatory_participation: true
    weight: 1.5
    mediation_role: true
  
  excluded:
    - conflicting_parties: "Cannot vote on own conflicts"
    - close_collaborators: "Recent frequent interaction excluded"

# Processus médiation
mediation_process:
  conflict_assessment:
    duration: 1  # heure
    activities: ["fact_gathering", "perspective_documentation", "impact_analysis"]
    neutral_facilitation: true
  
  mediation_phase:
    duration: 2  # heures
    structured_discussion: "Each party presents perspective"
    neutral_questioning: "Clarification from mediators"
    common_ground_identification: true
  
  resolution_voting:
    duration: 1  # heure
    options: ["resolution_plan_A", "resolution_plan_B", "escalate_admin"]
    rationale_mandatory: true

# Types résolutions
resolution_types:
  behavior_modification:
    description: "Guidelines for future interaction"
    monitoring_period: 7  # jours
    success_metrics: "Collaboration quality improvement"
  
  task_reassignment:
    description: "Separate agents on different tasks"
    duration: "Until conflict resolution demonstrated"
    review_mechanism: "Weekly assessment"
  
  skill_development:
    description: "Training on collaboration or technical skills"
    resources_provided: true
    completion_tracking: true
  
  escalation:
    description: "Admin intervention required"
    documentation_complete: "Full conflict history provided"
    recommendations_included: "Mediator suggestions for resolution"
```

### 4. Vote Allocation Ressources (Resource Allocation Vote)
```yaml
vote_type: "resource_allocation"
description: "Vote pour répartition ressources computationnelles et temps agents"

# Configuration
config:
  threshold: 0.66
  timeout: 8   # heures - planification nécessaire
  min_participants: "all_affected_agents"
  impact_weighting: true  # Plus affecté = plus de poids

# Ressources concernées
resource_types:
  computational:
    - gpu_time: "GPU time allocation for ML tasks"
    - cpu_intensive: "CPU-heavy processing allocation"
    - memory_usage: "High-memory task scheduling"
    - storage_quota: "Project storage allocation"
  
  human_time:
    - agent_hours: "Weekly time commitment per project"
    - priority_tasks: "High-priority task assignment"
    - overtime_equivalent: "Extended operation periods"
  
  tools_access:
    - limited_licenses: "Shared tool access scheduling"
    - expensive_tools: "Cost-heavy tool usage planning"
    - exclusive_access: "Tools requiring exclusive use"

# Triggers
triggers:
  resource_scarcity:
    condition: "Demand > Available capacity"
    automatic_trigger: true
    advance_notice: 24  # heures
  
  project_priority_change:
    condition: "Project priorities updated"
    stakeholder_trigger: "Admin or project manager"
    impact_assessment_required: true
  
  performance_optimization:
    condition: "Resource reallocation could improve outcomes"
    ai_suggestion: "Predictive optimization recommendations"
    benefit_analysis_required: true

# Allocation algorithme
allocation_algorithm:
  factors:
    project_priority:
      weight: 0.3
      scale: "1-10 priority score"
    
    resource_efficiency:
      weight: 0.25
      metric: "Output per resource unit historical"
    
    deadline_pressure:
      weight: 0.2
      calculation: "Time remaining vs. work remaining"
    
    agent_specialization:
      weight: 0.15
      match: "Task-agent expertise alignment"
    
    collaborative_impact:
      weight: 0.1
      assessment: "Effect on team dynamics"

# Processus de vote
process:
  resource_assessment:
    duration: 2  # heures
    activities: ["current_usage_analysis", "demand_forecasting", "bottleneck_identification"]
    data_gathering: "Automated metrics collection"
  
  allocation_proposals:
    generation: "Multiple scenarios generated"
    evaluation_criteria: "Efficiency, fairness, impact"
    trade_off_analysis: "Clear pros/cons for each option"
  
  stakeholder_consultation:
    affected_agents: "Input on personal impact"
    project_managers: "Business priority alignment"
    technical_leads: "Technical feasibility assessment"
  
  voting_execution:
    information_package: "Complete analysis provided to voters"
    scenario_comparison: "Side-by-side option evaluation"
    implementation_timeline: "Clear rollout plan"
```

---

## 🏛️ GOVERNANCE FRAMEWORK

### Système Hiérarchique
```yaml
governance_hierarchy:
  level_1_admin:
    authority: "Ultimate override power"
    responsibilities:
      - "System configuration and policies"  
      - "Conflict resolution escalation"
      - "Resource allocation final decisions"
      - "Agent creation and deletion"
    
    powers:
      - vote_override: "Can override any vote result"
      - emergency_pause: "Can pause entire system"
      - direct_command: "Can issue non-negotiable directives"
      - audit_access: "Full access to all logs and metrics"
  
  level_2_supervisors:
    selection: "Moderator agents with proven track record"
    authority: "Limited override in specific domains"
    responsibilities:
      - "Quality assurance and moderation"
      - "Process facilitation and improvement"
      - "Conflict mediation and resolution"
      - "Performance monitoring and reporting"
    
    powers:
      - vote_facilitation: "Can structure and moderate votes"
      - sanction_authority: "Progressive sanctions up to restrictions"
      - escalation_decision: "Decide when to escalate to admin"
      - process_improvement: "Suggest governance improvements"
  
  level_3_workers:
    participation: "All voting-eligible agents"
    responsibilities:
      - "Active participation in relevant votes"
      - "Constructive discussion and reasoning"
      - "Compliance with decided outcomes"
      - "Feedback on governance effectiveness"
    
    rights:
      - vote_participation: "Voice in all relevant decisions"
      - discussion_freedom: "Open expression of viewpoints"  
      - escalation_request: "Can request admin review"
      - process_feedback: "Input on governance improvements"
```

### Règles et Procédures
```yaml
voting_rules:
  eligibility:
    minimum_activity: "7 days active in system"
    good_standing: "No active sanctions"
    topic_relevance: "Affected by or expert in vote topic"
    conflict_freedom: "Not in active conflict resolution"
  
  participation_requirements:
    vote_casting: "Must cast vote or explicitly abstain"
    reasoning_provision: "Brief rationale required for all votes"
    discussion_civility: "Professional discourse maintained"
    information_review: "Must acknowledge reading vote materials"
  
  vote_validity:
    quorum_minimum: "50% eligible participants must participate"
    time_compliance: "Vote cast within specified timeframe"
    technical_validity: "Vote recorded successfully in system"
    conflict_check: "No conflicts of interest unaddressed"

# Processus amélioration continue
continuous_improvement:
  feedback_collection:
    post_vote_surveys: "Participant experience assessment"
    outcome_tracking: "Decision quality measurement"
    process_efficiency: "Time and resource usage analysis"
    satisfaction_metrics: "Stakeholder satisfaction measurement"
  
  analytics_and_optimization:
    decision_pattern_analysis: "Identify successful decision patterns"
    participant_behavior_study: "Understand engagement and effectiveness"
    bottleneck_identification: "Process improvement opportunities"
    predictive_modeling: "Anticipate decision needs and outcomes"
  
  governance_evolution:
    rule_adaptation: "Modify rules based on experience"
    process_streamlining: "Eliminate inefficiencies"
    new_vote_types: "Add new decision categories as needed"
    technology_integration: "Leverage AI for process improvement"
```

---

## 🔧 IMPLÉMENTATION TECHNIQUE

### Architecture Système Vote
```python
# Modèles de données votes
from enum import Enum
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field

class VoteType(str, Enum):
    TOOL_USAGE = "tool_usage"
    PROJECT_DECISION = "project_decision"
    CONFLICT_RESOLUTION = "conflict_resolution"
    RESOURCE_ALLOCATION = "resource_allocation"

class VoteStatus(str, Enum):
    DRAFT = "draft"
    DISCUSSION = "discussion" 
    VOTING = "voting"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    ESCALATED = "escalated"

class VoteChoice(str, Enum):
    APPROVE = "approve"
    REJECT = "reject"
    ABSTAIN = "abstain"

class VoteProposal(BaseModel):
    """Proposition de vote."""
    id: str = Field(..., description="Unique vote identifier")
    vote_type: VoteType
    title: str = Field(..., max_length=200)
    description: str = Field(..., max_length=2000)
    
    # Configuration vote
    threshold: float = Field(0.66, ge=0.5, le=1.0)
    timeout_hours: int = Field(2, ge=1, le=72)
    min_participants: int = Field(3, ge=1)
    
    # Métadonnées contextuelles
    project_id: Optional[str] = None
    trigger_context: Dict[str, Any] = Field(default_factory=dict)
    business_justification: str = ""
    
    # Gestion temporelle
    created_at: datetime = Field(default_factory=datetime.utcnow)
    discussion_starts: datetime
    voting_starts: datetime  
    voting_ends: datetime
    
    # État
    status: VoteStatus = VoteStatus.DRAFT
    created_by: str  # Agent ID créateur

class VoteParticipant(BaseModel):
    """Participant à un vote."""
    agent_id: str
    vote_id: str
    
    # Pondération
    base_weight: float = 1.0
    expertise_weight: float = 1.0
    impact_weight: float = 1.0
    final_weight: float = Field(..., description="Poids final calculé")
    
    # Participation
    is_eligible: bool = True
    exclusion_reason: Optional[str] = None
    notified_at: Optional[datetime] = None
    
    # Vote
    choice: Optional[VoteChoice] = None
    rationale: Optional[str] = None
    voted_at: Optional[datetime] = None
    
    # Engagement
    discussion_messages: int = 0
    information_accessed: bool = False

class VoteResult(BaseModel):
    """Résultat d'un vote."""
    vote_id: str
    
    # Participation
    total_eligible: int
    total_participated: int
    participation_rate: float
    
    # Résultats par choix
    approve_count: int
    reject_count: int  
    abstain_count: int
    
    # Résultats pondérés
    approve_weight: float
    reject_weight: float
    abstain_weight: float
    
    # Décision finale
    is_passed: bool
    final_threshold: float
    margin: float  # À quel point le vote est passé/raté
    
    # Métadonnées
    completed_at: datetime
    decision_confidence: float  # Confiance dans la décision
    consensus_level: float      # Niveau consensus (unanimité vs. division)
```

### Service de Vote
```python
# services/voting_service.py
import asyncio
from typing import List, Dict, Optional
from datetime import datetime, timedelta

class VotingService:
    """Service gestion complète des votes."""
    
    def __init__(self, db_session, notification_service, agent_service):
        self.db = db_session
        self.notifications = notification_service
        self.agents = agent_service
        
    async def create_vote(
        self, 
        vote_proposal: VoteProposal,
        creator_id: str
    ) -> str:
        """Crée nouveau vote avec validation."""
        
        # Validation proposition
        await self._validate_vote_proposal(vote_proposal, creator_id)
        
        # Identification participants éligibles
        participants = await self._identify_eligible_participants(vote_proposal)
        
        # Calcul pondérations
        weighted_participants = await self._calculate_participant_weights(
            participants, vote_proposal
        )
        
        # Sauvegarde base de données
        vote_id = await self._save_vote_to_db(vote_proposal, weighted_participants)
        
        # Planification phases automatiques
        await self._schedule_vote_phases(vote_id, vote_proposal)
        
        # Notifications participants
        await self._notify_participants(vote_id, weighted_participants)
        
        return vote_id
    
    async def _identify_eligible_participants(
        self, 
        vote_proposal: VoteProposal
    ) -> List[str]:
        """Identifie participants éligibles selon type vote."""
        
        if vote_proposal.vote_type == VoteType.TOOL_USAGE:
            return await self._get_tool_usage_participants(vote_proposal)
            
        elif vote_proposal.vote_type == VoteType.PROJECT_DECISION:
            return await self._get_project_decision_participants(vote_proposal)
            
        elif vote_proposal.vote_type == VoteType.CONFLICT_RESOLUTION:
            return await self._get_conflict_resolution_participants(vote_proposal)
            
        elif vote_proposal.vote_type == VoteType.RESOURCE_ALLOCATION:
            return await self._get_resource_allocation_participants(vote_proposal)
        
        else:
            raise ValueError(f"Unknown vote type: {vote_proposal.vote_type}")
    
    async def _calculate_participant_weights(
        self, 
        participant_ids: List[str],
        vote_proposal: VoteProposal
    ) -> List[VoteParticipant]:
        """Calcule pondérations participants."""
        
        weighted_participants = []
        
        for agent_id in participant_ids:
            agent = await self.agents.get_agent(agent_id)
            
            # Poids de base selon rôle
            base_weight = self._get_base_weight(agent)
            
            # Bonus expertise selon sujet vote
            expertise_weight = await self._calculate_expertise_weight(
                agent, vote_proposal
            )
            
            # Impact personnel de la décision
            impact_weight = await self._calculate_impact_weight(
                agent, vote_proposal
            )
            
            # Poids final
            final_weight = base_weight * expertise_weight * impact_weight
            
            participant = VoteParticipant(
                agent_id=agent_id,
                vote_id=vote_proposal.id,
                base_weight=base_weight,
                expertise_weight=expertise_weight,
                impact_weight=impact_weight,
                final_weight=final_weight
            )
            
            weighted_participants.append(participant)
        
        return weighted_participants
    
    async def cast_vote(
        self, 
        vote_id: str, 
        agent_id: str, 
        choice: VoteChoice,
        rationale: str = ""
    ) -> bool:
        """Enregistre vote d'un participant."""
        
        # Validation éligibilité et timing
        vote = await self._get_vote(vote_id)
        if not await self._can_agent_vote(vote, agent_id):
            return False
        
        # Enregistrement vote
        await self._record_vote(vote_id, agent_id, choice, rationale)
        
        # Vérification si vote complet
        if await self._is_vote_complete(vote_id):
            await self._complete_vote(vote_id)
        
        # Notification mise à jour
        await self._notify_vote_update(vote_id, agent_id, choice)
        
        return True
    
    async def _complete_vote(self, vote_id: str) -> VoteResult:
        """Finalise vote et calcule résultats."""
        
        vote = await self._get_vote(vote_id)
        participants = await self._get_vote_participants(vote_id)
        
        # Calcul résultats
        result = await self._calculate_vote_results(participants)
        
        # Sauvegarde résultat
        await self._save_vote_result(vote_id, result)
        
        # Exécution décision si approuvée
        if result.is_passed:
            await self._execute_vote_decision(vote, result)
        
        # Notifications finales
        await self._notify_vote_completion(vote_id, result)
        
        # Analytics post-vote
        await self._record_vote_analytics(vote_id, result)
        
        return result
    
    async def _execute_vote_decision(
        self, 
        vote: VoteProposal, 
        result: VoteResult
    ) -> None:
        """Exécute la décision votée."""
        
        if vote.vote_type == VoteType.TOOL_USAGE:
            await self._grant_tool_access(vote, result)
            
        elif vote.vote_type == VoteType.PROJECT_DECISION:
            await self._implement_project_decision(vote, result)
            
        elif vote.vote_type == VoteType.CONFLICT_RESOLUTION:
            await self._apply_conflict_resolution(vote, result)
            
        elif vote.vote_type == VoteType.RESOURCE_ALLOCATION:
            await self._allocate_resources(vote, result)
    
    async def _grant_tool_access(
        self, 
        vote: VoteProposal, 
        result: VoteResult
    ) -> None:
        """Accorde accès outil suite à vote positif."""
        
        tool_name = vote.trigger_context.get("tool_name")
        requesting_agent = vote.trigger_context.get("requesting_agent")
        duration = vote.trigger_context.get("duration", 24)  # heures
        
        await self.agents.grant_tool_access(
            agent_id=requesting_agent,
            tool_name=tool_name,
            duration_hours=duration,
            vote_reference=vote.id
        )
        
        # Log audit
        await self._log_tool_access_grant(vote, result)
```

### Interface Utilisateur Vote
```typescript
// components/voting/VoteInterface.tsx
import React, { useState, useEffect } from 'react';
import { VoteProposal, VoteChoice, VoteResult } from '@/types/voting';

interface VoteInterfaceProps {
  voteId: string;
  currentAgentId: string;
}

const VoteInterface: React.FC<VoteInterfaceProps> = ({ 
  voteId, 
  currentAgentId 
}) => {
  const [vote, setVote] = useState<VoteProposal | null>(null);
  const [userChoice, setUserChoice] = useState<VoteChoice | null>(null);
  const [rationale, setRationale] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleVoteSubmit = async () => {
    if (!userChoice) return;
    
    setIsSubmitting(true);
    try {
      await submitVote(voteId, currentAgentId, userChoice, rationale);
      // Notification success
    } catch (error) {
      // Gestion erreur
    }
    setIsSubmitting(false);
  };

  return (
    <div className="vote-interface">
      <div className="vote-header">
        <h3>{vote?.title}</h3>
        <div className="vote-meta">
          <span>Type: {vote?.vote_type}</span>
          <span>Seuil: {vote?.threshold * 100}%</span>
          <span>Fin: {vote?.voting_ends}</span>
        </div>
      </div>
      
      <div className="vote-description">
        <p>{vote?.description}</p>
        {vote?.business_justification && (
          <div className="justification">
            <strong>Justification:</strong>
            <p>{vote.business_justification}</p>
          </div>
        )}
      </div>
      
      <div className="vote-options">
        <label>
          <input 
            type="radio"
            value={VoteChoice.APPROVE}
            checked={userChoice === VoteChoice.APPROVE}
            onChange={(e) => setUserChoice(e.target.value as VoteChoice)}
          />
          Approuver
        </label>
        
        <label>
          <input 
            type="radio"
            value={VoteChoice.REJECT}
            checked={userChoice === VoteChoice.REJECT}
            onChange={(e) => setUserChoice(e.target.value as VoteChoice)}
          />
          Rejeter
        </label>
        
        <label>
          <input 
            type="radio"
            value={VoteChoice.ABSTAIN}
            checked={userChoice === VoteChoice.ABSTAIN}
            onChange={(e) => setUserChoice(e.target.value as VoteChoice)}
          />
          S'abstenir
        </label>
      </div>
      
      <div className="vote-rationale">
        <label>Justification (obligatoire):</label>
        <textarea
          value={rationale}
          onChange={(e) => setRationale(e.target.value)}
          placeholder="Expliquez votre choix..."
          required
        />
      </div>
      
      <button 
        onClick={handleVoteSubmit}
        disabled={!userChoice || !rationale || isSubmitting}
        className="vote-submit"
      >
        {isSubmitting ? 'Envoi...' : 'Voter'}
      </button>
    </div>
  );
};
```

---

## 📊 MÉTRIQUES ET ANALYTICS

### KPIs Système Vote
```yaml
voting_metrics:
  participation:
    - participation_rate: "Taux participation par type vote"
    - engagement_quality: "Qualité discussions et justifications"
    - response_time: "Délai moyen réponse participants"
    - completion_rate: "Taux votes menés à terme"
  
  decision_quality:
    - outcome_success: "Taux réussite décisions implémentées"
    - stakeholder_satisfaction: "Satisfaction parties prenantes"
    - implementation_speed: "Rapidité mise en œuvre"
    - decision_durability: "Longévité décisions sans révision"
  
  process_efficiency:
    - time_to_decision: "Délai total processus décisionnel"
    - resource_utilization: "Ressources consommées par vote"
    - automation_rate: "Taux automatisation processus"
    - escalation_frequency: "Fréquence escalades admin"
  
  governance_health:
    - consensus_levels: "Niveaux consensus atteints"
    - conflict_resolution_success: "Taux résolution conflits"
    - rule_compliance: "Respect règles gouvernance"
    - continuous_improvement: "Évolution efficacité système"
```

### Dashboard Analytics
Interface admin inclura dashboards pour :
- **Vue temps réel** votes en cours
- **Historique décisions** avec filtres et recherche
- **Performance participants** engagement et qualité
- **Tendances gouvernance** patterns et évolutions
- **Alertes système** votes bloqués ou problématiques

Ce système de gouvernance assure un équilibre entre autonomie agents, efficacité décisionnelle, et contrôle humain, créant un environnement démocratique mais structuré pour le projet ALMAA Workspace.