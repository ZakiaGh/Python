#Pierre Papier Ciseaux

from random import choice
 
 
coup = ("Pierre", "Feuille", "Ciseaux")
 
 
while input("Jouez (y/n): ").lower() != "n":
 
    print("\n------------------------------------")
    print("Le jeu du: Pierre - Feuille - Ciseaux")
    print("------------------------------------\n")
 
    a = int(input("Choisissez une lettre :\n0: Pierre\n1: Feuille\n2: Ciseaux\n-> "))
    b = choice(range(3))
 
    print("\n{} VS {}".format(coup[a], coup[b]))
    if a == b:
        print("ÉGALITÉ\n")
    elif (a>b and b+1 == a) or (a<b and a+b == 2):
        print(":D Vous avez gagnez.\n")
    else:
        print(":( Vous avez perdu.\n")
else:
    print("Au revoir.")