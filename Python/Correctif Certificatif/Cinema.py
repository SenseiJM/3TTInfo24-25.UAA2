# Cinema - Évaluation Certificative

montant_total = 0
nb_billets_vendus = 0
print("Combien de billets voulez-vous acheter ?")
nb_billets_a_acheter = int(input())

while nb_billets_a_acheter != nb_billets_vendus :
    print("Quel est l'âge pour ce billet ?")
    age = int(input())

    if age < 12 :
        montant_total = montant_total + 5
    elif age > 18 :
        montant_total = montant_total + 10
    else :
        montant_total = montant_total + 7

    nb_billets_vendus = nb_billets_vendus + 1

if nb_billets_vendus >= 10 :
    montant_total = montant_total * 0,75

print(montant_total)