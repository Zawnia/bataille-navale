from bateau import Bateau
from grille import Grille

def test_init():
    assert Bateau(2, 3).vertical == False
    assert Bateau(2, 3).ligne == 2
    assert Bateau(2, 3, longueur=3).longueur == 3


def test_positions():
    assert Bateau(2, 3, longueur=3).positions == [(2, 3), (2, 4), (2, 5)]
    assert Bateau(2, 3, longueur=3, vertical=True).positions == [(2, 3), (3, 3), (4, 3)]


def test_coule():
    g = Grille(3, 3)

    b = Bateau(1, 0, longueur=2, vertical=False)
    g.ajoute(b)

    assert not b.coule(g)
    g.tirer(1, 0)
    assert not b.coule(g)
    g.tirer(1, 1)
    assert b.coule(g)