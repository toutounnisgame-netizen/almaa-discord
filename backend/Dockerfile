FROM python:3.11-slim

# Variables d'environnement pour optimisation
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Répertoire de travail
WORKDIR /app

# Copie requirements en premier pour cache Docker
COPY requirements.txt ./

# Installation dépendances Python
# Pour environnement air-gapped, décommentez les lignes suivantes:
# COPY packages/ /packages/
# RUN pip install --no-index --find-links=/packages -r requirements.txt

# Installation standard (commentée en mode offline)
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code application (inclut déjà relevance_engine si présent)
COPY app/ ./app/

# Health check pour monitoring Docker
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8000/api/health')" || exit 1

# Port exposition
EXPOSE 8000

# Commande de démarrage
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
