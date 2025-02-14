#Exercice 3.2 - Lanceur de balles de tennis avec boucles

stock_balles = 15

while stock_balles != 0 :
    print("Le joueur est-il prêt ?")
    pret = (input() == "oui")

    if pret :
        print("lancerBalles()" + str(stock_balles - 1))
        stock_balles -= 1