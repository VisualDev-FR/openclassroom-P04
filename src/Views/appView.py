from Models.round import Round
from Models.player import Player
from Models.tournament import tournamentConst
from Config import roundConsts
import os


def clearConsole():
    """ generic function allowing to clear the console between two actions """

    # Run different command, depending on the os
    if os.name == "nt":
        # clear console on windows
        os.system('cls')
    else:
        # clear console on macos, linux
        os.system('clear')


def printSection(sectionName: str):
    """ Generic function allowing to display a centered section name """

    SECTION_LENGHT = 70

    print(" ")
    print("-" * SECTION_LENGHT)
    print((" " * int((SECTION_LENGHT - len(sectionName)) / 2)) + sectionName)
    print("-" * SECTION_LENGHT)
    print(" ")


def printRound(round: Round):
    """ generic function allowing to print all the matches of a round """

    printSection(("Round {index}".format(index=round.getIndex() + 1).upper()))

    roundMatchs: list = round.getMatchs()

    for i in range(len(roundMatchs)):

        player1: Player = roundMatchs[i][0][0]
        player2: Player = roundMatchs[i][1][0]

        print("    Match {index} : {p1} vs {p2}".format(index=i, p1=player1.getFullName(), p2=player2.getFullName()))

    print(" ")


def pressAnyKeyToExit():
    """ genric function allowing to wait any user input before to continue the program """

    print("Appuyez sur Entrée pour revenir au menu principal.")
    input()


def printPlayers(players: list):
    """ generic function allowing to print a list of players instances right in front of their indexes in the list """

    for i in range(len(players)):

        # cast player to make coding easier
        player: Player = players[i]

        # print the player
        print("    [{index}] : {fullName}".format(index=i, fullName=player.getFullName()))

    blankLine()


def printTournaments(tournaments: dict):
    """ function allowing to print a list of tournament instances, with their indexes in the list """

    for i in range(len(tournaments)):

        tournament: str = tournaments[i][tournamentConst.NAME_KEY]
        tDate: str = tournaments[i][tournamentConst.DATE_KEY]

        print("    [{index}] : Le {date} : {fullName}".format(index=i, fullName=tournament, date=tDate))

    blankLine()


def print_serialized_match(match: tuple, index: int):
    """ generic function allowing to print a match with the next format :

        Match 1 : player1 (score) vs player2 (score) """

    print(
        (" " * 4) + "Match {index} : {p1}({s1}) vs {p2} ({s2})".format(
            index=index,
            p1=match[roundConsts.PLAYER_1_KEY],
            p2=match[roundConsts.PLAYER_2_KEY],
            s1=match[roundConsts.PLAYER_1_SCORE_KEY],
            s2=match[roundConsts.PLAYER_2_SCORE_KEY]
        )
    )


def blankLine():
    """ function allowing to print a blank line into the terminal """
    print(" ")
