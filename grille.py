

class Grille :

    def __init__(self, nombre_lignes : int, nombre_colonnes : int):

        self.vide = "~"
        self.matrice = [self.vide for i in range (nombre_lignes * nombre_colonnes)]
        self.nombre_colonnes = nombre_colonnes


    def tirer(self, x : int, y : int):
        if 0 <= x < len(self.matrice) // self.nombre_colonnes and 0 <= y < self.nombre_colonnes:

            index = self.nombre_colonnes * x + y
            self.matrice[index] = "x"

        else:
            raise IndexError("Coordonnées hors de la grille")


    def __str__(self) -> str :
        sortie = ""
        for i in range(len(self.matrice)):

            if i % self.nombre_colonnes == 0 and i != 0:
                sortie += "\n"

            sortie += self.matrice[i]
        return sortie








