from Models.tournament import Tournament
from Models.round import Round
from Models.player import Player
import typing


def generateFirstRound(tournament: Tournament) -> Round:
    """ Function allowing to generate the first round of a tournament.
        sort the players by assessement and generate pairs according to the
        swiss tournament rules. """

    sortedPlayers: typing.List[Player] = tournament.getAssessementSortedPlayers()
    newRound = Round(0)

    for i in range(int(len(sortedPlayers) / 2)):

        player1 = sortedPlayers[i]
        player2 = sortedPlayers[i + int(len(sortedPlayers) / 2)]

        newRound.addMatch(player1, player2)

    return newRound


def generateRound(tournament: Tournament, roundIndex: int) -> Round:
    """ Function allowing to generate the next rounds of a tournament.
        sort the players by score and generate pairs according to the
        swiss tournament rules, avoiding the players to encouter more than one time """

    sortedPlayers: typing.List[Player] = tournament.getScoreSortedPlayers()
    newRound = Round(roundIndex)

    for i in range(int(len(sortedPlayers) / 2)):

        player1 = sortedPlayers[i]

        opponentFound: bool = False
        index: int = 0

        while not opponentFound and index < 8:

            player2 = sortedPlayers[(i + int(len(sortedPlayers) / 2) + index) % len(sortedPlayers)]

            if not player1.encountered(player2) and player1 != player2:
                newRound.addMatch(player1, player2)
                break

            index += 1

    return newRound
