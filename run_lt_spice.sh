#!/bin/bash

# Activer l'environnement virtuel
source venv/bin/activate

# Exécuter le script Python
python ./code/lt-spice.py "$@"

# Désactiver l'environnement virtuel
deactivate