import '../app/globals.css';
import Link from 'next/link';
import type { Metadata } from 'next';
import React from 'react';

/**
 * Layout racine de l’application.  Définit la barre de navigation,
 * applique le mode sombre et encadre le contenu des pages enfants.
 */
export const metadata: Metadata = {
  title: 'ALMAA Discord‑IA Offline',
  description: 'Interface de chat multi‑agents pour la plateforme IA collaborative offline',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="fr" className="dark">
      <body className="min-h-screen flex flex-col bg-darker text-white">
        <nav className="bg-dark border-b border-darker px-4 py-3 flex items-center justify-between">
          <div className="text-xl font-semibold text-primary">ALMAA IA</div>
          <div className="space-x-4">
            <Link href="/" className="hover:text-primary transition-colors">Chat</Link>
            <Link href="/admin" className="hover:text-primary transition-colors">Admin</Link>
          </div>
        </nav>
        <div className="flex-1 overflow-hidden">
          {children}
        </div>
      </body>
    </html>
  );
}
