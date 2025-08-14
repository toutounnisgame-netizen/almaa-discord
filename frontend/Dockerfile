## Dockerfile pour le frontend ALMAA
FROM node:18-alpine AS build
WORKDIR /app

# Copier les dépendances et la configuration
COPY package.json package-lock.json* ./
COPY tsconfig.json next.config.js postcss.config.js tailwind.config.js ./

# Copier le code source
COPY src ./src

# Installer les dépendances (mode production)
RUN npm install --omit=dev

# Construire et exporter le site statique
RUN npm run build && npm run export

# Étape finale : exposer uniquement le dossier /out
FROM alpine AS export
WORKDIR /out
COPY --from=build /app/out ./
