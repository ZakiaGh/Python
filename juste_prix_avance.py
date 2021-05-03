# Le juste prix 

from random import randint

nbr_essais_max = 6
nbr_essais = 1
borne_sup = 100
mon_prix = randint(1,borne_sup)
ton_prix = 0

print("J'ai choisi un prix entre 1 et",borne_sup)
print("A vous de le deviner en",nbr_essais_max,"tentatives au maximum !")

while ton_prix != mon_prix and nbr_essais <= nbr_essais_max:
    print("Essai numero : ",nbr_essais)    
    ton_prix = int(input("Votre proposition : "))
    if ton_prix < mon_prix:
        print("Trop petit")
    elif ton_prix > mon_prix:
        print("Trop grand")
    else:
        print("Bravo ! Vous avez trouvé",mon_prix,"en",nbr_essais,"essai(s)")   
    nbr_essais += 1
    
if nbr_essais>nbr_essais_max and ton_prix != mon_prix :
    print("Désolé, vous avez utilisé vos",nbr_essais_max,"essais.")    
    print("J'avais choisi le prix",mon_prix,".")