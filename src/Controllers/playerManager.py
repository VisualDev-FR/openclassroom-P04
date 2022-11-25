import Views.appInputs as AppInput
import Views.appView as AppView
import Controllers.dbManager as database

from Models.tournament import *

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
    AppView.printPlayers(database.getPlayers())

    # print the end of the section 
    AppView.printSection(" ")

    # display the exit message
    AppView.pressAnyKeyToExit()

def inputPlayer()->Player:
    
    # ask all the necessary inputs to create one Player instance
    inFirstName = AppInput.stringInput("Prénom")
    inLastName = AppInput.stringInput("Nom")
    inBirthDay = AppInput.dateInput("Anniversaire")
    inGender = AppInput.genderInput()
    inAssessement = AppInput.intInput("Classement")

    AppView.blankLine()
    
    return Player(firstName=inFirstName, lastName=inLastName, birthday=inBirthDay, gender=inGender, assessement=inAssessement)
