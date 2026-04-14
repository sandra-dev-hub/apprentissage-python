# "1) Fonction calculer_prix_ttc(prix, taux=0.19) avec valeur par défaut
# def calculer_prix_ttc(prix_ht, taux=0.19):
#     montant_taxe=prix_ht*taux
#     prix_ttc=prix_ht+montant_taxe
#     return prix_ttc

# print(f"prix avec taxe par defaut:{calculer_prix_ttc(1000)}")
# print(f"prix avec taxe personnalisee(5%):{calculer_prix_ttc(1000, 0.05)}")


# 2) Fonction verifier_stock(medicament, quantite) → True/False (anticipation du projet)
# ici j'utilise une fonction logique
# def verifier_stock(medicament, quantite_dispo):
#     if quantite_dispo <= 0:
#         return f"Alerte : Le médicament '{medicament}' est en rupture !"
#     elif quantite_dispo < 5:
#         return f"Attention : Stock faible pour '{medicament}' ({quantite_dispo} restants)."
#     else:
#         return f"Stock suffisant pour '{medicament}'."
    



# 3) Utiliser datetime.date.today() → manipuler les dates comme Django (DateField)"

from datetime import date
def afficher_infos_date():
    aujourdhui = date.today()
    print(f"Date du jour : {aujourdhui}")
    print(f"Année : {aujourdhui.year}")
    print(f"Mois : {aujourdhui.month}")
    print(f"Jour : {aujourdhui.day}")

afficher_infos_date()