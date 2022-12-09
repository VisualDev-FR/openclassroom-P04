from Models.tournament import Tournament
from Models.round import Round
from Models.player import Player
import typing


def generateFirstRound(tournament: Tournament) -> Round:

    sortedPlayers: typing.List[Player] = tournament.getAssessementSortedPlayers()
    newRound = Round(0)

    for i in range(int(len(sortedPlayers) / 2)):

        player1 = sortedPlayers[i]
        player2 = sortedPlayers[i + int(len(sortedPlayers) / 2)]

        newRound.addMatch(player1, player2)

    return newRound


def generateRound(tournament: Tournament, roundIndex: int) -> Round:

    sortedPlayers: typing.List[Player] = tournament.getScoreSortedPlayers()
    newRound = Round(roundIndex)

    for i in range(int(len(sortedPlayers) / 2)):

        player1 = sortedPlayers[i]
        player2 = sortedPlayers[i + int(len(sortedPlayers) / 2)]

        newRound.addMatch(player1, player2)

    return newRound
