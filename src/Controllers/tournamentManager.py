from Models.tournament import *
import Views.appInputs as AppInput
import Views.randomInputs as RandInput
import Views.appView as AppView
import Controllers.roundManager as roundManager
import Controllers.playerManager as playerManager
import Controllers.dbManager as database
import os

def createTournament():

    # print the current section
    AppView.printSection("DEFINITION DU TOURNOI")

    # ask to the user to give the tournaments inputs
    tournament:Tournament = RandInput.randomTournament()

    # print the current section
    AppView.printSection("CHOIX DES JOUEURS")

    # read all the Players table in the database
    players = database.getPlayers()

    # display all the players to the user
    AppView.printPlayers(players)

    # players input parsing
    for i in range(tournament.getPlayersCount()):

        # ask to the user to select a player in the displayed list
        playerIndex = AppInput.intInputBetween(0, len(players) - 1, "Joueur " + str(i))

        print("    -> {fullName}\n".format(fullName = players[playerIndex].getFullName()))

        # add that player to the tournament
        tournament.addPlayer(players[playerIndex])

    #TODO:generation des pairs du 1er tour

    # rounds generation
    for i in range(tournament.getRoundsCount()):
        
        # generate one round, given the tournament state
        nextRound = roundManager.generateRound(tournament, i)
        
        # print the next matchs to play, ex: 'Match 1 : Thomas Menanteau vs Christophe Derenne' 
        AppView.printRound(nextRound)

        # parsing of the round results    
        for match in nextRound.getMatchs():

            player1:Player = match[0][0]
            player2:Player = match[1][0]

            # ask to the user, the results of the match n
            winner:Player = AppInput.inputWinner(player1, player2)
            winner.increaseScore()
        
        print(" ")

    # print the current section
    AppView.printSection("RESULTATS")

    for player in roundManager.getScoreSortedPlayers(tournament):
        print("    " + player.getFullName() + " " + str(player.getScore()))

    # print the current section
    AppView.printSection("MISE A JOUR DES CLASSEMENTS")

    for player in roundManager.getNameSortedPlayers(tournament):
        player.setAssessement(AppInput.intInput(player.getFullName()))
        database.updatePlayer(player)

    # print the current section
    AppView.printSection("FIN")
    AppView.pressAnyKeyToExit()

def createRandomTournament():

    # print the current section
    AppView.printSection("DEFINITION DU TOURNOI")

    # ask to the user to give the tournaments inputs
    tournament:Tournament = RandInput.randomTournament()

    # print the current section
    AppView.printSection("DEFINITION DES JOUEURS")

    # players input parsing
    for i in range(tournament.getPlayersCount()):

        # ask to the user to give inputs for player i
        newPlayer:Player = RandInput.randomPlayer(i, tournament.getPlayersCount())

        # add that player to the tournament
        tournament.addPlayer(newPlayer)

    #TODO:generation des pairs du 1er tour

    # rounds generation
    for i in range(tournament.getRoundsCount()):
        
        # generate one round, given the tournament state
        nextRound = roundManager.generateRound(tournament, i)
        
        # print the next matchs to play, ex: 'Match 1 : Thomas Menanteau vs Christophe Derenne' 
        AppView.printRound(nextRound)

        # parsing of the round results    
        for match in nextRound.getMatchs():

            player1:Player = match[0][0]
            player2:Player = match[1][0]

            # ask to the user, the results of the match n
            winner:Player = RandInput.randomWinner(player1, player2)
            winner.increaseScore()
        
        print(" ")

    # print the current section
    AppView.printSection("RESULTATS")

    for player in roundManager.getSortedPlayers(tournament):
        print("    " + player.getFullName() + " " + str(player.getScore()))

    # print the current section
    AppView.printSection("FIN")
    AppView.pressAnyKeyToExit()

def inputTournament()->Tournament:
    
    # ask all necessary data to create one Tournament instance
    roundsCount = AppInput.intInput("    Nombre de tours")
    playersCount = AppInput.intInput("    Nombre de joueurs")
    name = AppInput.stringInput("    Nom du trournoi")
    location = AppInput.stringInput("    Lieu du tournoi")
    tDate = AppInput.dateInput("    Date du tournoi")
    timeControl = AppInput.timeControlInput()
    description = AppInput.stringInput("    Descritpion")

    AppView.blankLine()

    return Tournament(
        roundsCount=roundsCount, 
        playersCount=playersCount, 
        name=name, 
        location=location, 
        date=tDate, 
        timeControl=timeControl, 
        description=description
    )         