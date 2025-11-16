class Bateau:

    def __init__(self, ligne : int, colonne : int, longueur=1, vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical

    @property
    def positions(self):
        pos = []
        if self.vertical :
            for i in range(self.longueur):
                pos.append((self.ligne+i, self.colonne))
        else :
            for i in range(self.longueur):
                pos.append((self.ligne, self.colonne+i))

        return pos

    def coule(self, grille) -> bool:

        for (ligne, colonne) in self.positions :
            val = grille.matrice[grille.index(ligne,colonne)]
            if val not in ("x", "💣"):
                return False
        return True

    def set_vertical(self, vertical=False):
        self.vertical = vertical

#Filles

class PorteAvion(Bateau) :
    def __init__(self, ligne : int, colonne : int, vertical=False):
        super().__init__(ligne, colonne, vertical=vertical, longueur=4)
        self.marque = "🚢"

class Croiseur(Bateau) :
    def __init__(self, ligne : int, colonne : int, vertical=False):
        super().__init__(ligne, colonne, vertical=vertical, longueur=3)
        self.marque = "⛴"

class Torpilleur(Bateau) :
    def __init__(self, ligne : int, colonne : int, vertical=False):
        super().__init__(ligne, colonne, vertical=vertical, longueur=2)
        self.marque = "🚣"

class SousMarin(Bateau) :
    def __init__(self, ligne : int, colonne : int, vertical=False):
        super().__init__(ligne, colonne, vertical=vertical, longueur=2)
        self.marque = "🐟"
