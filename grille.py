from bateau import Bateau
from utils import chevauchement

class Grille :

    def __init__(self, nombre_lignes : int, nombre_colonnes : int):

        self.vide = "~"
        self.matrice = [self.vide for i in range (nombre_lignes * nombre_colonnes)]
        self.nombre_colonnes = nombre_colonnes
        self.bateaux = []

    def index(self, ligne: int, colonne: int) -> int:
        """Transforme (ligne, colonne) en index dans self.matrice."""
        return ligne * self.nombre_colonnes + colonne


    def tirer(self, ligne : int, colonne : int):
        if 0 <= ligne < len(self.matrice) // self.nombre_colonnes and 0 <= colonne < self.nombre_colonnes:
            self.matrice[self.index(ligne, colonne)] = "x"
        else:
            raise IndexError("Coordonnées hors de la grille")

    def ajoute(self, bateau: Bateau) -> None:
        # vérifier que toutes les positions sont dans la grille

        for (ligne, colonne) in bateau.positions:
            if ligne < 0 or colonne < 0 or colonne >= self.nombre_colonnes:
                raise IndexError("Le bateau ne rentre pas dans la grille")

            if self.index(ligne, colonne) >= len(self.matrice):
                raise IndexError("Le bateau ne rentre pas dans la grille")

        for b in self.bateaux:
            if chevauchement(bateau, b):
                raise IndexError("Chevauchement interdit")

        for (ligne, colonne) in bateau.positions:
            self.matrice[self.index(ligne, colonne)] = getattr(bateau, "marque", "⛵")
        self.bateaux.append(bateau)

    def __str__(self) -> str :
        sortie = ""
        for i in range(len(self.matrice)):

            if i % self.nombre_colonnes == 0 and i != 0:
                sortie += "\n"

            sortie += self.matrice[i]
        return sortie








