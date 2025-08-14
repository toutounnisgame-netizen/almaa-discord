import React from 'react';
import type { Agent } from '../../types';
import { stringToHslColor } from '../../utils/color';

/**
 * Liste les agents actifs dans une barre latérale (240 px).
 * Génère des avatars circulaires colorés (couleur déterminée à partir du nom).
 */
export default function AgentsList({ agents }: { agents: Agent[] }) {
  return (
    <aside className="w-60 bg-dark border-r border-darker p-2 overflow-y-auto">
      <h2 className="text-md font-semibold mb-2">Agents actifs</h2>
      <ul className="space-y-1">
        {agents.map((agent) => {
          const colour = stringToHslColor(agent.name);
          const initial = agent.name.charAt(0).toUpperCase();
          return (
            <li key={agent.name} className="flex items-center gap-3 p-2 rounded hover:bg-darker cursor-default">
              <span
                className="flex items-center justify-center rounded-full text-sm font-bold"
                style={{ backgroundColor: colour, color: '#fff', width: 32, height: 32 }}
              >
                {initial}
              </span>
              <div className="flex-1">
                <div className="text-sm font-medium">{agent.name}</div>
                <div className="text-xs text-gray-400">{agent.messagesCount} messages</div>
              </div>
            </li>
          );
        })}
      </ul>
    </aside>
  );
}
