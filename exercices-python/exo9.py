saisie_note = input("Entrez votre note sur 100 : ")
note = float(saisie_note)

if note >= 50:
    resultat = "Réussi"
else:
    resultat = "Échoué"

print("Résultat de l'examen :", resultat)