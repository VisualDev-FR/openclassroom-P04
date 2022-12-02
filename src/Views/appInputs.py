from datetime import datetime
from Models.player import *
from Models.tournament import *

def intInput(message:str)->int:

    inputValue = -1

    while inputValue == -1:

        try:
            inputValue = int(input(message + " : ")) 
        
        except KeyboardInterrupt:
            exit()
        except:
            print("    Erreur dans le format d'entrée. Veuillez renseigner une nombre entier.")

    return inputValue

def intInputBetween(minValue:int, maxValue:int, message:str)->int:

    inputValue = -1

    while inputValue == -1:

        try:
            inputValue = int(input("    "  + message + " : "))
            
            if not inputValue in range(minValue, maxValue + 1):
                print("    Le nombre spécifié doit être compris entre " + str(minValue) + " et " + str(maxValue))
                inputValue = -1

        except KeyboardInterrupt:
            exit()
        except:
            print("    Erreur dans le format d'entrée. Veuillez renseigner une nombre entier.")

    return inputValue

def stringInput(message:str)->str:
    return input(message + " : ").strip()

def dateInput(message:str)->datetime:
    
    dateIn:datetime = None

    while(dateIn == None):
    
        try:
            dateIn = datetime.strptime(input(message + " : "), DATE_FORMAT)
        except KeyboardInterrupt:
            raise ValueError("Sortie de fonction")
        except:
            print("    Erreur dans le format de date, veuillez spécifier une date au format jj/mm/aaaa")

    return dateIn

def genderInput()->Gender:
    
    genderIn:Gender = None

    while (genderIn == None):
        try:            
            genderValue = int(input("    Genre Homme[0] Femme[1] : "))
            genderIn = Gender(genderValue) 
        except:
            pass

    return genderIn

def timeControlInput()->TimeControl:
        
        timeControl:TimeControl = None

        while (timeControl == None):
            try:            
                timeControl = int(input("    Format de temps Bullet[0] Blitz[1] Rapid[2]: "))
                timeControl = timeControl(timeControl) 
            except:
                pass
 
        return timeControl

def inputWinner(player1:Player, player2:Player)->Player:

    winner:Player = None

    while winner == None:
        winnerIndex = input("    {p1}[0] vs {p2}[1] : vainqueur = ".format(p1=player1.getFullName(), p2=player2.getFullName()))

        if winnerIndex == "0":
            winner = player1
        elif winnerIndex == "1":
            winner = player2
        else:
            print("    Veuillez rentrer un nombre entre 0 et 1 pour désigner le vainqueur.")

    return winner