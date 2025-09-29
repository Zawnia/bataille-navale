import pytest as pt
from grille import Grille
from bateau import Bateau
import pytest as pt


def test_init():
    g = Grille(2,3)
    assert g.matrice == ["~", "~", "~", "~", "~", "~"]
    assert g.nombre_colonnes == 3

def test_tirer():
    g = Grille(2, 3)
    g.tirer(0,0)
    assert g.matrice[0] == "x"
    assert g.matrice[1] == "~"

def test_ajoute():
    g = Grille(2, 3)
    g.ajoute(Bateau(1, 0, longueur=2, vertical=False))
    assert g.matrice == ["~", "~", "~", "⛵", "⛵", "~"]

    g2 = Grille(2, 3)
    before = g2.matrice.copy()
    with pt.raises(IndexError):
        g2.ajoute(Bateau(1, 3, longueur=1, vertical=False))
    assert g2.matrice == before

    g3 = Grille(2, 3)
    before = g3.matrice.copy()
    with pt.raises(IndexError):
        g3.ajoute(Bateau(2, 0, longueur=1, vertical=True))
    assert g3.matrice == before





