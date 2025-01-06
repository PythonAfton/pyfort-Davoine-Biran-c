Titre du Projet : pyfort-Davoine-Biran-c

#1 - Présentation Générale

o Contributeurs : Clément DAVOINE & Pablo BIRAN
o Description : Adaptation du célèbre programme français Fort Boyard sur France 2, sous python.
o Fonctionnalités Principales : Nombreuses épreuves testant la logique, la chance, les mathématiques et la célèbre épreuve du père Fouras.
o Technologies Utilisées : 
      - Langage de Programmation : Python
      - Bibliothèque utilisée : random | json
o Installation & Exécution du programme : 
      § Clôner le dépôt à l'aide de la commande suivante : git clone https://github.com/PythonAfton/pyfort-Davoine-Biran-c
      § Exécuter le fichier main.py

# 2 - Documentation Technique

o Fonctions utilisées - "Fonctions utiles" :
      - "introduction" : Affiche l'introduction du jeu au joueur
      - "composer_equipe" : 
          - Demande le nombre de joueurs participant au jeu
          - Redemande le nombre de joueurs tant qu'il y n'y a pas entre 1 et 3 joueurs
          - Demande le nom du joueur puis sa profession
              - Demande également s'il est le leader de l'équipe uniquement s'il n'y a toujours aucun leader (afin qu'il n'y ait qu'un seul leader)
      - "menu_epreuves" : Redirige l'utilisateur sur l'épreuve sélectionnée par celui-ci
      - "choisir_joueur" : 
          - Affiche les membres de l'équipe ansi que son leader
          - Demande à l'utilisateur de choisir un joueur

o Fonctions utilisées - "epreuve_mathematique" :
      - "factorielle" : Calcule et renvoie la factorielle d'un nombre
      - "epreuve_math_factorielle" : Epreuve de calcul d'une factorielle
      - "resoudre_equation_lineaire" : Epreuve de résolution d'équation linéaire
      - "epreuve_math_equation" : Epreuve de résolution d'équation mathématique
      - "est_premier" : Vérifie et renvoie si un nombre donné est premier ou non
      - "premier_plus_proche" : Cherche et renvoie le nombre premier le plus proche d'un nombre donné
      - "epreuve_math_premier" : Epreuve de recherche du nombre premier le plus proche
      - "epreuve_roulette_mathematique" : Epreuve d'opération mathématique (+ ; - ; *) choisi au hasard
      - "epreuve_math" : Sélectionne une des 3 épreuves au hasard

o Fonctions utilisées - "epreuve_logiques" :
      - "affiche_batonets" : Montre les batonnets restants de l'épreuve des batonnets
      - "joueur_retrait" : Permet au joueur de retirer soit 1, 2 ou 3 bâtonnait d'un seul coup
      - "maitre_retrait" : Permet au maître de jeu de retirer soit 1, 2 ou 3 bâtonnait d'un seul coup en fonction d'une stratégie particulière
      - "jeu_nim" : Epreuve du jeu de nim (des bâtonnets)
      - "afficher_grille" : Affiche la grille pour l'épreuve de morpion
      - "verifier_victoire" : Vérifie et renvoie si la grille contient la victoire d'un joueur
      - "coup_maitre" : Détermine où le maître doit jouer
      - "tour_joueur" : Fait jouer le joueur
      - "tour_maitre" : Fait jouer le maître
      - "grille_complete" : Vérifie et renvoie si une grille est complète
      - "verifier_resultat" : Vérifie et renvoie s'il y a une égalité ou si un des joueurs a gagné
      - "jeu_tictactoe" : Epreuve du morpion
      - "suiv" : Fait passer le joueur suivant
      - "grille_vide" : Initialise une grille vide
      - "affiche_grille" : Renvoie la grille
      - "demande_position" : Demande la position à jouer au joueur
      - "init" : initialise le jeu et demande au joueurs de placer ses bâteaux à l'épreuve de la bataille navale
      - "gagne" : Vérifie et renvoie si le joueur a gagné
      - "jeu_bataille_navale" : Epreuve de la bataille navale
      - "epreuve_logique" : Sélectionne une des 3 épreuves au hasard

  o Fonctions utilisées - "epreuve_hasard" :
      - "bonneteau" : Epreuve des bonneteaux
      - "jeu_lance_des" : Epreuve de lancement de dés
      - "epreuve_hasard" : Sélectionne une des 2 épreuves au hasard

  o Fonctions utilisées - "epreuve_finale" :
      - "salle_De_Tresor" : Epreuve de la salle du trésor

  o Fonctions utilisées - "enigme_pere_fouras" : 
      - "charger_enigmes" : Récupère les énigme présents dans le fichier enigmesPF.json
      - "enigme_pere_fouras" : Epreuve du Père Fouras

  o Gestion des entrées erronées
      - Présence de saisies sécurisées, au cas où le joueurs ne saisie les bonnes valeurs 


  # 3 - Journal de Bord

  o Pablo BIRAN
      - Rédaction de "epreuve_mathematiques"
      - Rédaction de "epreuve_hasard"
      - Rédaction de "enigme_pere_fouras"
      - Rédaction de "README" (30/12)

  o Clément DAVOINE
      - Rédaction de "epreuve_logique"
      - Rédaction de "epreuve_finale"
      - Rédaction de "fonctions_utiles"
      - Rédaction de "README" (30/12)


  # 4 - Tests & Validation

  o Appels de fonctions en boucle pour vérifier leurs bon fonctionnement
