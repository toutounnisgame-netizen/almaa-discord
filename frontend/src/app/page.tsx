'use client';

import React, { useState } from 'react';
import useWebSocket from '../hooks/useWebSocket';
import useAgents from '../hooks/useAgents';
import AgentsList from '../components/chat/AgentsList';
import MessageList from '../components/chat/MessageList';
import { SendHorizonal } from 'lucide-react';

/**
 * Cette page rend l’interface principale du chat. Elle comporte :
 * – une barre latérale listant les agents actifs,
 * – une zone de conversation à défilement automatique,
 * – un champ de saisie pour envoyer des prompts.
 */
export default function Page() {
  const { messages, status } = useWebSocket();
  const agents = useAgents(messages);
  const [sending, setSending] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleSend(prompt: string) {
    if (!prompt.trim()) return;
    setError(null);
    setSending(true);
    try {
      const response = await fetch('/api/prompt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt }),
      });
      if (!response.ok) throw new Error(`Erreur ${response.status}`);
    } catch (err) {
      setError("Impossible d'envoyer le message. Vérifiez la connexion.");
    } finally {
      setSending(false);
    }
  }

  /** Champ de saisie local. Valide sur Entrée (sans Maj). */
  function MessageInput({ disabled }: { disabled: boolean }) {
    const [value, setValue] = useState('');
    function onSubmit(e: React.FormEvent) {
      e.preventDefault();
      if (!disabled && value.trim()) {
        handleSend(value.trim());
        setValue('');
      }
    }
    function onKeyDown(e: React.KeyboardEvent<HTMLTextAreaElement>) {
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        onSubmit(e as any);
      }
    }
    return (
      <form onSubmit={onSubmit} className="flex items-center border-t border-darker px-4 py-2 bg-dark" autoComplete="off">
        <textarea
          className="flex-1 resize-none bg-darker text-white placeholder-gray-500 text-sm p-2 rounded focus:outline-none focus:ring-1 focus:ring-primary disabled:opacity-50"
          rows={1}
          placeholder="Envoyer un prompt…"
          value={value}
          onChange={(e) => setValue(e.target.value)}
          onKeyDown={onKeyDown}
          disabled={disabled}
        />
        <button
          type="submit"
          disabled={disabled || !value.trim()}
          className="ml-3 p-2 rounded bg-primary hover:bg-primary/80 disabled:opacity-50"
          title="Envoyer"
        >
          <SendHorizonal size={18} className="text-white" />
        </button>
      </form>
    );
  }

  return (
    <div className="flex h-full">
      <AgentsList agents={agents} />
      <div className="flex-1 flex flex-col overflow-hidden">
        <div className="flex-1 overflow-y-auto">
          <MessageList messages={messages} />
        </div>
        {/* Indicateurs de statut et d’envoi */}
        <div className="px-4 py-1 text-xs text-gray-400 flex items-center gap-2">
          {status === 'connecting' && <span>Connexion…</span>}
          {status === 'open' && <span className="text-success">Connecté</span>}
          {(status === 'closed' || status === 'error') && <span className="text-danger">Déconnecté</span>}
          {sending && <span>Envoi…</span>}
          {error && <span className="text-danger">{error}</span>}
        </div>
        <MessageInput disabled={sending || status !== 'open'} />
      </div>
    </div>
  );
}

