from Models.player import Player
from Models.tournament import Tournament
from Views.appInputs import AppInput

print(" ")

tournament = AppInput.randomTournament()

for i in range (tournament.getPlayersCount()):
    newPlayer = AppInput.randomPlayer(i)
    tournament.addPlayer(newPlayer)
    print(" ")

