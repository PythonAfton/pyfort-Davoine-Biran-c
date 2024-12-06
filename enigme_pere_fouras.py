import json
import random


def charger_enigmes(fichier):
     # Ouverture du fichier data.json en mode lecture
     with open(fichier, 'r', encoding='utf-8') as f:
          donnees = json.load(f)  # Chargement des données JSON dans une structure Python
     # Affichage de toute la structure 'donnees' pour visualiser le contenu chargé
     fichier.close()
     return donnees


def enigme_pere_fouras():
     liste_enigmes = charger_enigmes("./data/enigmesPF.json")
     enigme = liste_enigmes[random.randint(0, 47)]
     print(enigme['question'])
     essai = 3
     while essai > 0:
          reponse_utilisateur = input("Saisir une reponse")
          reponse_utilisateur = reponse_utilisateur.lower()
          if reponse_utilisateur == enigme["reponse"].lower():
               print("Bonne reponse. Vous gagnez une clef")
               return True
          else:
               essai -= 1
               if essai > 0:
                    print("Mauvaise reponse. Il vous reste", essai, "restant.")
               else:
                    print("Vous avez échoué a l'énigme. La réponse était:", enigme["reponse"])
                    return False