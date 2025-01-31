#Exercice 2.3

angle1 = int(input("Veuillez entrer l'amplitude du premier angle : "))
angle2 = int(input("Veuillez entrer l'amplitude du deuxième angle : "))
angle3 = int(input("Veuillez entrer l'amplitude du troisième angle : "))
angle4 = int(input("Veuillez entrer l'amplitude du quatrième angle : "))

cote1 = int(input("Veuillez entrer la longueur du premier côté : "))
cote2 = int(input("Veuillez entrer la longueur du deuxième côté : "))
cote3 = int(input("Veuillez entrer la longueur du troisième côté : "))
cote4 = int(input("Veuillez entrer la longueur du quatrième côté : "))

if (((angle1 == 90) and (angle2 == 90) and (angle3 == 90) and (angle4 == 90)) and ((cote1 == cote2) and (cote3 == cote1) and (cote4 == cote1))) :
    print("La forme que vous décrivez est un carré ! Hourrah !")
else :
    print("La forme que vous décrivez n'est pas un carré ! Snif...")