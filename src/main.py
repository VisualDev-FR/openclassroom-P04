import random
import Views.appInputs as AppInput
import Views.appView as AppView
import Controllers.RoundFactory as RoundFactory
from Models.tournament import *

print(" ")

tournament:Tournament = AppInput.randomTournament()

for i in range(tournament.getPlayersCount()):
    newPlayer:Player = AppInput.randomPlayer(i)
    newPlayer.setScore(random.choice([0, 2, 4, 6, 8, 10, 12, 14, 16, 18]))
    tournament.addPlayer(newPlayer)

for i in range(tournament.getRoundsCount()):
    nextRound = RoundFactory.generateRound(tournament, i)
    AppView.printRound(nextRound)