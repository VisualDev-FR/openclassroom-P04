from Controllers.tournamentManager import  *
from Controllers.playerManager import *
from Views.appView import *
import os

runtime = True

while runtime :

    os.system('cls')

    AppView.printSection("MENU PRINCIPAL")

    print("[1] : Créer un nouveau tournoi")
    print("[2] : Créer un nouveau joueur")    
    print("[3] : Afficher tout les tournois existant")
    print("[4] : Afficher tout les joueurs")
    print("[5] : Quitter l'application\n")

    AppView.printSection(" ")

    choice = input()

    AppView.clearConsole()

    if(choice == "1"):
        # open the tournamentFactory
        createTournament()

    elif choice == "2":
        createPlayer()

    elif choice == "3":
        displayTournaments()

    elif choice == "4":
        displayPlayers()

    elif choice == "5":

        AppView.clearConsole()

        # exit the application
        runtime = False