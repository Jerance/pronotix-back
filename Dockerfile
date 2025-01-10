# Utilise une image Python de base
FROM python:3.12-slim

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie le fichier de dépendances
COPY requirements.txt .

# Crée un environnement virtuel
RUN python -m venv .venv

# Active l'environnement virtuel et installe les dépendances
RUN ./.venv/bin/pip install -r requirements.txt

# Copie le reste de ton application
COPY . .

# Commande par défaut (à adapter selon ton application)
CMD ["python", "app.py"]
