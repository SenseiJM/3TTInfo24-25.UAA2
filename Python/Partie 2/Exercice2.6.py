#Exercice 2.6

print("Entrer un premier nombre : ")
nb1 = int(input())
print("Entrer un opérateur : ")
operateur = input()
print("Entrer un deuxième nombre : ")
nb2 = int(input())

if operateur == '+' :
    resultat = nb1 + nb2
    aCalcule = True
elif operateur == '-' :
    resultat = nb1 - nb2
    aCalcule = True
elif operateur == '*' :
    resultat = nb1 * nb2
    aCalcule = True
elif operateur == '/' :
    if nb2 == 0 :
        print("La division par 0 n'est pas supportée...")
        aCalcule = False
    else :
        resultat = nb1 / nb2
        aCalcule = True

if aCalcule :
    print(str(nb1) + " " + operateur + " " + str(nb2) + " = " + str(resultat))