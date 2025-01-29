#Exercice05

print("Donnez un nombre en secondes : ")
secondes_lues = int(input())

s = secondes_lues % 60
m = ((secondes_lues - s) // 60) % 60
h = (((secondes_lues - s) // 60) // 60) % 24
j = (((secondes_lues - s) // 60) // 60) // 24

print(secondes_lues, "secondes valent", j, "jour(s)", h, "heure(s)", m, "minute(s)", s, "seconde(s).")

print(str(secondes_lues) + " secondes valent " + str(j) + " jour(s) " + str(h) + " heure(s) " + str(m) + " minute(s) " + str(s) + " seconde(s).")