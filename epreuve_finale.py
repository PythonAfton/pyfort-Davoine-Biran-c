import json
import random


def salle_De_Tresor():
    with open("./data/indicesSalle.json", 'r', encoding='utf-8') as f:
        jeu_tv = json.load(f)
    annee = str(random.randint(2015, 2023))
    num_emission = str(random.randint(1, len(jeu_tv["Fort Boyard"][annee])))
    if annee == "2023":
        if num_emission == "10":
            num_emission = str(random.randint(1, len(jeu_tv["Fort Boyard"][annee])-1))
        if num_emission == "4":
            AB = random.randint(0, 1)
            if AB == 1:
                num_emission = num_emission+"A"
            else:
                num_emission = num_emission+"B"
    if num_emission == "10" or num_emission == "11":
        emission = "Émission " + num_emission
    else:
        emission = "Émission 0" + num_emission
    indices = jeu_tv["Fort Boyard"][annee][emission]["Indices"]
    mot_code = jeu_tv["Fort Boyard"][annee][emission]["MOT-CODE"]
    print("Indices:", indices[0], indices[1], indices[2])
    reponse_correcte = False
    essai = 3
    while essai > 0 and not reponse_correcte:
        reponse_joueur = input("Votre réponse: ")
        reponse_joueur = reponse_joueur.upper()
        if reponse_joueur == mot_code:
            reponse_correcte = True
        else:
            essai -= 1
            if essai > 0:
                print("Il vous reste", essai, "essai")
                print("Indice suplémentaire: ", indices[3+essai])
            else:
                print("Le mot code est:", mot_code)
    if reponse_correcte:
        print("Vous avez gagné.")
    else:
        print("Vous avez perdu.")
