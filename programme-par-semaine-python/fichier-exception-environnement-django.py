# exo1 et 2

import csv #ici on n'importe le module qui permet a python de comprendre les fichier.csv

# Définition d'une exception personnalisée
class StockVideError(Exception):
    pass #Ici, tu crées ton propre type d'erreur. En héritant de Exception, tu dis à Python : « Désormais, StockVideError est une erreur officielle dans mon programme ». Le pass signifie qu'on ne rajoute pas de code spécial, on veut juste le nom de l'erreur.

def charger_medicaments(nom_fichier):
    try:
        with open(nom_fichier, mode='r', encoding='utf-8') as fichier: 
# try: : On commence un bloc "essai". Si une erreur arrive dans les lignes qui suivent, Python ne plantera pas, il ira directement au bloc except à la fin.

# with open(...) : On ouvre le fichier. Le with est très important : il garantit que le fichier sera fermé automatiquement, même s'il y a un bug.

# mode='r' : Ouverture en lecture (read).

# encoding='utf-8' : Pour bien lire les accents (é, à, ç) fréquents en français.

            lecteur = csv.DictReader(fichier)
            for ligne in lecteur: #csv.DictReader : C'est la version "intelligente". Elle utilise la première ligne du CSV (l'entête) pour créer un Dictionnaire pour chaque ligne. Au lieu d'accéder aux données par numéro (0, 1), on les appelle par leur nom (nom, stock).
                nom = ligne['nom']
                stock = int(ligne['stock']) #On récupère les valeurs. int() est crucial ici : dans un CSV, tout est considéré comme du texte. Pour faire des calculs ou des comparaisons, il faut transformer le stock en nombre entier.
                
                if stock == 0:
                    raise StockVideError(f"Alerte : {nom} est totalement épuisé !")
                print(f"Médicament : {nom} | Stock : {stock}")
# if stock == 0: : On vérifie la condition.

# raise : C'est l'ordre de déclencher l'alarme. On crée volontairement une erreur car un stock vide est un problème grave pour ta pharmacie.

# Si le stock n'est pas à 0, le print s'exécute normalement.

                
    except FileNotFoundError: #Si quelque chose a mal tourné plus haut, Python saute directement ici :
        print("Erreur : Le fichier de données est introuvable.")
    except StockVideError as e: #Si tu as fait une faute de frappe dans le nom du fichier sur ton Ubuntu.
        print(e)
    except Exception as e: #Si le raise a été activé parce qu'un médicament était à zéro, on affiche le message d'alerte.
        print(f"Une erreur imprévue est survenue : {e}")


# apres avoir creer le fichier medicament.csv et enregistrer les medic on reviens ici ecrire cette ligne pour appeler la fonction pour tester. puis aller dans le terminal ce placer dans le fichier a tester et lancer : python3 nom_fichier.py
charger_medicaments('medicaments.csv')



# Try : "Essaie d'ouvrir et de lire."

# Raise : "Si le stock est vide, déclenche l'alerte !"

# Except : "Si ça a raté, affiche l'explication au lieu de planter."




# exo3
# # 1. Créer le dossier du projet
# mkdir mon_projet_django && cd mon_projet_django

# # 2. Créer l'environnement virtuel
# python3 -m venv venv

# # 3. L'activer
# source venv/bin/activate

# # 4. Installer Django
# pip install django

# # 5. Créer le fichier des dépendances
# pip freeze > requirements.txt

# # 6. Vérifier l'installation
# django-admin --version