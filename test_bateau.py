from bateau import Bateau

def test_init():
    assert Bateau(2, 3).vertical == False
    assert Bateau(2, 3).ligne == 2
    assert Bateau(2, 3, longueur=3).longueur == 3


def test_positions():

    assert Bateau(2, 3, longueur=3).positions == [(2, 3), (2, 4), (2, 5)]
    assert Bateau(2, 3, longueur=3, vertical=True).positions == [(2, 3), (3, 3), (4, 3)]