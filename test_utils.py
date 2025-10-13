from grille import Grille
from bateau import Bateau
from utils import positions_possibles

def test_positions_possibles():
    g = Grille(3, 3)
    cand = positions_possibles(2, g)

    assert isinstance(cand, list)
    assert all(len(t) == 3 for t in cand)

    L, C = 3, 3
    assert all(0 <= l < L and 0 <= c < C for (l, c, _) in cand)
    assert len(cand) == 12

    g.ajoute(Bateau(0, 0, longueur=2, vertical=False))
    cand2 = positions_possibles(2, g)

    def couvre(l0, c0, ori, Lb=2):
        return [(l0, c0 + i) for i in range(Lb)] if (ori in ("H", False)) else [(l0 + i, c0) for i in range(Lb)]
    occ = {(0, 0), (0, 1)}
    assert all(set(couvre(l, c, ori)).isdisjoint(occ) for (l, c, ori) in cand2)

    assert len(cand2) == 12 - 4

    g_small = Grille(2, 2)
    cand3 = positions_possibles(3, g_small)
    assert cand3 == []