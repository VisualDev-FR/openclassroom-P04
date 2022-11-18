from Models.round import *

def printRound(round:Round)->None:

    print("Round {index}".format(index=round.getIndex()))

    roundMatchs:list = round.getMatchs()

    for i in range(len(roundMatchs)):

        player1:Player = roundMatchs[i][0][0]
        player2:Player = roundMatchs[i][1][0]

        print("    Match {index} : {p1} vs {p2}".format(index=i, p1=player1.getFullName(), p2=player2.getFullName()))

    print(" ")