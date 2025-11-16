# Bataille navale

Implémentation du jeu de bataille navale en Python, réalisée dans le cadre d’un projet de fin de I1, dans le cadre lde l'approfondissement MIE.
Le projet propose une version jouable en ligne de commande.

## Prérequis

- Python 3
- (Optionnel : un environnement virtuel pour isoler les dépendances)

## Installation

Cloner le dépôt :

    git clone https://github.com/Zawnia/bataille-navale.git
    cd bataille-navale

Installer les dépendances :

    pip install -r requirement.txt

## Lancer le jeu

Depuis la racine du projet :

    python main.py

Suivez ensuite les instructions affichées dans le terminal.

## Structure du projet

- `main.py` : point d’entrée du programme
- `main_features.py` : fonctionnalités principales du jeu
- `bateau.py` : définition et gestion des bateaux
- `grille.py` : gestion des grilles de jeu
- `utils.py` : fonctions utilitaires
- `test_bateau.py`, `test_grille.py`, `test_utils.py` : tests unitaires
- `story_grille.py`, `story_chevauchement.py` : scénarios/test stories 

## Tests

Vous pouvez exécuter les tests unitaires par exemple avec :

    python -m pytest

Ou lancer directement les fichiers de test avec Python :

    python test_bateau.py
    python test_grille.py
    python test_utils.py



