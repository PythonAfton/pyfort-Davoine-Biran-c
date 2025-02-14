from epreuves_mathematiques import *
from epreuves_hasard import *
from epreuves_logiques import *
from enigme_pere_fouras import *


def introduction():
    print("Le joueur doit accomplir des épreuves pour gagner des clés et déverrouiller la salle du trésor.L'objectif est de ramasser trois clés pour accéder à la salle du trésor.")


def composer_equipe():
    nb_joueur = input("Combien de joueur souhaitez vous inscrire ? ")
    while nb_joueur[0] > '3' or nb_joueur[0] <= '0':
        nb_joueur = input("Combien de joueur souhaitez vous inscrire ?(3 maximum) ")
    equipe = []
    leader = False
    for i in range(int(nb_joueur)):
        joueur = {}
        joueur["nom"] = input("Saisir le nom du joueur: ")
        joueur["profession"] = input("Saisir la profession du joueur: ")
        if not leader:
            joueur["leader"] = input("Ce joueur est il le leader de l'équipe ?oui/non ")
            while joueur["leader"] not in ["oui", "non"]:
                joueur["leader"] = input("Ce joueur est il le leader de l'équipe ?oui/non ")
        else:
            joueur["leader"] = False
        if joueur["leader"] == "oui":
            leader = True
            joueur["leader"] = True
        joueur["cles_gagnees"] = 0
        equipe.append(joueur)


def menu_epreuves():
    epreuve = input("Saisir le numéro de l'epreuve \n 1 : Mathématiques \n 2 : Logique \n 3 : Hasard \n 4 : Enigme du Père Fouras \n Votre réponse : ")
    while epreuve not in ['1','2','3','4']:
        epreuve = input("Saisir le numéro de l'epreuve \n 1 : Mathématiques \n 2 : Logique \n 3 : Hasard \n 4 : Enigme du Père Fouras \n Votre réponse : ")
    if epreuve == '1':
        return epreuve_math()
    elif epreuve == '2':
        return epreuve_logique()
    elif epreuve == '3':
        return epreuve_hasard()
    elif epreuve == '4':
        return enigme_pere_fouras()


def choisir_joueur(equipe):
    for i in range(len(equipe)):
        if equipe[i]["leader"]:
            print(i, equipe[i]["nom"], "(", equipe[i]["profession"], ")", "- Leader")
        else:
            print(i, equipe[i]["nom"], "(", equipe[i]["profession"], ")", "- Membre")
    num_joueur = int(input("Entrez le numero du joueur: "))
    return equipe[num_joueur]
