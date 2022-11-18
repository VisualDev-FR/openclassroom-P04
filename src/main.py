import random
import Views.appInputs as AppInput
import Views.appView as AppView
import Controllers.RoundFactory as RoundFactory
from Models.tournament import *

print(" ")

# ask to the user to give the tournaments inputs
tournament:Tournament = AppInput.randomTournament()

# players input parsing
for i in range(tournament.getPlayersCount()):

    # ask to the user to give inputs for player i
    newPlayer:Player = AppInput.inputPlayer(i)

    # add that player to the tournament
    tournament.addPlayer(newPlayer)


# generation des pairs du 1er tour


# rounds generation
for i in range(tournament.getRoundsCount() - 1):
    
    # generate one round, given the tournament state
    nextRound = RoundFactory.generateRound(tournament, i)
    
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

for player in RoundFactory.getSortedPlayers(tournament):
    print(player.getFullName() + " " + str(player.getScore()))