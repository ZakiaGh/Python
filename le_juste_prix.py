#Le juste prix 

import random

n = random.randint(0,100)
commentaire = "?"
while True:
    var = input("Entrez un nombre")
    var = int(var)
    if var < n :
        commentaire = "trop bas"
        print(var, commentaire)

    else :
        commentaire = "trop haut"
        print(var, commentaire)
    if var == n:
        commentaire = "bravo !"
        print(var, commentaire)
        break

