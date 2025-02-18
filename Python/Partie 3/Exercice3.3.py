#Exercice 3.3 - Tables de Multiplication de 1 à 9

m = 1
while m < 10 :
    i = 0
    while i < 11 :
        print(str(i) + "*" + str(m) + "=" + str(i * m))
        i += 1 #ou i = i + 1
    m += 1 #ou m = m + 1