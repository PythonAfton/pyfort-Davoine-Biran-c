import random


def factorielle(n):
    if n == 0:
        return 1
    return factorielle(n-1)*n


def epreuve_math_factorielle():
    n = random.randint(1, 10)
    print("Calculer la factorielle de", n, ".")
    resultat = factorielle(n)
    reponse_utilisateur = int(input("Votre réponse: "))
    if resultat == reponse_utilisateur:
        print("Correct! Vous gagnez une clé.")
        return True
    else:
        return False


def resoudre_equation_lineaire():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    x = -b/a
    return a, b, x


def epreuve_math_equation():
    a, b, x = resoudre_equation_lineaire()
    print("Épreuve de Mathématiques: Résoudre l'équation", a, "x +", b, "= 0.")
    reponse_utilisateur = float(input("Quelle est la valeur de x: "))
    if reponse_utilisateur == round(x, 2):
        print("Correct! Vous gagnez une clé.")
        return True
    else:
        return False


def est_premier(n):
    premier = True
    for i in range(2, n):
        if n % i == 0:
            premier = False
    return premier


def premier_plus_proche(n):
    i = n
    premier = est_premier(i)
    while not premier:
        i += 1
        premier = est_premier(i)

    return i


def epreuve_math_premier():
    n = random.randint(10, 20)
    print("Épreuve de Mathématiques: Trouver le nombre premier le plus proche de", n, ".")
    reponse_utilisateur = int(input("Votre réponse: "))
    if reponse_utilisateur == premier_plus_proche(n):
        print("Correct! Vous gagnez une clé.")
        return True
    else:
        return False


def epreuve_roulette_mathematique():
    liste_nombre = [random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20)]
    operateur = random.randint(1, 3)
    print("Nombres sur la roulette :", liste_nombre)
    if operateur == 1:
        print("Calculez le résultat en combinant ces nombres avec une addition.")
        reponse_utilisateur = int(input("Votre réponse : "))
        if reponse_utilisateur == liste_nombre[0]+liste_nombre[1]+liste_nombre[2]+liste_nombre[3]+liste_nombre[4]:
            print("Bonne réponse! Vous avez gagné une clé.")
            return True
        else:
            return False
    if operateur == 2:
        print("Calculez le résultat en combinant ces nombres avec une soustraction.")
        reponse_utilisateur = int(input("Votre réponse : "))
        if reponse_utilisateur == liste_nombre[0]-liste_nombre[1]-liste_nombre[2]-liste_nombre[3]-liste_nombre[4]:
            print("Bonne réponse! Vous avez gagné une clé.")
            return True
        else:
            return False
    if operateur == 3:
        print("Calculez le résultat en combinant ces nombres avec une multiplication.")
        reponse_utilisateur = int(input("Votre réponse : "))
        if reponse_utilisateur == liste_nombre[0]*liste_nombre[1]*liste_nombre[2]*liste_nombre[3]*liste_nombre[4]:
            print("Bonne réponse! Vous avez gagné une clé.")
            return True
        else:
            return False


def epreuve_math():
    epreuves = [epreuve_math_factorielle, epreuve_math_premier, epreuve_math_equation, epreuve_roulette_mathematique]
    epreuve = random.choice(epreuves)
    return epreuve()