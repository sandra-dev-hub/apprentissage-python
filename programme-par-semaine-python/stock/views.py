from django.shortcuts import render
from .models import Medicament

def liste_stock(request):
    produits = Medicament.objects.all()
    return render(request, 'stock/index.html', {'liste': produits})