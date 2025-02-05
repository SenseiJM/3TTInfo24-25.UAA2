#Exercice 2.4
#Récupéré par les capteurs du robot
nb_balles = 80

#Vérification du panier
if (nb_balles == 0) :
    est_vide = True
    print("Aucune balle restante...")
else :
    est_vide = False

#Si le panier contient des balles
if (est_vide == False) :
    print("Le joueur est-il prêt ?")
    reponse_pret = input()

    #Vérification : le joueur est-il prêt ?
    if (reponse_pret == "oui") :
        est_pret = True
    else :
        print("Veuillez redémarrer le programme lorsque vous êtes prêt.")
    
    if (est_pret == True) :
        print("LancerBalles()")