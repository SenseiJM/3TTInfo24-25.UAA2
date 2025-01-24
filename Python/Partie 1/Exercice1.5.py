#Exercice1.5

PRIX_ARTICLE = 40
print("Le prix de l'article est " + str(PRIX_ARTICLE) + " €")
print("Combien d'articles voulez-vous ?")
quantite = int(input())
print("Le prix total de votre commande est de " + str((PRIX_ARTICLE * quantite)) + " €")