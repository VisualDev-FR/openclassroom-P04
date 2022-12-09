from Models.round import Round
from Models.player import Player
from Models.tournament import tournamentConst
import os


def clearConsole():

    # Run different command, depending on the os
    if os.name == "nt":
        # clear console on windows
        os.system('cls')
    else:
        # clear console on macos, linux
        os.system('clear')


def printSection(sectionName: str):

    SECTION_LENGHT = 70

    print(" ")
    print("-" * SECTION_LENGHT)
    print((" " * int((SECTION_LENGHT - len(sectionName)) / 2)) + sectionName)
    print("-" * SECTION_LENGHT)
    print(" ")


def printRound(round: Round):

    printSection(("Round {index}".format(index=round.getIndex() + 1).upper()))

    roundMatchs: list = round.getMatchs()

    for i in range(len(roundMatchs)):

        player1: Player = roundMatchs[i][0][0]
        player2: Player = roundMatchs[i][1][0]

        print("    Match {index} : {p1} vs {p2}".format(index=i, p1=player1.getFullName(), p2=player2.getFullName()))

    print(" ")


def pressAnyKeyToExit():
    print("Appuyez sur Entrée pour revenir au menu principal.")
    input()


def printPlayers(players: list):

    for i in range(len(players)):

        # cast player to make coding easier
        player: Player = players[i]

        # print the player
        print("    [{index}] : {fullName}".format(index=i, fullName=player.getFullName()))

    blankLine()


def printTournaments(tournaments: dict):

    for i in range(len(tournaments)):

        tournament: str = tournaments[i][tournamentConst.NAME_KEY]
        tDate: str = tournaments[i][tournamentConst.DATE_KEY]

        print("    [{index}] : Le {date} : {fullName}".format(index=i, fullName=tournament, date=tDate))

    blankLine()


def blankLine():
    print(" ")
