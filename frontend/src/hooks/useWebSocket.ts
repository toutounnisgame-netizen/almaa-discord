import { useEffect, useRef, useState } from 'react';
import type { Message } from '../types';

export type ConnectionStatus = 'connecting' | 'open' | 'closed' | 'error';

/**
 * Gère la connexion WebSocket au backend (/ws).  Implémente une
 * reconnexion exponentielle et stocke jusqu’à 1000 messages dans
 * localStorage.  Les messages doivent avoir la forme {sender, content, timestamp}.
 */
export default function useWebSocket() {
  const [messages, setMessages] = useState<Message[]>(() => {
    if (typeof window !== 'undefined') {
      const saved = window.localStorage.getItem('almaa_messages');
      if (saved) {
        try {
          return JSON.parse(saved) as Message[];
        } catch {
          return [];
        }
      }
    }
    return [];
  });
  const [status, setStatus] = useState<ConnectionStatus>('connecting');
  const wsRef = useRef<WebSocket | null>(null);
  const reconnectAttempts = useRef(0);
  const reconnectTimeout = useRef<NodeJS.Timeout | null>(null);

  useEffect(() => {
    let cancelled = false;

    function connect() {
      const protocol = window.location.protocol === 'https:' ? 'wss' : 'ws';
      const host = window.location.host;
      const url = `${protocol}://${host}/ws`;
      const ws = new WebSocket(url);
      wsRef.current = ws;
      setStatus('connecting');
      ws.onopen = () => {
        if (cancelled) return;
        setStatus('open');
        reconnectAttempts.current = 0;
      };
      ws.onmessage = (event: MessageEvent) => {
        try {
          const data = JSON.parse(event.data) as Message;
          setMessages((prev) => {
            const list = [...prev, data].slice(-1000);
            if (typeof window !== 'undefined') {
              window.localStorage.setItem('almaa_messages', JSON.stringify(list));
            }
            return list;
          });
        } catch {
          // ignore malformed messages
        }
      };
      ws.onclose = () => {
        if (cancelled) return;
        setStatus('closed');
        scheduleReconnect();
      };
      ws.onerror = () => {
        if (cancelled) return;
        setStatus('error');
        try {
          ws.close();
        } catch {}
      };
    }

    function scheduleReconnect() {
      reconnectAttempts.current += 1;
      const delay = Math.min(10000, 1000 * 2 ** (reconnectAttempts.current - 1));
      reconnectTimeout.current = setTimeout(() => {
        if (!cancelled) connect();
      }, delay);
    }

    connect();
    return () => {
      cancelled = true;
      if (reconnectTimeout.current) clearTimeout(reconnectTimeout.current);
      wsRef.current?.close();
    };
  }, []);

  return { messages, status };
}
