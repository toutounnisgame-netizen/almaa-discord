/**
 * Configuration Next.js export statique.
 * Le site est exporté dans le dossier `out/` et servi par Nginx.
 */
const nextConfig = {
  reactStrictMode: true,
  images: {
    unoptimized: true,
  },
  output: 'export'
};

module.exports = nextConfig;
