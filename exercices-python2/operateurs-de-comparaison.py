# 1. Comparaison de deux nombres
nb1 = float(input("Nombre 1 : "))
nb2 = float(input("Nombre 2 : "))
print(f"Égalité : {nb1 == nb2}")
print(f"Le premier est plus grand : {nb1 > nb2}")

# 2. Majeur ou mineur
age = int(input("Entrez votre âge : "))
if age >= 18:
    print("Majeur")
else:
    print("Mineur")