#Exercice 2.5

STOCK_MAXIMUM = 20

a_servi_snack = False
stock_balisto = stock_mms = stock_snickers = stock_lion = stock_bounty = stock_bueno = STOCK_MAXIMUM
print("Bienvenue. Veuillez sélectionner votre snack à l'aide du numéro correspondant :\n1.Snickers\n2.M&M's\n3.Lion\n4.Bounty\n5.Kinder Bueno\n6.Balisto")
choix_utilisateur = int(input())

if choix_utilisateur == 1 :
    if stock_snickers == 0 :
        print("Stock épuisé...")
    else :
        print("ServirSnack()")
        stock_snickers = stock_snickers - 1
        a_servi_snack = True
elif choix_utilisateur == 2 :
    if stock_mms == 0 :
        print("Stock épuisé...")
    else :
        print("ServirSnack()")
        stock_mms = stock_mms - 1
        a_servi_snack= True
elif choix_utilisateur == 3 :
    if stock_lion == 0 :
        print("Stock épuisé...")
    else :
        print("ServirSnack()")
        stock_lion = stock_lion - 1
        a_servi_snack = True
elif choix_utilisateur == 4 :
    if stock_bounty == 0 :
        print("Stock épuisé...")
    else :
        print("ServirSnack()")
        stock_bounty = stock_bounty -1
        a_servi_snack = True
elif choix_utilisateur == 5 :
    if stock_bueno == 0 :
        print("Stock épuisé...")
    else :
        print("ServirSnack()")
        stock_bueno = stock_bueno - 1
        a_servi_snack = True
elif choix_utilisateur == 6 :
    if stock_balisto == 0 :
        print("Stock épuisé...")
    else :
        print("ServirSnack()")
        stock_balisto = stock_balisto - 1
        a_servi_snack = True

if a_servi_snack :
    print("Merci pour votre achat, à bientôt !")
else :
    print("Achat impossible, veuillez réessayer...")