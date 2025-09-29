from bateau import Bateau

class Grille :

    def __init__(self, nombre_lignes : int, nombre_colonnes : int):

        self.vide = "~"
        self.matrice = [self.vide for i in range (nombre_lignes * nombre_colonnes)]
        self.nombre_colonnes = nombre_colonnes

    def index(self, ligne: int, colonne: int) -> int:
        """Transforme (ligne, colonne) en index dans self.matrice."""
        return ligne * self.nombre_colonnes + colonne


    def tirer(self, ligne : int, colonne : int):
        if 0 <= ligne < len(self.matrice) // self.nombre_colonnes and 0 <= colonne < self.nombre_colonnes:
            self.matrice[self.index(ligne, colonne)] = "x"
        else:
            raise IndexError("Coordonnées hors de la grille")


    def ajoute(self, bateau : Bateau):
        pos = bateau.positions

        for (ligne,colonne) in pos :
            if ligne <= len(self.matrice)//self.nombre_colonnes and colonne <= self.nombre_colonnes :
                self.matrice[self.in
                             dex(ligne,colonne)] = '⛵'

            else :
                raise IndexError("Le bateau ne rentre pas dans la grille")


    def __str__(self) -> str :
        sortie = ""
        for i in range(len(self.matrice)):

            if i % self.nombre_colonnes == 0 and i != 0:
                sortie += "\n"

            sortie += self.matrice[i]
        return sortie








