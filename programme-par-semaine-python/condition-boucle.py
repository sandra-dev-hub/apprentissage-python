# mini-quiz:demander une note sur 20 et afficher TB,B,I
note=float(input("entrer une note inferieur ou egale a 20 : "))
if note>=16:
    print("tres bien")

elif note>=12:
    print("bien")

else:
    print("insuffisant")

    # afficher les multiple de 3 entre 1 et 50 avec for + continue
print("afficher les multiple de 3 entre 1 et 50 :")
for nbre in range(1, 50):
    if nbre % 3 ==0:
        print(nbre)

        # jeu:devinez un nombre (white+break):base de la logique de validation django
nombre_secret = 7
tentatives = 0

while True:
    essai = int(input("Devinez le nombre entre 1 et 10 : "))
    tentatives += 1
    
    if essai == nombre_secret:
        print(f"Bravo ! Trouve en {tentatives} tentatives.")
        break
    else:
        print("Rate, réessayez !")