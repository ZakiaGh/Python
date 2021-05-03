#Le jeu du pendu

from random import choice

fichier = open("liste_mots.txt", "r")
liste_mots = fichier.readlines()
mot = choice(liste_mots)  
mot = mot.rstrip()        
fichier.close()

mot_devine = "-" * len(mot)
print(mot_devine)
essais = 0

while mot_devine != mot:
    lettre = input("Entrez un  '?' pour abandonner : ")
    lettre = lettre[0]  
    if lettre == '?':
        print('Le mot était',mot)
        break    
    lettre = lettre.upper()
    for i in range(len(mot)):
        if lettre == mot[i]:
            mot_devine = mot_devine[:i] + lettre + mot_devine[i+1:]
    print(mot_devine)    
    essais += 1
    
if mot == mot_devine:
    print('Bravo ! Le mot',mot,'a été trouvé en', essais,'coups')





