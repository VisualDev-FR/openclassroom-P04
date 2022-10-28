from Models.player import Player
from Views.appInputs import AppInput

print(" ")

for i in range (1, 8):
    myPlayer:Player = AppInput.inputPlayer(i)
    print(" ")