from Models.tournament import Tournament, TimeControl
from Models.player import Player
from Models.tournamentBuffer import TournamentBuffer
import Views.appInputs as AppInput
import Views.appView as AppView
import Controllers.roundManager as roundManager
import Controllers.dbManager as database
from Config import tournamentConst, roundConsts
import typing
from Config import config


def print_section_tournament_info():
    AppView.printSection("DEFINITION DU TOURNOI")
    AppView.blankLine()


def print_section_player_choice():
    AppView.printSection("CHOIX DES JOUEURS")
    AppView.blankLine()


def print_section_results():
    AppView.printSection("RESULTATS")
    AppView.blankLine


def print_section_update_assessements():
    AppView.printSection("MISE A JOUR DES CLASSEMENTS")
    AppView.blankLine()


def print_section_end():
    AppView.printSection("FIN")
    AppView.pressAnyKeyToExit()


def choose_players(buffer: TournamentBuffer) -> TournamentBuffer:

    tournament = buffer.tournament

    # read all the Players table in the database
    players = database.getPlayers()

    # display all the players to the user
    AppView.printPlayers(players)

    # players input parsing
    for i in range(buffer.selectedPlayers, tournament.getPlayersCount()):

        # ask to the user to select a player in the displayed list
        playerIndex = AppInput.intInputBetween(0, len(players) - 1, "Joueur " + str(i))

        print("    -> {fullName}\n".format(fullName=players[playerIndex].getFullName()))

        # add that player to the tournament
        tournament.addPlayer(players[playerIndex])
        buffer.selectedPlayers += 1

    buffer.set_players_choosen()


def generate_rounds(buffer: TournamentBuffer):

    tournament = buffer.tournament

    # generation of rounds
    while buffer.roundIndex < tournament.getRoundsCount():

        # we generate the first round, based on the players assessements
        if buffer.roundIndex == 0:
            nextRound = roundManager.generateFirstRound(tournament)
        else:
            nextRound = roundManager.generateRound(tournament, buffer.roundIndex)

        # print the next matchs to play, ex: 'Match 1 : Thomas Menanteau vs Christophe Derenne'
        AppView.printRound(nextRound)

        # parsing of the round results
        for match in nextRound.getMatchs():

            player1: Player = match[0][0]
            player2: Player = match[1][0]

            # ask to the user, the results of the match n
            winner: Player = AppInput.inputWinner(player1, player2)

            if winner is None:
                player1.increaseScore(0.5)
                player2.increaseScore(0.5)
                match[0][1] = 0.5
                match[1][1] = 0.5

            elif winner == player1:
                player1.increaseScore(1)
                match[0][1] = 1

            elif winner == player2:
                player2.increaseScore(1)
                match[1][1] = 1

        # set the the end hour of the round, once all winners have been designated
        nextRound.end()

        # add the round instance to the created tournament
        tournament.addRound(nextRound)
        buffer.roundIndex += 1


def print_results(buffer: TournamentBuffer):

    tournament = buffer.tournament

    for player in tournament.getScoreSortedPlayers():

        playerName: str = player.getFullName()

        print(
            "    " +
            playerName + (" " * (25 - len(playerName))) +
            str(player.getScore()) + " "
        )


def update_assessements(buffer: TournamentBuffer):

    # print all the player scores
    for player in buffer.tournament.getScoreSortedPlayers():
        player.setAssessement(AppInput.intInput("{fullName} ({score})".format(
            fullName=player.getFullName(),
            score=player.getAssessement()
        )))
        database.updatePlayer(player)

    # at the end, we save the created tournament into the database
    database.saveTournament(buffer.tournament)


def createTournament(buffer: TournamentBuffer) -> TournamentBuffer:

    if buffer is None:
        return create_tournament_from_scratch()

    else:
        print_section_tournament_info()
        userWantsToLoadBuffer: bool = AppInput.ask_user_to_load_buffer()
        AppView.clearConsole()

        if userWantsToLoadBuffer:
            return create_tournament_from_buffer(buffer=buffer)

        else:
            return create_tournament_from_scratch()


def create_tournament_from_buffer(buffer: TournamentBuffer) -> TournamentBuffer:

    # print the current section

    print_section_tournament_info()
    buffer.print_tournament_infos()

    tournament: buffer.tournament

    try:

        # players choice
        print_section_player_choice()
        buffer.print_choosen_players()
        if not buffer.playersChoosen:
            choose_players(buffer)

        # rounds specification
        buffer.print_specified_rounds()
        generate_rounds(buffer)

        # print the results of the tournament
        print_section_results()
        print_results(buffer)

        # update the players assessement
        print_section_update_assessements()
        update_assessements(buffer)

    except KeyboardInterrupt:
        # in case of interruption, we return the currentBufffer of the tournament
        return buffer

    # return a null buffer if the tournament was created successfully
    print_section_end()
    return None


def create_tournament_from_scratch() -> TournamentBuffer:

    # ask to the user to give the tournaments inputs
    print_section_tournament_info()
    tournament: Tournament = inputTournament()
    tournamentBuffer: TournamentBuffer = TournamentBuffer(tournament_=tournament)

    try:
        print_section_player_choice()
        choose_players(tournamentBuffer)

        generate_rounds(tournamentBuffer)

        print_section_results()
        print_results(tournamentBuffer)

        print_section_update_assessements()
        update_assessements(tournamentBuffer)

    except KeyboardInterrupt:
        # in case of interruption, we return the currentBufffer of the tournament
        return tournamentBuffer

    # return a null buffer if the tournament was created successfully
    print_section_end()
    return None


