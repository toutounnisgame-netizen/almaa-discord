-- Migration: Ajout tables de pertinence
CREATE SCHEMA IF NOT EXISTS relevance;
CREATE TABLE IF NOT EXISTS relevance.scores (
id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
agent_id TEXT NOT NULL,
channel_id TEXT NOT NULL,
conversation_context JSONB NOT NULL,
factors JSONB NOT NULL,
score REAL NOT NULL CHECK (score >= 0 AND score <= 1),
decision VARCHAR(20) NOT NULL CHECK (decision IN ('intervene','observe','reflect')),
created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
CREATE INDEX IF NOT EXISTS idx_relevance_agent_created ON relevance.scores (agent_id, cre
CREATE INDEX IF NOT EXISTS idx_relevance_score ON relevance.scores (score DESC, created_a
CREATE INDEX IF NOT EXISTS idx_relevance_channel ON relevance.scores (channel_id, created
CREATE TABLE IF NOT EXISTS relevance.interventions (
id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
agent_id TEXT NOT NULL,
relevance_score_id UUID NOT NULL REFERENCES relevance.scores(id) ON DELETE CASCADE,
message_id UUID,
intervention_type VARCHAR(20) NOT NULL,
outcome VARCHAR(20),
quality_rating REAL,
created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
