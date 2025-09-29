import pytest as pt
from grille import Grille

def test_init():
    g = Grille(2,3)
    assert g.matrice == ["~", "~", "~", "~", "~", "~"]
    assert g.nombre_colonnes == 3

def test_tirer():
    g = Grille(2, 3)
    g.tirer(0,0)
    assert g.matrice[0] == "x"
    assert g.matrice[1] == "~"





