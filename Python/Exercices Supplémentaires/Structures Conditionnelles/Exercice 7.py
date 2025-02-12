#Exercice 7

cote1 = int(input("Quelle est la longueur du côté 1 ? "))
cote2 = int(input("Quelle est la longueur du côté 2 ? "))
cote3 = int(input("Quelle est la longueur du côté 3 ? "))

if ((cote1 == cote2) and (cote2 == cote3)) :
    print("Le triangle est équilatéral.")
elif ((cote1 == cote2) or (cote2 == cote3) or (cote3 == cote1)) :
    print("Le triangle est isocèle.")
else :
    print("Le triangle est quelconque/scalène.")