#Exercice 3.8 - Le juste prix ENCORE amélioré !

import random
import os

os.system('cls')

VALEUR_MIN = 1
VALEUR_MAX_FACILE = 10
VALEUR_MAX_MOYEN = 100
VALEUR_MAX_DIFFICILE = 1000

veut_rejouer = True

while veut_rejouer :
    print("Choisissez votre difficulté : \n1.Facile (" + str(VALEUR_MIN) + "-" + str(VALEUR_MAX_FACILE) + ")\n2.Moyen (" + str(VALEUR_MIN) + "-" + str(VALEUR_MAX_MOYEN) + ")\n3.Difficile (" + str(VALEUR_MIN) + "-" + str(VALEUR_MAX_DIFFICILE) + ")")
    choix_difficulte = int(input())
    if choix_difficulte == 1 :
        juste_prix = random.randint(VALEUR_MIN, VALEUR_MAX_FACILE)
    elif choix_difficulte == 2 :
        juste_prix = random.randint(VALEUR_MIN, VALEUR_MAX_MOYEN)
    elif choix_difficulte == 3 :
        juste_prix = random.randint(VALEUR_MIN, VALEUR_MAX_DIFFICILE)
    else :
        print("La valeur n'est pas dans les choix proposés. Veuillez réessayer...")
    
    if choix_difficulte >= 1 or choix_difficulte <= 3 :
        print("Proposez un prix : ")
        proposition = int(input())
        while juste_prix != proposition :
            if juste_prix < proposition :
                print("C'est moins !")
            elif juste_prix > proposition :
                print("C'est plus !")
            print("Proposez un prix : ")
            proposition = int(input())
        print("C'est gagné !")

    print("Voulez-vous rejouer ?")
    veut_rejouer = (input() == "oui")
    os.system('cls')