import React, { useEffect, useState, useMemo } from 'react';
import useWebSocket from '../../hooks/useWebSocket';
import useAgents from '../../hooks/useAgents';
import {
  BarChart, Bar, XAxis, YAxis, Tooltip,
  ResponsiveContainer, CartesianGrid, Legend,
  LineChart, Line
} from 'recharts';
import { Cpu, Server, Activity } from 'lucide-react';

export default function AdminPage() {
  const { messages } = useWebSocket();
  const agents = useAgents(messages);

  // Préparation des données pour le graphe d'activité
  const agentData = useMemo(() =>
    agents.map((a) => ({ name: a.name, count: a.messagesCount })), [agents]
  );
  const formatTime = (ts?: string) => {
    if (!ts) return '-';
    const d = new Date(ts);
    return isNaN(d.getTime()) ? '-' : d.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  };

  // Génération de métriques systèmes simulées (20 derniers points)
  interface MetricPoint { time: string; cpu: number; ram: number; latency: number; }
  const [metrics, setMetrics] = useState<MetricPoint[]>([]);
  useEffect(() => {
    const interval = setInterval(() => {
      const now = new Date();
      const time = now.toLocaleTimeString([], { minute: '2-digit', second: '2-digit' });
      setMetrics((prev) => {
        const pts = [...prev, {
          time,
          cpu: Math.floor(20 + Math.random() * 60),
          ram: Math.floor(20 + Math.random() * 60),
          latency: Math.floor(10 + Math.random() * 40)
        }];
        return pts.slice(-20);
      });
    }, 3000);
    return () => clearInterval(interval);
  }, []);
  const latest = metrics[metrics.length - 1];

  return (
    <div className="h-full overflow-y-auto p-4 space-y-8">
      {/* Panel d’activité des agents */}
      <section className="bg-darker rounded border border-dark p-4 shadow-md">
        <h3 className="text-lg font-semibold mb-4">Activité des agents</h3>
        <div className="flex flex-col lg:flex-row gap-8">
          <div className="flex-1 min-w-0">
            {agentData.length > 0 ? (
              <ResponsiveContainer width="100%" height={250}>
                <BarChart data={agentData} margin={{ top: 10, right: 10, bottom: 20, left: 10 }}>
                  <CartesianGrid strokeDasharray="3 3" stroke="#3a3d45" />
                  <XAxis dataKey="name" stroke="#bbb" tick={{ fill: '#bbb', fontSize: 12 }} />
                  <YAxis stroke="#bbb" tick={{ fill: '#bbb', fontSize: 12 }} allowDecimals={false} />
                  <Tooltip
                    contentStyle={{ backgroundColor: '#2f3136', border: '1px solid #36393f', color: '#fff' }}
                    itemStyle={{ color: '#fff' }}
                  />
                  <Bar dataKey="count" fill="#5865f2" radius={[4, 4, 0, 0]} />
                </BarChart>
              </ResponsiveContainer>
            ) : <p className="text-sm text-gray-400">Aucune donnée disponible.</p>}
          </div>
          <div className="overflow-x-auto lg:w-1/3">
            <table className="min-w-full text-sm">
              <thead>
                <tr className="border-b border-dark">
                  <th className="text-left pb-2">Agent</th>
                  <th className="text-left pb-2">Messages</th>
                  <th className="text-left pb-2">Dernière activité</th>
                </tr>
              </thead>
              <tbody>
                {agents.map((agent) => (
                  <tr key={agent.name} className="border-b border-dark hover:bg-dark/40">
                    <td className="py-1 pr-4">{agent.name}</td>
                    <td className="py-1 pr-4">{agent.messagesCount}</td>
                    <td className="py-1">{formatTime(agent.lastActive)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </section>

      {/* Panel des métriques système simulées */}
      <section className="bg-darker rounded border border-dark p-4 shadow-md">
        <h3 className="text-lg font-semibold mb-4">Métriques système</h3>
        <ResponsiveContainer width="100%" height={250}>
          <LineChart data={metrics} margin={{ top: 10, right: 10, bottom: 20, left: 10 }}>
            <CartesianGrid strokeDasharray="3 3" stroke="#3a3d45" />
            <XAxis dataKey="time" stroke="#bbb" tick={{ fill: '#bbb', fontSize: 12 }} />
            <YAxis stroke="#bbb" tick={{ fill: '#bbb', fontSize: 12 }} domain={[0, 100]} />
            <Tooltip contentStyle={{ backgroundColor: '#2f3136', border: '1px solid #36393f', color: '#fff' }} itemStyle={{ color: '#fff' }} />
            <Legend wrapperStyle={{ color: '#fff' }} />
            <Line type="monotone" dataKey="cpu" stroke="#5865f2" dot={false} name="CPU (%)" />
            <Line type="monotone" dataKey="ram" stroke="#43b581" dot={false} name="RAM (%)" />
            <Line type="monotone" dataKey="latency" stroke="#f04747" dot={false} name="Latence (ms)" />
          </LineChart>
        </ResponsiveContainer>
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 mt-4">
          <div className="flex items-center bg-dark rounded p-3 space-x-3">
            <Cpu className="text-primary" size={24} />
            <div>
              <div className="text-xs text-gray-400">CPU</div>
              <div className="text-lg font-semibold">{latest ? `${latest.cpu}%` : '--'}</div>
            </div>
          </div>
          <div className="flex items-center bg-dark rounded p-3 space-x-3">
            <Server className="text-success" size={24} />
            <div>
              <div className="text-xs text-gray-400">RAM</div>
              <div className="text-lg font-semibold">{latest ? `${latest.ram}%` : '--'}</div>
            </div>
          </div>
          <div className="flex items-center bg-dark rounded p-3 space-x-3">
            <Activity className="text-danger" size={24} />
            <div>
              <div className="text-xs text-gray-400">Latence</div>
              <div className="text-lg font-semibold">{latest ? `${latest.latency} ms` : '--'}</div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
