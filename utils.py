from bateau import Bateau

def chevauchement(bateau1 : Bateau, bateau2 : Bateau) -> bool:
    chevauch = False
    for pos in bateau1.positions:
        if pos in bateau2.positions :
            chevauch = True
    return chevauch