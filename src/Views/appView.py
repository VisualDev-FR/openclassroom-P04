from Models.round import *
import os
import json

def clearConsole():
    os.system('cls')

def printSection(sectionName:str)->None:

    SECTION_LENGHT = 70

    print(" ")
    print("-" * SECTION_LENGHT)
    print((" " * int((SECTION_LENGHT - len(sectionName)) / 2)) + sectionName)
    print("-" * SECTION_LENGHT)
    print(" ")

def printRound(round:Round)->None:

    printSection(("Round {index}".format(index=round.getIndex() + 1).upper()))

    roundMatchs:list = round.getMatchs()

    for i in range(len(roundMatchs)):

        player1:Player = roundMatchs[i][0][0]
        player2:Player = roundMatchs[i][1][0]

        print("    Match {index} : {p1} vs {p2}".format(index=i, p1=player1.getFullName(), p2=player2.getFullName()))

    print(" ")

def pressAnyKeyToExit():
    print("Appuyez sur Entrée pour revenir au menu principal.")
    input()

def printPlayers(players:list)->None:
    
    for i in range(len(players)):

        # cast player to make coding easier
        player:Player = players[i]

        # print the player
        print("    [{index}] : {fullName}".format(index=i, fullName=player.getFullName()))

    blankLine()

def blankLine():
    print(" ")