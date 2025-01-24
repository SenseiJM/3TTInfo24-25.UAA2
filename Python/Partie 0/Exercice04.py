#Exercice04

print("Entrer un nombre pour la première valeur : ")
nombre1 = int(input())
print("Entrer un nombre pour la deuxième valeur : ")
nombre2 = int(input())

nombre1 = nombre1 + nombre2
nombre2 = nombre1 - nombre2
nombre1 = nombre1 - nombre2

print("La première valeur vaut maintenant " + str(nombre1) + " et la seconde vaut " + str(nombre2))
print("La première valeur vaut maintenant", nombre1, "et la seconde vaut", nombre2)