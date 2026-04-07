saisie_poids = input("Entrez le poids en kg : ")

# 2. Convertir le texte en nombre flottant (pour autoriser les virgules)
poids_kg = float(saisie_poids)

# 3. Calculer la conversion (Affectation d'une nouvelle valeur)
taux_conversion = 2.20462
poids_litres = poids_kg * taux_conversion

# 4. Afficher le résultat final
print("Le poids en livres est :", poids_litres)