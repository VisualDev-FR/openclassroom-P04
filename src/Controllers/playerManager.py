import Views.appInputs as AppInput
import Views.appView as AppView
import Controllers.dbManager as database
from Models.player import Player
import json


def createPlayer():
    """ Main function allowing to create a player and to save it into the database """

    # print the section name
    AppView.printSection("CREATION D'UN JOUEUR")

    # parse a new player from the user inputs
    newPlayer: Player = inputPlayer()

    # save the player into the database
    database.savePlayer(newPlayer)

    # diplsay the exit message
    AppView.pressAnyKeyToExit()


def displayPlayers(players):
    """ Allow to display all players given a player list, and ask the user to select one player
        in order to have more details.
     """

    # print the current section name
    AppView.printSection("JOUEURS")

    # print all players
    AppView.printPlayers(players)

    # print the end of the section
    AppView.printSection(" ")

    # ask the user to display details about players
    playerIndex = input(
        "Séléctionnez un joueur pour afficher ses détails, " +
        "ou appuyez sur entrée pour revenir au menu principal : ")

    # break if the user press enter key, else print the selected player's details
    while playerIndex != "":

        try:
            print(json.dumps(players[int(playerIndex)].serialize(), indent=4))
            playerIndex = input(
                "Séléctionnez un joueur pour afficher ses détails, " +
                "ou appuyez sur entrée pour revenir au menu principal : ")
        except Exception:
            # catch the wrong inputs
            playerIndex = input("Veuillez spécifier un nombre entre 0 et " + str(len(players)))


def displayAlphabeticalSortedPlayers():
    """ get all the players contained in the database, sort them by name and display them """

    # read the database
    players = sorted(database.getPlayers(), key=lambda player: player.getFullName(reverse=True))

    # Display the sorted players
    displayPlayers(players)


def displayAssessementSortedPlayers():
    """ get all the players contained in the database, sort them by assessement and display them """

    # read the database
    players = sorted(database.getPlayers(), key=lambda player: player.getAssessement())

    # Display the sorted players
    displayPlayers(players)


def inputPlayer() -> Player:
    """ Standard function allowing to create a player from user inputs, and return a new instance of player """

    # ask all the necessary inputs to create one Player instance
    inFirstName = AppInput.stringInput("Prénom")
    inLastName = AppInput.stringInput("Nom")
    inBirthDay = AppInput.dateInput("Anniversaire")
    inGender = AppInput.genderInput()
    inAssessement = AppInput.intInput("Classement")

    AppView.blankLine()

    return Player(
        firstName=inFirstName,
        lastName=inLastName,
        birthday=inBirthDay,
        gender=inGender,
        assessement=inAssessement
        )


def modifyAssessement():
    """ Function allowing to modify the assessement of a player. Displays the actual assessment,
    ask the new assessement to the user, and update the player into the database """

    # read database
    players = sorted(database.getPlayers(), key=lambda player: player.getAssessement())

    # print the current section name
    AppView.printSection("JOUEURS")

    # print all players
    AppView.printPlayers(players)

    # print the end of the section
    AppView.printSection(" ")

    # ask the user to display details about players
    playerIndex = input(
        "Séléctionnez un joueur pour modifier son classement, " +
        "ou appuyez sur entrée pour revenir au menu principal : ")

    # break if the user press enter key, else print the selected player's details
    while playerIndex != "":

        try:

            player: Player = players[int(playerIndex)]
            player.setAssessement(AppInput.intInput(
                "{fullName} ({assessement})".format(
                    fullName=player.getFullName(),
                    assessement=player.getAssessement())
                )
            )
            database.updatePlayer(player)

            playerIndex = input(
                "Séléctionnez un joueur pour modifier son classement, " +
                "ou appuyez sur entrée pour revenir au menu principal : ")
        except Exception:
            # catch the wrong inputs
            playerIndex = input("Veuillez spécifier un nombre entre 0 et " + str(len(players)))
