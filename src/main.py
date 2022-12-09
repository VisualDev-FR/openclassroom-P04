from Controllers.tournamentManager import  *
from Controllers.playerManager import *
from Views.appView import *

runtime = True

while runtime :

    AppView.clearConsole()    
    AppView.printSection("MENU PRINCIPAL")

    print("[1] : Créer un nouveau tournoi")
    print("[2] : Créer un nouveau joueur") 
    print("[3] : Afficher tous les tournois existant")
    print('[4] : Afficher tous les joueurs par ordre alphabétique')
    print("[5] : Afficher tous les joueurs par classement")   
    print("[6] : Quitter l'application\n")

    AppView.printSection(" ")

    choice = input()

    AppView.clearConsole()

    if(choice == "1"):
        # open the tournamentFactory
        createTournament()

    elif choice == "2":
        # open the player factory
        createPlayer()

    elif choice == "3":
        # display all tournament registered in the database
        displayTournaments()

    elif choice == "4":
        # display all players registered in the database, sorted by name
        displayAlphabeticalSortedPlayers()

    elif choice == "5":
        # display all players registered in the database, sorted by assessement
        displayAssessementSortedPlayers()

    elif choice == "6":
        # Clear the console and break the runtime
        AppView.clearConsole()

        # exit the application
        runtime = False