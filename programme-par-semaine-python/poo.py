# class Medicament:
#     def __init__(self, nom, prix, stock):
#         self.nom = nom
#         self.prix = prix
#         self.stock = stock

#     def is_disponible(self):
#         return self.stock > 0

#     def __str__(self):
#         return f"{self.nom} ({self.stock} en stock)"

# # Test
# m1 = Medicament("Efferalgan", 500, 10)
# print(m1) # Utilise __str__
# print(f"Disponible ? {m1.is_disponible()}")





# class Produit:
#     def __init__(self, nom, prix_ht):
#         self.nom = nom
#         self.prix_ht = prix_ht

#     @property
#     def prix_ttc(self):
#         return self.prix_ht * 1.19 # Taxe de 19%

# # Utilisation
# p = Produit("Sirop", 1500)
# # Notez qu'on ne met pas de parenthèses après prix_ttc grâce au décorateur
# print(f"Prix HT : {p.prix_ht} | Prix TTC : {p.prix_ttc}")




from django.db import models

class Medicament(models.Model): # Héritage
    nom = models.CharField(max_length=100) # Attribut
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self): # Méthode spéciale
        return self.nom