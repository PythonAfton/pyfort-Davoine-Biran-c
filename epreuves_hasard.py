import random


def bonneteau():
    liste_bonneteau = ['A', 'B', 'C']
    print("Épreuve de Hasards: trouver la clef sous l'un des bonneteaus, vous avez 2 essai.")
    print("Les trois bonneteau sont ", liste_bonneteau)
    for tentative in range(1, 3):
        emplacement_clef = random.randint(0, 2)
        print(3-tentative, "tentatives restantes.")
        choix_utilisateur = input("Votre choix: ")
        choix_utilisateur = choix_utilisateur.upper()
        if choix_utilisateur in liste_bonneteau:
            if choix_utilisateur == liste_bonneteau[emplacement_clef]:
                print("Vous avez trouvé la clef.")
                return True
            else:
                print("Vous n'avez pas trouvé la clef.")
        else:
            print("Votre choix est invalide.")
    print("Vous avez perdu, la clef se trouvait sous le bonneteau ", liste_bonneteau[emplacement_clef],".")
    return False


def jeu_lance_des():
    nb_essai = 3
    for essai in range(nb_essai):
        print(nb_essai-essai, "tentatives restantes.")
        input("Lancez les dés")
        lance_des_utilisateur = (random.randint(1, 6), random.randint(1, 6))
        print(lance_des_utilisateur)
        if 6 in lance_des_utilisateur:
            print("Vous avez gagné la clef.")
            return True
        lance_des_mdj = (random.randint(1, 6), random.randint(1, 6))
        print(lance_des_mdj)
        if 6 in lance_des_mdj:
            print("Le maitre du jeu a gagné.")
            return False
        print("Aucun 6 on passe au prochaine essai.")
    print("Aucun en 3 essai. Match nul.")
    return False


def epreuve_hasard():
    epreuves = [bonneteau, jeu_lance_des]
    epreuve = random.choice(epreuves)
    return epreuve()