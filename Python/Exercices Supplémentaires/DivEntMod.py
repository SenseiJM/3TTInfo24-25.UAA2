#Division Entière, Modulo, Division

print("Veuillez entrer un nombre : ")
nombre_lu = int(input())
print("Veuillez entrer un deuxième nombre : ")
nombre_lu2 = int(input())

if nombre_lu2 == 0 :
    print("Le deuxième nombre ne peut pas être 0")
else :
    print("Voici les résultats pour " + str(nombre_lu) + " et " + str(nombre_lu2) + " :\nDivision Entière : " + str(nombre_lu // nombre_lu2) + "\nModulo : " + str(nombre_lu % nombre_lu2) + "\nDivision : " + str(nombre_lu / nombre_lu2))