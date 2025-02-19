#Exercice 3.7 - Le juste prix amélioré
import random

juste_prix = random.randint(0, 100)
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