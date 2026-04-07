reponse1 = input("La première valeur est-elle vraie ? (True/False) : ")
reponse2 = input("La deuxième valeur est-elle vraie ? (True/False) : ")

val1 = (reponse1 == "True")
val2 = (reponse2 == "True")

if val1 and val2:
    print("Les deux sont vrais")
else:
    print("L'une des valeurs (ou les deux) est fausse")