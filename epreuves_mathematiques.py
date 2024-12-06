# Utilisation du module 'random' pour les 3 jeux de hasard
import random

# Fonction récursive qui renvoie la factorielle d'un argument
def factorielle(n):
    if n == 0:
        return 1
    return factorielle(n-1)*n

# Epreuve : Déterminer/Calculer la factorielle d'un nombre choisi aléatoirement
## La fonction renvoie 'True' si le joueur gagne, 'False' si le joueur ne gagne pas
def epreuve_math_factorielle():
    n = random.randint(1, 10)                   ## Tirage au hasard pour déterminer la factorielle à calculer
    print("Calculer la factorielle de", n, ".")
    resultat = factorielle(n)
    reponse_utilisateur = int(input("Votre réponse: "))
    if resultat == reponse_utilisateur:                     ## On vérifie que le joueur a eu la bonne réponse
        print("Correct! Vous gagnez une clé.")
        return True
    else:
        return False


# Fonction qui détermine aléatoirement les coefficients de l'équation linéaire de l'exercice sur les équations linéaires
## La fonction renvoie les coefficients de l'équation linéaire ainsi que la solution d'une équation avec ces coefficients
def resoudre_equation_lineaire():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    x = -b/a                    ## x la solution de l'équation linéaire 'ax + b'
    return a, b, x

# Epreuve : Déterminer/Calculer la solution d'une équation linéaire pour des coefficients choisis aléatoirement
## La fonction renvoie 'True' si le joueur gagne, 'False' si le joueur ne gagne pas
def epreuve_math_equation():
    a, b, x = resoudre_equation_lineaire()                  ## Utilisation de la fonction pour tirer au sort les coefficients
    print("Épreuve de Mathématiques: Résoudre l'équation", a, "x +", b, "= 0.")
    reponse_utilisateur = float(input("Quelle est la valeur de x: "))
    if reponse_utilisateur == round(x, 2):                  ## On vérifie si le joueur a eu la bonne réponse
        print("Correct! Vous gagnez une clé.")
        return True
    else:
        return False

# Fonction qui renvoie si l'argument n est premier ou non
def est_premier(n):
    premier = True                  ## On part du fait qu'il est premier
    for i in range(2, n):                   ## On vérifie si n a des diviseurs autres que 1 & n
        if n % i == 0:                  ## Si oui, alors il ne peut être premier
            premier = False                 ## Car si on trouve un diviseur un diviseur autre que 1 et n alors il n'est pas premier
    return premier

# Fonction qui renvoie le nombre premier le plus proche est supérieur à l'argument n
def premier_plus_proche(n):
    i = n
    premier = est_premier(i)
    while not premier:                  ## Tant que nous ne trouvons aucun premier on continue à chercher
        i += 1
        premier = est_premier(i)

    return i

# Epreuve : Déterminer le nombre premier le plus proche d'un nombre au hasard entre 10 & 20
## La fonction renvoie 'True' si le joueur gagne, 'False' si le joueur ne gagne pas
def epreuve_math_premier():
    n = random.randint(10, 20)                  ## Tirage aléatoire du nombre
    print("Épreuve de Mathématiques: Trouver le nombre premier le plus proche de", n, ".")
    reponse_utilisateur = int(input("Votre réponse: "))
    if reponse_utilisateur == premier_plus_proche(n):                   ## On vérifie si le joueur a trouvé la bonne réponse
        print("Correct! Vous gagnez une clé.")
        return True
    else:
        return False


# Epreuve : Calculer une opération aléatoire de valeurs aléatoires
## La fonction renvoie 'True' si le joueur gagne, 'False' si le joueur ne gagne pas
def epreuve_roulette_mathematique():
    liste_nombre = [random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20)]                  ## On tire au hasard les nombres qui subiront l'opération
    operateur = random.randint(1, 3)                ## On tire au hasard l'opération à effectuer
    print("Nombres sur la roulette :", liste_nombre)
    if operateur == 1:
        print("Calculez le résultat en combinant ces nombres avec une addition.")
        reponse_utilisateur = int(input("Votre réponse : "))
        if reponse_utilisateur == liste_nombre[0]+liste_nombre[1]+liste_nombre[2]+liste_nombre[3]+liste_nombre[4]:                  ## On vérifie si le joueur a trouvé la bonne réponse
            print("Bonne réponse! Vous avez gagné une clé.")
            return True
        else:
            return False
    if operateur == 2:
        print("Calculez le résultat en combinant ces nombres avec une soustraction.")
        reponse_utilisateur = int(input("Votre réponse : "))
        if reponse_utilisateur == liste_nombre[0]-liste_nombre[1]-liste_nombre[2]-liste_nombre[3]-liste_nombre[4]:                  ## On vérifie si le joueur a trouvé la bonne réponse
            print("Bonne réponse! Vous avez gagné une clé.")
            return True
        else:
            return False
    if operateur == 3:
        print("Calculez le résultat en combinant ces nombres avec une multiplication.")
        reponse_utilisateur = int(input("Votre réponse : "))
        if reponse_utilisateur == liste_nombre[0]*liste_nombre[1]*liste_nombre[2]*liste_nombre[3]*liste_nombre[4]:                  ## On vérifie si le joueur a trouvé la bonne réponse
            print("Bonne réponse! Vous avez gagné une clé.")
            return True
        else:
            return False


# Tirage au hasard de l'épreuve pour le joueur
def epreuve_math():
    epreuves = [epreuve_math_factorielle, epreuve_math_premier, epreuve_math_equation, epreuve_roulette_mathematique]
    epreuve = random.choice(epreuves)
    return epreuve()