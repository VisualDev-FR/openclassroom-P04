from datetime import date, datetime
import random
from Models.player import Gender
from Models.player import Player

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
    def inputPlayer(cls, playerIndex:int)->Player:
        
        print("Joueur " + str(playerIndex) + " :")
        
        inFirstName = cls.__stringInput("Prénom")
        inLastName = cls.__stringInput("Nom")
        inBirthDay = cls.__dateInput("Anniversaire")
        inGender = cls.__genderInput()
        
        return Player.create(firstName=inFirstName, lastName=inLastName, birthday=inBirthDay, gender=inGender)
    
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