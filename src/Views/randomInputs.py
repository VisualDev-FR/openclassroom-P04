import random

from datetime import date, datetime
from Models.player import *
from Models.tournament import *

def randomPlayer(playerIndex:int, maxPlayers:int)->Player:
    
    print("Joueur " + str(playerIndex) + " :")
    
    inFirstName = random.choice(["Thomas", "Pauline","Sandra","Pascal","Léa","Julie","Marion","Michel","Deplhine","Kévin","Fanny"])
    inLastName = random.choice(["Menanteau","Fourdrinois","Vantour","Grafmeyer","Levrero"])
    inBirthDay = random.choice(["17/11/1995","28/01/1997","16/01/2001","03/12/1966","18/08/1960","28/12/1966","01/06/2007"])
    inGender = Gender(random.choice([0,1]))
    inAssessement = random.choice(range(1, maxPlayers + 1))

    print("    Prénom : " + inFirstName)
    print("    Nom : " + inLastName)
    print("    Anniversaire : " + inBirthDay)
    print("    Genre : " + inGender.name)
    print("    Classement : " + str(inAssessement))

    print(" ")

    return Player(firstName=inFirstName, lastName=inLastName, birthday=inBirthDay, gender=inGender, assessement=inAssessement)

def randomTournament()->Tournament: 

    roundsCount = random.choice([4 ,5 ,6, 7, 8])
    playersCount = random.choice([4 ,6 ,8, 10, 12])
    name = random.choice(["Tournoi amical du club d'échec de Vitrolles", "Championnats de France d'echecs"])
    location = random.choice(["Vitrolles", "Paris", "Marseille", "Lyon", "Strasbourg", "Bourg-en-Bresse", "Dunkerque"])
    tDate = random.choice(["18/11/2019", "18/11/2020", "18/11/2021", "18/11/2022"])
    timeControl = random.choice([0, 1, 2])
    description = random.choice(["Tournoi Amical", "Tournoi amical en vue de la préparation des championnats de france", "Tournoi Homme vs Machine"])

    print("    Nombre de tours : " + str(roundsCount))
    print("    Nombre de joueurs : " + str(playersCount))
    print("    Nom du trournoi : " + name)
    print("    Lieu du tournoi : " + location)
    print("    Date du tournoi : " + tDate)
    print("    Format de temps Bullet[0] Blitz[1] Rapid[2]: " + str(timeControl))
    print("    Descritpion : " + description)

    print(" ")

    return Tournament(
        roundsCount=roundsCount, 
        playersCount=playersCount, 
        name=name, 
        location=location, 
        date=datetime.strptime(tDate, DATE_FORMAT), 
        timeControl=timeControl, 
        description=description
    )

def randomWinner(player1:Player, player2:Player)->Player:
    winnerIndex = random.choice([0, 1])
    print("    {p1}[0] vs {p2}[1] : vainqueur = {index}".format(p1=player1.getFullName(), p2=player2.getFullName(), index=winnerIndex))    
    return (player1, player2)[winnerIndex == 2]
