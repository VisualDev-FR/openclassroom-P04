from Models.tournament import Tournament
from Views import appView
from Config import roundConsts, config


class TournamentBuffer:

    tournament: Tournament
    playersChoosen: bool = False
    roundsSpecified: bool = False
    roundIndex: int = 0
    selectedPlayers: int = 0

    def __init__(self, tournament_: Tournament) -> None:
        self.tournament = tournament_
        pass

    def set_players_choosen(cls):
        cls.playersChoosen = True

    def set_rounds_specified(cls):
        cls.roundsSpecified = True

    def print_choosen_players(self):

        players = self.tournament.getNameSortedPlayers()

        for i in range(len(players)):

            if players[i] is not None:
                print(
                    "    Joueur {index} : {fullName}".format(index=i, fullName=players[i].getFullName())
                )

        appView.blankLine()

    def print_specified_rounds(self):

        rounds = self.tournament.getRounds()

        for i in range(config.NB_ROUNDS):

            if i >= len(rounds):
                break

            appView.printSection("ROUND " + str(i + 1))

            round = rounds[i]
            roundBegin = round.getStrBeginTime()
            roundEnd = round.getStrEndTime()
            matchList = round.getMatchs()

            print((" " * 4) + roundConsts.BEGIN_KEY + " : " + roundBegin)
            print((" " * 4) + roundConsts.END_KEY + " : " + roundEnd)

            for i in range(len(matchList)):
                round.printMatch(i)

            appView.blankLine()

        appView.blankLine()

    def print_tournament_infos(self):

        print("    Nom du tournoi : " + self.tournament.getName())
        print("    Lieu du tournoi : " + self.tournament.getLocation())
        print("    Date du tournoi : " + self.tournament.getStrDate())
        print("    Format de temps : " + self.tournament.getStrTimecontrol())
        print("    Description : " + self.tournament.getDescription())

        appView.blankLine()
