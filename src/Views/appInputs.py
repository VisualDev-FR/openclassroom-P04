from datetime import date, datetime
import random
from Models.player import Gender
from Models.player import Player
from Models.tournament import Tournament
from Models.tournament import TimeControl

class AppInput:
    
    @classmethod
    def randomPlayer(cls, playerIndex:int)->Player:
        
        print("Joueur " + str(playerIndex) + " :")
        
        inFirstName = random.choice(["Thomas", "Pauline","Sandra","Pascal","Léa","Julie","Marion","Michel","Deplhine","Kévin","Fanny"])
        inLastName = random.choice(["Menanteau","Fourdrinois","Vantour","Grafmeyer","Levrero"])
        inBirthDay = random.choice(["17/11/1995","28/01/1997","16/01/2001","03/12/1966","18/08/1960","28/12/1966","01/06/2007"])
        inGender = Gender(random.choice([0,1]))
        
        print("    Prénom : " + inFirstName)
        print("    Nom : " + inLastName)
        print("    Anniversaire : " + inBirthDay)
        print("    Genre : " + inGender.name)

        return Player(firstName=inFirstName, lastName=inLastName, birthday=inBirthDay, gender=inGender)

    @classmethod
    def randomTournament(cls)->Tournament: 

        print("Veuillez spécifier un nouveau tournoi :")

        roundsCount = random.choice([1, 2, 3, 4 ,5 ,6, 7, 8])
        playersCount = random.choice([4 ,6 ,8, 10, 12])
        name = random.choice(["Tournoi amical du club d'échec de Vitrolles", "Championnats de France d'echecs"])
        location = random.choice(["Vitrolles", "Paris", "Marseilles", "Lyon", "Strasbourg", "Bourg-en-Bresse", "Dunkerque"])
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
            date=tDate, 
            timeControl=timeControl, 
            description=description
        )
    
    @classmethod
    def inputPlayer(cls, playerIndex:int)->Player:
        
        print("Joueur " + str(playerIndex) + " :")
        
        inFirstName = cls.__stringInput("Prénom")
        inLastName = cls.__stringInput("Nom")
        inBirthDay = cls.__dateInput("Anniversaire")
        inGender = cls.__genderInput()
        
        return Player(firstName=inFirstName, lastName=inLastName, birthday=inBirthDay, gender=inGender)

    @classmethod
    def inputTournament(cls)->Tournament:
        roundsCount = cls.__intInput("Nombre de tours")
        playersCount = cls.__intInput("Nombre de joueurs")
        name = cls.__stringInput("Nom du trournoi")
        location = cls.__stringInput("Lieu du tournoi")
        tDate = cls.__dateInput("Date du tournoi")
        timeControl = cls.__timeControlInput()
        description = cls.__stringInput("Descritpion")

        print(" ")

        return Tournament(
            roundsCount=roundsCount, 
            playersCount=playersCount, 
            name=name, 
            location=location, 
            date=tDate, 
            timeControl=timeControl, 
            description=description
        )         
    
    @staticmethod
    def __intInput(message:str)->int:

        inputValue = -1

        while inputValue == -1:

            try:
                inputValue = int(input("    "  + message + " : "))                
            except:
                print("    Erreur dans le format d'entrée. Veuillez renseigner une nombre entier.")

        return inputValue

    @staticmethod
    def __stringInput(message:str)->str:
        return input("    "  + message + " : ")
    
    @staticmethod
    def __dateInput(message:str)->datetime:
        
        dateIn:datetime = None

        while(dateIn == None):
        
            try:
                dateIn = datetime.strptime(input("    " + message + " : "), "%d/%m/%Y")
            except:
                print("    Erreur dans le format de date, veuillez spécifier une date au format jj/mm/aaaa")
   
        return dateIn
    
    @staticmethod
    def __genderInput()->Gender:
        
        genderIn:Gender = None

        while (genderIn == None):
            try:            
                genderValue = int(input("    Genre Homme[0] Femme[1] : "))
                genderIn = Gender(genderValue) 
            except:
                pass
 
        return genderIn

    @staticmethod
    def __timeControlInput()->TimeControl:
        
        timeControl:TimeControl = None

        while (timeControl == None):
            try:            
                timeControl = int(input("    Format de temps Bullet[0] Blitz[1] Rapid[2]: "))
                timeControl = timeControl(timeControl) 
            except:
                pass
 
        return timeControl        