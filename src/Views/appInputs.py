from datetime import date, datetime
from Models.player import Gender
from Models.player import Player

class AppInput:
    
    @classmethod
    def inputPlayer(cls, playerIndex:int)->Player:
        
        print("Joueur " + str(playerIndex) + " :")
        
        inFirstName = cls.__stringInput("Prénom")
        inLastName = cls.__stringInput("Nom")
        inBirthDay = cls.__dateInput("Anniversaire")
        inGender = cls.__genderInput()
        
        return Player(firstName=inFirstName, lastName=inLastName, birthday=inBirthDay, gender=inGender)
    
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
                genderValue = int(input("    Genre Homme[0] Femme[1] N/A[2]: "))
                genderIn = Gender(genderValue) 
            except:
                pass
 
        return genderIn