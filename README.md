# OCR_projet_4
## Description du projet:
  Ce projet s'incris dans le cadre de la formation "Développeur d'application : Python" de OpenClassRooms.
  Le but de ce projet et de créer un programme Python en ligne de commande qui permet de gérer un tournoi d'échecs. Ce programme doit fonctionner hors ligne et doit permettre de stocker les informations sur le disque à l'aide de "Tiny_db"
  
## Fonctionnalités du programme:
  Ce programme permet:
    - La sauvegarde des joueurs en base de données. (prénom, nom, date de naissance, sexe, classement).
    - La gestion des joueurs avec des options de modification ou de suppression.
    - La création d'un tournoi et son enregistrement en base de données.
    - Chaque tournoi est caractérisé par :
      * un nom
      * un lieu
      * une date
      * un nombre de joueurs
      * un nombre de tours
      * une manière de gérer le temps dans les matchs
      * une description
    - Chaque tournoi peut être interrompu entre chaque ronde, sauvegarder et repris plus tard.
    - L'ensemble des tournois enregistrés en base de données (fini ou en cours) peuvent être consultés sous forme d'un rapport de tournoi.
    - La suppression d'un tournoi.
    
 ## Pré-requis:
   - Language de programmation:
      Python3
   - Module utilisés:
      - TinyDB
      - Colorama
      - Pytest
   - Un fichier **requirements.txt** est disponible sur le depository.

## Installation:
   - Créer un dossier, par exemple "Programme échec".
   - Copier et dézipper l' archive dans le dossier.
   - Ouvrir une console et se placer dans le dossier.
   - Créer un environnement virtuel grâce à la commande " py -m venv env".
   - Activer l'environnent virtuel avec la commande : "source env/Scripts/activate".
   - Installer les packages nécessaires avec la commande : " pip install -r requirements.txt".

 ## Utilisation:
   - Exécuter le programme soit en tapant "py main.py" dans la console ou au travers d'un éditeur de code.
   - Le programme se lance sur le menu principal qui vous permet la gestion des joueurs ou des tournois.
   - Le menu "gestion des joueurs" vous permet de créer, afficher, modifier ou supprimer un joueur.
   - Le menu "gestion des tournois" vous permet de créer, de reprendre et de supprimer un tournoi.
   - Le menu "gestion des tournois permet également d'afficher les rapports des tournois terminés
   - La touche "m" permet le retour au menu précédent.
   - On quitte le programme avec la touche "3" à partir du menu principal.

  ## Flake8
    Vous pouvez acceder au rapport Flak8 avec la commande :
      flake8 --max-line-length 119 --format=html --htmldir=flake-report model view controller utils

  
   ## Version:
   - Ce programme constitue une première version totalement en ligne de commande et hors ligne, qui doit être validé par le client.
    
   ## Auteurs:
   Parajua Pierre
      
      
  
