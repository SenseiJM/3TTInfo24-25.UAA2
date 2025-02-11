#Exercice 4 - Maximum parmi 3 nombres

nb1 = int(input("Entrez un premier nombre : "))
nb2 = int(input("Entrez un deuxième nombre : "))
nb3 = int(input("Entrez un troisième nombre : "))

if nb1 > nb2 :
    if nb1 > nb3 :
        print(str(nb1) + " est le plus grand.")
    else :
        print(str(nb3) + " est le plus grand.")
elif nb2 > nb3 :
    print(str(nb2) + " est le plus grand.")
else :
    print(str(nb3) + " est le plus grand.")