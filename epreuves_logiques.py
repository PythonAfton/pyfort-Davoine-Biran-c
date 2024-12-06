import random


def affiche_batonets(n):
    print("|"*n)


def joueur_retrait(n):
    nb_retrait = int(input("Choisir le nombre de batonnet à retirer(1,2 ou 3). "))
    while nb_retrait not in [1, 2, 3]:
        nb_retrait = int(input("Choisir le nombre de batonnet à retirer(1,2 ou 3). "))
    return nb_retrait


def maitre_retrait(n):
    if n % 4 > 1:
        nb_retrait = n % 4-1
    else:
        nb_retrait = 3
    return nb_retrait


def jeu_nim():
    nb_batonnets = 20
    tour_joueur = True
    while nb_batonnets > 0:
        affiche_batonets(nb_batonnets)
        if tour_joueur:
            print("Tour du joueur.")
            nb_retrait = joueur_retrait(nb_batonnets)
            tour_joueur = False
        else:
            nb_retrait = maitre_retrait(nb_batonnets)
            print("Le maitre du jeu retire", nb_retrait, "batonnets.")
            tour_joueur = True
        nb_batonnets -= nb_retrait
    if tour_joueur:
        print("Le maitre du jeu a retiré le dernier batonnet. Le joueur gagne !")
        return True
    else:
        print("Le joueur a retiré le dernier batonnet. Le maitre du jeu gagne !")
        return False


def afficher_grille(grille):
    for i in range(3):
        for j in range(3):
            print(grille[i][j], end=" ")
            if j != 2:
                print("|", end=" ")
        print("\n ---------")


def verifier_victoire(grille, symbole):
    diagonale = []
    antidiagonale = []
    for i in range(3):
        colonne = []
        for j in range(3):
            colonne.append(grille[j][i])
        diagonale.append(grille[i][i])
        antidiagonale.append(grille[i][3-i-1])
        if grille[i] == [symbole]*3 or colonne == [symbole]*3 or diagonale == [symbole]*3 or antidiagonale == [symbole]*3:
            return True
    return False


def coup_maitre(grille, symbole):
    coup_trouve = False
    grille_test = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    for i in range(3):
        for j in range(3):
            grille_test[i][j] = grille[i][j]
    for i in range(3):
        for j in range(3):
            if grille[i][j] == " ":
                tmp = grille_test[i][j]
                grille_test[i][j] = symbole
                if verifier_victoire(grille_test, symbole):
                    return i, j
                grille_test[i][j] = "X"
                if verifier_victoire(grille_test, "X"):
                    coup_defense = (i, j)
                    coup_trouve = True
                grille_test[i][j] = tmp
    if coup_trouve:
        return coup_defense
    else:
        coup_hasard = (random.randint(0, 2), random.randint(0, 2))
        while grille[coup_hasard[0]][coup_hasard[1]] != " ":
            coup_hasard = (random.randint(0, 2), random.randint(0, 2))
        return coup_hasard


def tour_joueur(grille):
    input_joueur = tuple(input("Joueur X, c'est à vous. Où voulez-vous placer votre symbole ? "))
    coup_joueur = input_joueur[0], input_joueur[2]
    while grille[int(coup_joueur[0])-1][int(coup_joueur[1])-1] != " ":
        input_joueur = tuple(input("Joueur X, c'est à vous. Où voulez-vous placer votre symbole ? "))
        coup_joueur = input_joueur[0], input_joueur[2]
    grille[int(coup_joueur[0])-1][int(coup_joueur[1])-1] = "X"


def tour_maitre(grille):
    print("Tour de du maître du jeu (O)...")
    coup = coup_maitre(grille, "O")
    grille[coup[0]][coup[1]] = "O"


def grille_complete(grille):
    for i in range(3):
        for j in range(3):
            if grille[i][j] == " ":
                return False
    return True


def verifier_resultat(grille):
    if verifier_victoire(grille, "X") or verifier_victoire(grille, "O") or grille_complete(grille):
        return True
    return False


def jeu_tictactoe():
    grille = [[" ", " ", " "], [" ", "  ", " "], [" ", " ", " "]]
    print("Pour jouer, entrez les coordonnées de votre coup sous forme ligne, colonne (ex: 1,2). ")
    afficher_grille(grille)
    tourjoueur = True
    while not grille_complete(grille):
        if tourjoueur:
            tour_joueur(grille)
            afficher_grille(grille)
            if verifier_resultat(grille) and verifier_victoire(grille, "X"):
                print("Le joueur a gagné !")
                return True
            tourjoueur = False
        else:
            tour_maitre(grille)
            afficher_grille(grille)
            if verifier_resultat(grille) and verifier_victoire(grille, "O"):
                print("Le maitre du jeu a gagné !")
                return False
            tourjoueur = True
    print("Match nul")
    return False


