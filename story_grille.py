from grille import Grille

g = Grille(5,8)
print(g)

print("\n---------------------------------")
ligne = int(input("ligne = "))
colonne = int(input("colonne = "))
print("\n")

g.tirer(ligne,colonne)

print(g)