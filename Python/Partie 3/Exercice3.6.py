#Exercice 3.6

veut_calculer = True
while veut_calculer :

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

    print("Voulez-vous faire un nouveau calcul ? (1 pour oui, 0 pour non)")
    veut_calculer = bool(int(input()))