def suiv(joueur):
    if joueur == 0:
        return 1
    else:
        return 0


def grille_vide():
    grille = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    return grille


def affiche_grille(grille, message):
    print(message)
    for i in range(3):
        for j in range(3):
            print(grille[i][j], end=" ")
            if j != 2:
                print("|", end=" ")
        if i < 2:
            print("\n ---------")
        else:
            print()


def demande_position():
    entree_joueur = tuple(input("Entrez la position (ligne,colonne) entre 1 et 3 (ex: 1,2) :"))
    position_joueur = int(entree_joueur[0])-1, int(entree_joueur[2])-1
    while position_joueur[0] not in (0, 1, 2) or position_joueur[1] not in (0, 1, 2):
        entree_joueur = tuple(input("Entrez la position (ligne,colonne) entre 1 et 3 (ex: 1,2) :"))
        position_joueur = int(entree_joueur[0])-1, int(entree_joueur[2])-1
    return position_joueur


def init():
    grille = grille_vide()
    print("Positionnez vos bateaux :")
    for i in range(2):
        print("Bateau", i+1)
        position = demande_position()
        while grille[position[0]][position[1]] == "B":
            position = demande_position()
        grille[position[0]][position[1]] = "B"
    affiche_grille(grille, "Découvrez votre grille de jeu avec vos bateaux :")
    return grille


def tour(joueur, grille_tirs_joueur, grille_adversaire):

    if joueur == 0:
        affiche_grille(grille_tirs_joueur, "Rappel de l'historique des tirs que vous avez effectués :")
        position = demande_position()
        if grille_adversaire[position[0]][position[1]] == "B":
            grille_tirs_joueur[position[0]][position[1]] = "x"
            print("Touché coulé !")
        else:
            grille_tirs_joueur[position[0]][position[1]] = "."
            print("Dans l'eau...")
    else:
        position = (random.randint(0, 2), random.randint(0, 2))
        while grille_adversaire[position[0]][position[1]] == "x":
            position = (random.randint(0, 2), random.randint(0, 2))
        print("Le maître du jeu tire en position", position[0]+1, ",", position[1]+1)
        if grille_adversaire[position[0]][position[1]] == "B":
            grille_tirs_joueur[position[0]][position[1]] = "x"
            print("Touché coulé !")
        else:
            grille_tirs_joueur[position[0]][position[1]] = "."
            print("Dans l'eau...")


def gagne(grille_tirs_joueur):
    nb_bateaux_coules = 0
    for i in range(3):
        for j in range(3):
            if grille_tirs_joueur[i][j] == "x":
                nb_bateaux_coules += 1
            if nb_bateaux_coules == 2:
                return True
    return False


def jeu_bataille_navale():
    print("Chaque joueur doit placer 2 bateaux sur une grille de 3x3.\n"
          "Les bateaux sont représentés par 'B' et les tirs manqués par '.'. Les bateaux coulés sont marqués par 'x'.")
    grille_bateaux_joueur = init()
    grille_bateaux_mdj = grille_vide()
    positon_mdj = random.randint(0, 2), random.randint(0, 2)
    grille_bateaux_mdj[positon_mdj[0]][positon_mdj[1]] = "B"
    positon_mdj = random.randint(0, 2), random.randint(0, 2)
    while grille_bateaux_mdj[positon_mdj[0]][positon_mdj[1]] == "B":
        positon_mdj = random.randint(0, 2), random.randint(0, 2)
    grille_bateaux_mdj[positon_mdj[0]][positon_mdj[1]] = "B"
    grille_tirs_joueurs = grille_vide()
    grille_tirs_mdj = grille_vide()
    joueur = 0
    while True:
        if joueur == 0:
            print("C'est à votre tour de faire feu !:")
            tour(joueur, grille_tirs_joueurs, grille_bateaux_mdj)
            joueur = suiv(joueur)
            if gagne(grille_tirs_joueurs):
                print("Le joueur a gagné !")
                return True

        else:
            print("C'est le tour du maître du jeu :")
            tour(joueur, grille_tirs_mdj, grille_bateaux_joueur)
            joueur = suiv(joueur)
            if gagne(grille_tirs_mdj):
                print("Le maitre du jeu a gagné !")
                return False

def epreuve_hasard():
    epreuves = [jeu_nim, jeu_tictactoe, jeu_bataille_navale]
    epreuve = random.choice(epreuves)
    return epreuve()