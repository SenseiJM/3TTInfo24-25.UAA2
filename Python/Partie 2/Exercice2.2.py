#Exercice 2.2

print("Veuillez entrer une année : ")
annee = int(input())

if (((annee % 400) == 0) or (((annee % 4) == 0) and ((annee % 100) != 0))) :
    print("Votre année " + str(annee) + " est bissextile.")
else :
    print("Votre année " + str(annee) + " n'est pas bissextile.")