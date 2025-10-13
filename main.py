import logging
import sys
from random import choice
from grille import Grille
from utils import positions_possibles
from bateau import PorteAvion, SousMarin, Torpilleur, Croiseur

# Configuration de l'encodage pour les émojis
sys.stdout.reconfigure(encoding='utf-8')

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

#SETUP
grille = Grille(8,10)
logging.debug("Grille 8x10 crée")

DISPOSITION = [
    (PorteAvion, 4),
    (Croiseur, 3),
    (Torpilleur, 2),
    (SousMarin, 2),
]

#Placements bateaux
flotte = []
for classe, taille in DISPOSITION:

    candidats = positions_possibles(taille, grille)

    if not candidats:
        raise RuntimeError(f"Impossible de placer {classe.__name__}")

    l, c, vertical = choice(candidats)
    bat = classe(l, c, vertical=vertical)

    grille.ajoute(bat)
    flotte.append(bat)

logging.debug(f"Bateaux disposés : {grille.occupe}")


#Boucle principale
coups = 0
print("----------------------Bataille Navale v1.0-------------------------------")

while not all(bateau.coule(grille) for bateau in flotte):
    print(f"---------------------- Tour numéro {coups+1}----------------------\n")
    grille.affiche_visible(flotte)
    print("Ou voulez-vous tirer ?")

    ligne_tir = int(input("Ligne : "))
    colonne_tir = int(input("Colonne : "))

    coules_avant = {bateau for bateau in flotte if bateau.coule(grille)}

    if (ligne_tir, colonne_tir) in grille.occupe :
        grille.tirer(ligne_tir, colonne_tir, "💣")
    else :
        grille.tirer(ligne_tir, colonne_tir)

    coules_apres = {bateau for bateau in flotte if bateau.coule(grille)}
    nouveaux_coules = coules_apres - coules_avant

    for bateau in nouveaux_coules:
        print(f"\n🎯 Le {bateau.__class__.__name__} a été coulé !\n")

    coups += 1

print(f"Victoire ! vous avez gagné après {coups} coups")
