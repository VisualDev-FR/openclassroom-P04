# Application gérant un tournoi d'échecs

## Openclassroom P04

Projet consistant à créer une application permettant de créer la structure d'un tournoi d'échecs, permettant d'ajouter des joueurs dans une base de données. Le programme utilise un algorithme permettant de calculer la rotation des joueurs afin que les matchs soit équitables et ne se reproduisent pas (algorithme suisse de tournois).

Le programme utilise le design pattern MVC (Modèles - Vues - Controlleurs), et utilise la librairie TinyDB pour sauvegarder les joueurs et les tournois.

Il permet de :

- Créer et sauvegarder des joueurs.
- Mettre à jour le classement d'un joueur.
- Créer et sauvegarder des tournois.
- Lancer des tournois.
- Arrêter un tournoi en cours et le reprendre plus tard.

## Configuration de l'environnement virtuel :

Le programme utilise plusieurs librairies externes, et modules de Python, qui sont repertoriés dans le fichier ```requirements.txt```

Commencez par ouvrir un terminal à la racine du projet 

Créez un environnement virtuel à partir de la commande suivante : 
```bash
python -m venv env
```
Installez les packages python spécifiés dans le fichier ```requirement.txt``` :

```bash
pip install -r requirement.txt
```

## Démarrage 

Ouvrez un terminal à la racine du projet, et entrez la commande suivante :

```bash
python /src/main.py
```

## Rapport flake8

Le dépôt contient un rapport flake8, qui n'affiche aucune erreur. Il est possible d'en générer un nouveau en installant le module ```flake8``` et en entrant dans le terminal :

```bash
flake8 .\src\ --format=html --htmldir=flake-report
```

Le fichier ```setup.cfg``` à la racine contient les paramètres concernant la génération du rapport.

Le rapport se trouve dans le repertoire ```flake-report```
