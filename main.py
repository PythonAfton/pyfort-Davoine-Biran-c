from epreuve_finale import *
from fonctions_utiles import *


def jeu():
    introduction()
    composer_equipe()
    nb_clef_equipe = 0
    while nb_clef_equipe < 3:
        if menu_epreuves():
            nb_clef_equipe += 1
    salle_De_Tresor()


if __name__ == '__main__':
    jeu()