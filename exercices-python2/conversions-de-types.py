# 1. Input en entier et double
valeur = int(input("Entrez un chiffre : "))
print(f"Le double est : {valeur * 2}")

# 2. Prix en string
prix = 19.99
message = "Le prix est de " + str(prix) + " euros."
print(message)

# 3. Somme de deux entrées (Important : input() renvoie toujours du texte)
n_a = float(input("Premier nombre : "))
n_b = float(input("Deuxième nombre : "))
print(f"La somme réelle est : {n_a + n_b}")