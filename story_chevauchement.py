from bateau import Bateau

def chevauchement(bateau1 : Bateau, bateau2 : Bateau) -> bool:
    chevauch = False
    for pos in bateau1.positions:
        if pos in bateau2.positions :
            chevauch = True
    return chevauch


# --- Cas qui SE CHEVAUCHENT ---
b1 = Bateau(2, 3, longueur=3, vertical=False)   # positions: (2,3), (2,4), (2,5)
b2 = Bateau(1, 5, longueur=3, vertical=True)    # positions: (1,5), (2,5), (3,5)

print(chevauchement(b1,b2))

# --- Cas qui NE SE CHEVAUCHENT PAS ---
b3 = Bateau(0, 0, longueur=2, vertical=True)    # (0,0), (1,0)
b4 = Bateau(2, 0, longueur=2, vertical=False)   # (2,0), (2,1)

print(chevauchement(b3,b4))