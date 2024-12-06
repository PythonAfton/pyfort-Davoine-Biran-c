# Utilisation du module 'random' pour les 3 jeux de hasard
import random

# Définition de la fonction permettant aux joueurs de lancer une partie de bonneteau
## La fonction renvoie 'True' si le joueur gagne, 'False' si le joueur ne gagne pas
def bonneteau():
    liste_bonneteau = ['A', 'B', 'C']
    print("Épreuve de Hasards: trouver la clef sous l'un des bonneteaus, vous avez 2 essai.")
    print("Les trois bonneteau sont ", liste_bonneteau)
    for tentative in range(1, 3):               ## Le joueur continue à jouer tant qu'il lui reste des tentatives
        emplacement_clef = random.randint(0, 2)                 ## On choisie le bon gobelet au hasard
        print(3-tentative, "tentatives restantes.")
        choix_utilisateur = input("Votre choix: ")
        choix_utilisateur = choix_utilisateur.upper()                   ## On fait en sorte que la réponse joueur soit en majuscule
        if choix_utilisateur in liste_bonneteau:                    ## On vérifie que la réponse soit "A", "B" ou "C"
            if choix_utilisateur == liste_bonneteau[emplacement_clef]:              ## On vérifie si le joueur a trouvé la bonne réponse
                print("Vous avez trouvé la clef.")
                return True
            else:
                print("Vous n'avez pas trouvé la clef.")
        else:
            print("Votre choix est invalide.")                  ## Si la réponse joueur n'est pas "A", "B" ou "C"
    print("Vous avez perdu, la clef se trouvait sous le bonneteau ", liste_bonneteau[emplacement_clef],".")             ## Si l'utilisateur n'a plus de tentatives restantes
    return False

# Définition de la fonction permettant aux joueurs de lancer une partie de lancée de dés
## La fonction renvoie 'True' si le joueur gagne, 'False' si le joueur ne gagne pas
def jeu_lance_des():
    nb_essai = 3                ## On définit un nombre d'essais maximum
    for essai in range(nb_essai):
        print(nb_essai-essai, "tentatives restantes.")
        input("Lancez les dés")
        lance_des_utilisateur = (random.randint(1, 6), random.randint(1, 6))
        print(lance_des_utilisateur)
        if 6 in lance_des_utilisateur:                  ## On vérifie si le joueur a obtenu au moins un 6 au lancé de dés
            print("Vous avez gagné la clef.")
            return True
        lance_des_mdj = (random.randint(1, 6), random.randint(1, 6))
        print(lance_des_mdj)
        if 6 in lance_des_mdj:                  ## On vérifie si le mdj a obtenu au moins un 6 au lancé de dés
            print("Le maitre du jeu a gagné.")
            return False
        print("Aucun 6 on passe au prochaine essai.")
    print("Aucun en 3 essai. Match nul.")
    return False

# Choix aléatoire du jeu de hasard (ironique)
def epreuve_hasard():
    epreuves = [bonneteau, jeu_lance_des]
    epreuve = random.choice(epreuves)               ## On choisie aléatoirement le jeu de hasard qu'aura le joueur
    return epreuve()