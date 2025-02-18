#Exercice 3.4 - Le juste prix

print("Veuillez entrer le juste prix :")
juste_prix = int(input())
print("Proposez un prix : ")
proposition = int(input())

while proposition != juste_prix :
    if proposition > juste_prix :
        print("C'est moins !")
        proposition = int(input())
    elif proposition < juste_prix :
        print("C'est plus! ")
        proposition = int(input())

print("Félicitations ! Vous avez trouvé le juste prix !")