def inputTournament() -> Tournament:
    """ function allowing to create a new tournament instance, from the user inputs """

    # ask all necessary data to create one Tournament instance
    roundsCount = config.NB_ROUNDS
    playersCount = config.NB_PLAYERS
    name = AppInput.stringInput("Nom du tournoi")
    location = AppInput.stringInput("Lieu du tournoi")
    tDate = AppInput.dateInput("Date du tournoi")
    timeControl = AppInput.timeControlInput()
    description = AppInput.stringInput("Descritpion")

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


def printAlphaSortedPlayers(serializedTournament: dict):
    """ function allowing to print a list of players sorted by name,
        from a dictionnary of serialized players """

    # deserialize all the players registered in the tournament
    deserializedPlayers = getPlayersFromSerializedTournament(serializedTournament)

    # sort all the players by name
    sortedPlayers = sorted(deserializedPlayers, key=lambda player: player.getFullName(reverse=True))

    # print all the player we just sorted
    AppView.printSection('JOUEURS')
    AppView.printPlayers(sortedPlayers)


def printAssessementSortedPlayers(serializedTournament: dict):
    """ function allowing to print a list of players sorted by assessement,
        from a dictionnary of serialized players """

    # deserialize all the players registered in the tournament
    deserializedPlayers = getPlayersFromSerializedTournament(serializedTournament)

    # sort all the players by name
    sortedPlayers = sorted(deserializedPlayers, key=lambda player: player.getAssessement())

    # print all the player we just sorted
    AppView.printSection('JOUEURS')
    AppView.printPlayers(sortedPlayers)


def printAllTournamentRounds(serializedTournament: dict):
    """ function allowing to print all rounds contained in a tournament,
        from a dictionnary containing one serialized tournament instance """

    serializedRounds: dict = serializedTournament[tournamentConst.ROUNDS_KEY]

    AppView.printSection('ROUNDS')

    for round in serializedRounds.values():

        roundName = round[roundConsts.ROUND_NAME_KEY]
        roundBegin = round[roundConsts.BEGIN_KEY]
        roundEnd = round[roundConsts.END_KEY]
        matchList = round[roundConsts.MATCH_LIST_KEY]

        print(roundName + " :")
        print((" " * 4) + roundConsts.BEGIN_KEY + " : " + roundBegin)
        print((" " * 4) + roundConsts.END_KEY + " : " + roundEnd)

        for i in range(len(matchList)):
            AppView.print_serialized_match(matchList[i], i + 1)

        AppView.blankLine()


def printAllTournamentMatch(serializedTournament: dict):
    """ function allowing to print all matchs contained in a tournament,
        from a dictionnary containing one serialized tournament instance """

    serializedRounds: dict = serializedTournament[tournamentConst.ROUNDS_KEY]

    AppView.printSection('MATCH')

    matchIndex = 1

    for round in serializedRounds.values():
        for match in round[roundConsts.MATCH_LIST_KEY]:
            AppView.print_serialized_match(match, matchIndex)
            matchIndex += 1
    print(" ")


def getPlayersFromSerializedTournament(serializedTournament: dict) -> typing.List[Player]:
    """ function allowing to get all serialized players contained in a tournament,
        from a dictionnary containing one serialized tournament instance  """

    # get the dictionnary of all player registered in the tournament
    serializedPlayers: dict = serializedTournament[tournamentConst.PLAYERS_KEY]

    # return a list containing all deserialized player instances
    return [Player.deserialize(serializedPlayer) for serializedPlayer in serializedPlayers.values()]


def displayTournaments():
    """ main function displaying all tournaments contained into the database,
        and ask the user to choose one tournament, in order to have more details """

    # print the current section name
    AppView.printSection("TOURNOIS")

    # read the database and print all the tournaments registered in the database
    tournaments = database.getTournaments()
    AppView.printTournaments(tournaments)

    # print the end of the section
    AppView.printSection(" ")

    # ask the user to display details about players
    tournamentIndex = input(
        "Séléctionnez un tournoi pour afficher ses détails, ou appuyez sur entrée " +
        "pour revenir au menu principal : "
    )

    # break if the user press enter key, else print the selected player's details
    if tournamentIndex != "":

        selectedTournament: dict = tournaments[int(tournamentIndex)]

        print(selectedTournament[tournamentConst.NAME_KEY] + " : \n")
        print(
            "    " +
            tournamentConst.PLAYERS_COUNT_KEY + " : " +
            str(selectedTournament[tournamentConst.PLAYERS_COUNT_KEY]))

        print(
            "    " +
            tournamentConst.LOCATION_KEY + " : " +
            selectedTournament[tournamentConst.LOCATION_KEY])
        print(
            "    " +
            tournamentConst.ROUNDS_COUNT_KEY + " : " +
            str(selectedTournament[tournamentConst.ROUNDS_COUNT_KEY]))

        print(
            "    " +
            tournamentConst.TIME_CONTROL_KEY + " : " +
            TimeControl(selectedTournament[tournamentConst.TIME_CONTROL_KEY]).name)

        print("    " + tournamentConst.DESCRIPTION_KEY + " : " + selectedTournament[tournamentConst.DESCRIPTION_KEY])
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
