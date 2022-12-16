# Openclassroom P04 - Developpez un programme logiciel en python

Cette application a pour but de gérer des tournois d'échecs, en s'appuyant une base donnée (format json) de joueurs et de tournois gérée dynamiquement.

Le programme permet :

- de créer et sauvegarder des joueurs dans la base de données.
- de créer et sauvegarder des tournois dans la base de données.
- d'afficher les joueurs enregistrés par classement / par ordre alphabétique.
- d'afficher les tournois enregistrés dans la base données.

Une base de donnée ```db.json``` contenant 16 joueurs et 1 tournoi, est à disposition dans le dépôt pour permettre d'effectuer des tests.

## Configuration de l'environnement virtuel :

Le programme utilise plusieurs librairies externes, et modules de Python, qui sont repertoriés dans le fichier ```requirements.txt```

Pour configuer l'environnement, commencez par ouvrir un terminal à la racine du projet.

Créez un environnement virtuel à partir de la commande suivante : 
```bash
python -m venv env
```
Installez les packages python spécifiés dans le fichier ```requirement.txt``` :

```bash
pip install -r requirement.txt
```

activez l'environnement virtuel que vous venez de créer avec la commande suivante :

```bash
env/Scripts/activate
```


## Démarrage 

Ouvrez un terminal à la racine du projet, et entrez la commande suivante :

```bash
python /src/main.py
```

## Rapport flake8

Le dépôt contient un rapport flake8, qui n'affiche aucune violation des règles PEP8. 

Il est possible d'en générer un nouveau en activant l'environnement virtuel (voir procédure ci-dessus) et en entrant la commande suivante dans le terminal :

```bash
flake8 .\src\ --format=html --htmldir=flake-report
```

Le fichier ```setup.cfg``` à la racine contient les paramètres concernant la génération du rapport.

Le rapport se trouve dans le repertoire ```flake-report```
