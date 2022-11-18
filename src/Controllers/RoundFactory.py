from Models.tournament import Tournament
from Models.round import Round

def generateRound(tournament:Tournament, roundIndex:int)->Round:
    
    sortedPlayers:list = getSortedPlayers(tournament)
    newRound = Round(roundIndex)

    for i in range(int(len(sortedPlayers) / 2)):

        player1 = sortedPlayers[i]
        player2 = sortedPlayers[i + int(len(sortedPlayers) / 2)]

        newRound.addMatch(player1, player2)

    return newRound

def getSortedPlayers(tournament:Tournament)->list:
        return  sorted(tournament.getPlayers(), key=lambda player: player.getScore(), reverse=True)