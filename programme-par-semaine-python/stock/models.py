from django.db import models

class Medicament(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    stock_disponible = models.IntegerField(default=0) # On ajoute le stock !

    def __str__(self):
        return f"{self.nom} - {self.prix} FCFA"