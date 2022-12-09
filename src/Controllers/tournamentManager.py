from Models.tournament import *
import Views.appInputs as AppInput
import Views.randomInputs as RandInput
import Views.appView as AppView
import Controllers.roundManager as roundManager
import Controllers.playerManager as playerManager
import Controllers.dbManager as database
import Config.tournamentConst as tournamentConsts
import json, sys
import typing

def createTournament():

    # print the current section
    AppView.printSection("DEFINITION DU TOURNOI")

    # ask to the user to give the tournaments inputs
    tournament:Tournament = inputTournament()

    # print the current section
    AppView.printSection("CHOIX DES JOUEURS")

    # read all the Players table in the database
    players = database.getPlayers()

    print("playersCOunt = " + str(len(players)))

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
        tournament.addRound(nextRound)
        
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

    # at the end, we save the created tournament into the database
    database.saveTournament(tournament)

    # print the current section
    AppView.printSection("FIN")
    AppView.pressAnyKeyToExit()


def inputTournament()->Tournament:
    
    # ask all necessary data to create one Tournament instance
    roundsCount = AppInput.intInput("    Nombre de tours")
    playersCount = 8
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

def printAlphaSortedPlayers(serializedTournament:dict):

    # deserialize all the players registered in the tournament
    deserializedPlayers = getPlayersFromSerializedTournament(serializedTournament)

    # sort all the players by name
    sortedPlayers = sorted(deserializedPlayers, key=lambda player: player.getFullName(reverse=True))

    # print all the player we just sorted
    AppView.printSection('JOUEURS')
    AppView.printPlayers(sortedPlayers)

def printAssessementSortedPlayers(serializedTournament:dict):
    # deserialize all the players registered in the tournament
    deserializedPlayers = getPlayersFromSerializedTournament(serializedTournament)

    # sort all the players by name
    sortedPlayers = sorted(deserializedPlayers, key=lambda player: player.getAssessement())

    # print all the player we just sorted
    AppView.printSection('JOUEURS')
    AppView.printPlayers(sortedPlayers)

def printAllTournamentRounds(serializedTournament:dict):

    serializedRounds: dict = serializedTournament[tournamentConsts.ROUNDS_KEY]

    AppView.printSection('ROUNDS')

    print(json.dumps(serializedRounds, indent=4))

def printAllTournamentMatch(serializedTournament:dict):
    
    serializedRounds: dict = serializedTournament[tournamentConsts.ROUNDS_KEY]

    AppView.printSection('MATCH')

    matchIndex = 1

    for round in serializedRounds.values():
        for match in round.values():
            print("    Match " + str(matchIndex) + " : " + match)
            matchIndex += 1
    print(" ")

def getPlayersFromSerializedTournament(serializedTournament:dict)->typing.List[Player]:

    # get the dictionnary of all player registered in the tournament
    serializedPlayers:dict = serializedTournament[tournamentConsts.PLAYERS_KEY]

    # return a list containing all deserialized player instances
    return [Player.deserialize(serializedPlayer) for serializedPlayer in serializedPlayers.values()]

def displayTournaments():
    # print the current section name
    AppView.printSection("TOURNOIS")

    # read the database and print all the tournaments registered in the database
    tournaments = database.getTournaments()
    AppView.printTournaments(tournaments)

    # print the end of the section 
    AppView.printSection(" ")

    # ask the user to display details about players
    tournamentIndex = input("Séléctionnez un tournoi pour afficher ses détails, ou appuyez sur entrée pour revenir au menu principal : ")

    # break if the user press enter key, else print the selected player's details 
    if tournamentIndex != "":

        selectedTournament:dict = tournaments[int(tournamentIndex)]

        print(selectedTournament[NAME_KEY] + " : \n")
        print("    " + PLAYERS_COUNT_KEY + " : " + str(selectedTournament[PLAYERS_COUNT_KEY]))
        print("    " + LOCATION_KEY + " : " + selectedTournament[LOCATION_KEY])
        print("    " + ROUNDS_COUNT_KEY + " : " + str(selectedTournament[ROUNDS_COUNT_KEY]))
        print("    " + TIME_CONTROL_KEY + " : " + TimeControl(selectedTournament[TIME_CONTROL_KEY]).name)
        print("    " + DESCRIPTION_KEY + " : " + selectedTournament[DESCRIPTION_KEY])
        print(" ")

        print("    [0] : Afficher tous les joueurs par ordre alphabétique")
        print("    [1] : Afficher tous les joueurs par classement")
        print("    [2] : Afficher tous les rounds")
        print("    [3] : Afficher tous les match")

        choiceIndex = AppInput.intInputBetween(0, 3, "\nAction")

        if choiceIndex == 0:
            printAlphaSortedPlayers(selectedTournament)

        elif choiceIndex == 1:
            printAssessementSortedPlayers(selectedTournament)

        elif choiceIndex == 2:
            printAllTournamentRounds(selectedTournament)

        elif choiceIndex == 3:
            printAllTournamentMatch(selectedTournament)

        choiceIndex = input('Appuyez sur entrée pour revenir au menu principal.')
