#VerifMdp

#Imaginer un login et un mot de passe fictifs en début de code et les stocker dans une variable
login_correct = "login"
mot_de_passe_correct = "pass"

#Demander le login à l’utilisateur
print("Veuillez entrer votre login :")
login_entre = input()

#Tant que le login est incorrect, redemander le login à l’utilisateur en affichant le message « Login incorrect, veuillez réessayer… »
while login_correct != login_entre :
    print("Login incorrect, veuillez réessayer...")
    login_entre = input()

#Si le login entré est correct, demander le mot de passe 
if login_entre == login_correct :
    print("Veuillez entrer votre mot de passe : ")
    mot_de_passe_entre = input()
    nombre_tentatives = 3

    #Tant que le mot de passe n’est pas bon, redemander le mot de passe à l’utilisateur
    while (mot_de_passe_entre != mot_de_passe_correct) and (nombre_tentatives > 0) :
        print("Mot de passe incorrect, veuillez réessayer...")
        mot_de_passe_entre = input()
        nombre_tentatives = nombre_tentatives - 1
    
    #Si l’utilisateur se trompe de mot de passe trois fois, afficher le message « Vous vous êtes trompé trop souvent de mot de passe. Compte verrouillé. »
    if (nombre_tentatives == 0) and (mot_de_passe_entre != mot_de_passe_correct) :
        print("Vous vous êtes trompé trop souvent de mot de passe. Compte verrouillé.")
    #Si le bon mot de passe est entré, afficher le message « Bienvenue ! »
    elif mot_de_passe_correct == mot_de_passe_entre :
        print("Bienvenue !")