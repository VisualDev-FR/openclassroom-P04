import Views.appInputs as AppInput
import Views.appView as AppView
import Controllers.dbManager as database
from Models.tournament import *
import json

def createPlayer():

    # print the section name
    AppView.printSection("CREATION D'UN JOUEUR")
    
    # parse a new player from the user inputs
    newPlayer:Player = inputPlayer()

    # save the player into the database
    database.savePlayer(newPlayer)

    # diplsay the exit message
    AppView.pressAnyKeyToExit()

def displayPlayers():

    # print the current section name
    AppView.printSection("JOUEURS")

    # read the database and print all the players
    players = database.getPlayers()
    AppView.printPlayers(players)

    # print the end of the section 
    AppView.printSection(" ")

    # ask the user to display details about players
    playerIndex = input("Séléctionnez un joueur pour afficher ses détails, ou appuyez sur entrée pour revenir au menu principal.")

    # break if the user press enter key, else print the selected player's details 
    while playerIndex != "":

        try:
            print(json.dumps(players[int(playerIndex)].serialize(), indent=4))
            playerIndex = input()
        except:
            # catch the wrong inputs
            print("Veuillez spécifier un nombre entre 0 et " + str(len(players)))
            playerIndex = input()

def inputPlayer()->Player:
    
    # ask all the necessary inputs to create one Player instance
    inFirstName = AppInput.stringInput("Prénom")
    inLastName = AppInput.stringInput("Nom")
    inBirthDay = AppInput.dateInput("Anniversaire")
    inGender = AppInput.genderInput()
    inAssessement = AppInput.intInput("Classement")

    AppView.blankLine()
    
    return Player(firstName=inFirstName, lastName=inLastName, birthday=inBirthDay, gender=inGender, assessement=inAssessement)
