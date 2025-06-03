#Démo boucles

import os

os.system('cls')

continuer = True

while continuer :
    print("Hello World !")
    print("Voulez-vous continuer ?")
    continuer = (input() == "oui")

print("Boucle terminée !")