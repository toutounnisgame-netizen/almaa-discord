import React, { useEffect, useRef } from 'react';
import type { Message } from '../../types';
import { stringToHslColor } from '../../utils/color';

/**
 * Affiche l’historique des messages.  Fait défiler automatiquement
 * vers le bas à l’arrivée de nouveaux messages.
 */
export default function MessageList({ messages }: { messages: Message[] }) {
  const endRef = useRef<HTMLDivElement>(null);
  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  return (
    <div className="flex-1 overflow-y-auto p-4 space-y-4" style={{ wordBreak: 'break-word' }}>
      {messages.map((msg, index) => {
        const isSystem = msg.sender === 'system' || msg.sender === 'user';
        const colour = stringToHslColor(msg.sender);
        const initial = msg.sender.charAt(0).toUpperCase();
        const date = new Date(msg.timestamp);
        const timeString = isNaN(date.getTime()) ? '' : date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        return (
          <div key={index} className="flex items-start gap-3">
            {!isSystem && (
              <span
                className="flex items-center justify-center rounded-full text-sm font-bold flex-shrink-0"
                style={{ backgroundColor: colour, color: '#fff', width: 32, height: 32 }}
              >
                {initial}
              </span>
            )}
            <div className="flex-1 min-w-0">
              <div className="flex items-center gap-2">
                <span className={`font-medium ${isSystem ? 'text-gray-400 italic' : ''}`}>{msg.sender}</span>
                {timeString && <span className="text-xs text-gray-500">{timeString}</span>}
              </div>
              <p className="text-sm leading-relaxed">{msg.content}</p>
            </div>
          </div>
        );
      })}
      <div ref={endRef} />
    </div>
  );
}
