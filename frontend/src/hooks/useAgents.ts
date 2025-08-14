'use client';

import { useMemo } from 'react';
import type { Agent, Message } from '../types';

/**
 * Détermine la liste des agents actifs à partir des messages.
 * Ignore les messages envoyés par "system" ou "user".
 * Calcule le nombre de messages par agent et la dernière activité.
 */
export default function useAgents(messages: Message[]): Agent[] {
  return useMemo(() => {
    const map = new Map<string, Agent>();
    for (const msg of messages) {
      const sender = msg.sender;
      if (sender === 'system' || sender === 'user') continue;
      const existing = map.get(sender);
      if (existing) {
        existing.messagesCount += 1;
        existing.lastActive = msg.timestamp;
      } else {
        map.set(sender, {
          name: sender,
          messagesCount: 1,
          lastActive: msg.timestamp,
        });
      }
    }
    return Array.from(map.values());
  }, [messages]);
}
