#Le juste prix 

# import random

# n = random.randint(0,100)
# commentaire = "?"
# while True:
#     var = input("Entrez un nombre")
#     var = int(var)
#     if var < n :
#         commentaire = "trop bas"
#         print(var, commentaire)

#     else :
#         commentaire = "trop haut"
#         print(var, commentaire)
#     if var == n:
#         commentaire = "bravo !"
#         print(var, commentaire)
#         break

# Le juste prix 

from random import randint

nbr_essais_max = 6
essais = 1
borneSup = 100
mon_prix = randint(1,borneSup)
ton_prix = 0

print("J'ai choisi un prix entre 1 et",borneSup)
print("Vous avez",essais_max,"tentatives !")
while ton_prix != mon_prix and nbr_essais <= essais_max:
    print("Essai numero : ",essais)    
    ton_prix = int(input("Votre proposition : "))
    if ton_prix < mon_prix:
        print("Trop petit")
    elif ton_prix > mon_prix:
        print("Trop grand")
    else:
        print("Bravo ! Vous avez trouvé",mon_prix,"en",nbr_essais,"essai(s)")   
    nbr_essais += 1
    
if essais>essais_max and ton_prix != mon_prix :
    print("Désolé, vous avez utilisé vos",essais_max,"essais.")    
    print("J'avais choisi le prix",mon_prix,".")