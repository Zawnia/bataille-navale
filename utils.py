from bateau import Bateau

def chevauchement(bateau1 : Bateau, bateau2 : Bateau) -> bool:
    chevauch = False
    for pos in bateau1.positions:
        if pos in bateau2.positions :
            chevauch = True
    return chevauch

def positions_possibles(taille_bateau: int, grille):
    li, col = len(grille.matrice)//grille.nombre_colonnes, grille.nombre_colonnes

    occ = set(getattr(grille, "occupe", []))  # ex: {(l,c), ...}
    out = []

    # Horizontal
    for l in range(li):
        for c in range(col - taille_bateau + 1):
            pos = [(l, c + i) for i in range(taille_bateau)]
            if occ.isdisjoint(pos):
                out.append((l, c, False))

    # Vertical
    for l in range(li - taille_bateau + 1):
        for c in range(col):
            pos = [(l + i, c) for i in range(taille_bateau)]
            if occ.isdisjoint(pos):
                out.append((l, c, True))

    return out










