#Exercice 6

print("Entrer le numéro d'un mois : ")
choix = int(input())

if choix == 2 :
    print("Le mois de février compte 28 jours.")
elif ((choix == 1) or (choix == 3) or (choix == 5) or (choix == 7) or (choix == 8) or (choix == 10) or (choix == 12)) :
    print("Ce mois contient 31 jours.")
elif ((choix == 4) or (choix == 6) or (choix == 9) or (choix == 11)) :
    print("Ce mois contient 30 jours.")
else :
    print("Ce mois n'existe pas.")