from Controllers import tournamentManager, playerManager, dbManager
from Views import appView as AppView

runtime = True

while runtime:

    AppView.clearConsole()
    AppView.printSection("MENU PRINCIPAL")

    print("[1] : Créer un nouveau tournoi")
    print("[2] : Créer un nouveau joueur")
    print("[3] : Afficher tous les tournois existant")
    print('[4] : Afficher tous les joueurs par ordre alphabétique')
    print("[5] : Afficher tous les joueurs par classement")
    print("[6] : Modifier le classement d'un joueur")
    print("[7] : Quitter l'application\n")

    AppView.printSection(" ")

    try:

        choice = input()

        AppView.clearConsole()

        if (choice == "1"):
            # open the tournamentFactory
            tournamentManager.createTournament()

        elif choice == "2":
            # open the player factory
            playerManager.createPlayer()

        elif choice == "3":
            # display all tournament registered in the database
            tournamentManager.displayTournaments()

        elif choice == "4":
            # display all players registered in the database, sorted by name
            playerManager.displayAlphabeticalSortedPlayers()

        elif choice == "5":
            # display all players registered in the database, sorted by assessement
            playerManager.displayAssessementSortedPlayers()

        elif choice == "6":
            # player assessement modification
            playerManager.modifyAssessement()

        elif choice == "7":
            # Clear the console and break the runtime
            AppView.clearConsole()

            # exit the application
            runtime = False

        elif choice == "8":
            dbManager.prettifyDatabase()

    except KeyboardInterrupt:
        pass
