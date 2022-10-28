from Models.player import Player
from Views.appInputs import AppInput

print(" ")

for i in range (1, 9):
    myPlayer:Player = AppInput.randomPlayer(i)
    print(" ")