saisie = input("Entrez un nombre : ")

try:
    if "." in saisie:
        nombre = float(saisie)
    else:
        nombre = int(saisie)
    
    print("Le type de la variable est :", type(nombre))
except:
    print("Ce n'est pas un nombre valide.")