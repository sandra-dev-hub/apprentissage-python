# 1. Conduite (Âge + Permis)
age_conducteur = int(input("Âge : "))
a_le_permis = input("Avez-vous le permis ? (oui/non) : ").lower() == "oui"

if age_conducteur >= 18 and a_le_permis:
    print("Vous pouvez conduire.")
else:
    print("Vous ne pouvez pas conduire.")

# 2. Nombre entre 10 et 20
nombre = float(input("Entrez un nombre : "))
if 10 <= nombre <= 20: # Ou : nombre >= 10 and nombre <= 20
    print("Le nombre est entre 10 et 20.")

# 3. Mot de passe
mdp = input("Entrez le mot de passe : ")
if mdp != "1234":
    print("Accès refusé : mot de passe incorrect.")