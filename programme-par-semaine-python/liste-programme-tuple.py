# Simulation de données (ce que renverrait une base de données)
stocks = [
    {"nom": "Paracétamol", "stock": 50},
    {"nom": "Amoxicilline", "stock": 8},
    {"nom": "Vitamine C", "stock": 3},
    {"nom": "Ibuprofène", "stock": 15}
]

# Filtrer les médicaments dont le stock est < 10
alertes = [m for m in stocks if m["stock"] < 10]

print("Médicaments à recommander d'urgence :")
for item in alertes:
    print(f"- {item['nom']} (Reste : {item['stock']})")





    produits_ht = {"Seringue": 100, "Alcool": 500, "Coton": 200}
TAUX = 0.19

# Création du dictionnaire {nom: prix_ttc}
catalogue_ttc = {nom: prix * (1 + TAUX) for nom, prix in produits_ht.items()}

print(f"Catalogue TTC : {catalogue_ttc}")





# On reprend notre liste de dictionnaires
medicaments = [
    {"nom": "Paracétamol", "prix": 500},
    {"nom": "Amoxicilline", "prix": 2500},
    {"nom": "Vitamine C", "prix": 1200}
]

# # Trier par prix croissant
# # 'key' indique sur quel critère trier
tri_par_prix = sorted(medicaments, key=lambda x: x["prix"])

print("Liste triée par prix :")
for m in tri_par_prix:
    print(f"{m['nom']} : {m['prix']} FCFA")