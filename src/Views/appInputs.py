from datetime import datetime
from Models.player import Player, Gender
from Models.tournament import TimeControl
from Config import config


def intInput(message: str, indent: int = 4) -> int:

    inputValue = -1

    while inputValue == -1:

        try:
            inputValue = int(input((" " * indent) + message + " : "))

        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception:
            print((" " * indent) + "Erreur dans le format d'entrée. Veuillez renseigner une nombre entier.")

    return inputValue


def intInputBetween(minValue: int, maxValue: int, message: str, indent: int = 4) -> int:

    inputValue = -1

    while inputValue == -1:

        try:
            inputValue = int(input((" " * indent) + message + " : "))

            if inputValue not in range(minValue, maxValue + 1):
                print(
                    (" " * indent) +
                    "Le nombre spécifié doit être compris entre " +
                    str(minValue) + " et " + str(maxValue)
                )
                inputValue = -1

        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception:
            print((" " * indent) + "Erreur dans le format d'entrée. Veuillez renseigner une nombre entier.")

    return inputValue


def stringInput(message: str, indent: int = 4) -> str:
    return input((" " * indent) + message + " : ").strip()


def dateInput(message: str, indent: int = 4) -> datetime:

    dateIn: datetime = None

    while (dateIn is None):

        try:
            dateIn = datetime.strptime(input((" " * indent) + message + " : "), config.DATE_FORMAT)
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception:
            print((" " * indent) + "Erreur dans le format de date, veuillez spécifier une date au format jj/mm/aaaa")

    return dateIn


def genderInput(indent: int = 4) -> Gender:

    genderIn: Gender = None

    while (genderIn is None):
        try:
            genderValue = int(input((" " * indent) + "Genre Homme[0] Femme[1] : "))
            genderIn = Gender(genderValue)

        except Exception:
            pass

    return genderIn


def timeControlInput(indent: int = 4) -> TimeControl:

    timeControl: TimeControl = None

    while (timeControl is None):
        try:
            timeControl = int(input((" " * indent) + "Format de temps Bullet[0] Blitz[1] Rapid[2]: "))
            timeControl = timeControl(timeControl)
        except Exception:
            pass

    return timeControl


def inputWinner(player1: Player, player2: Player, indent: int = 4) -> Player:

    winner: Player = None

    while (winner is None):
        winnerIndex = input(
            (" " * indent) + "{p1}[0] vs {p2}[1] : vainqueur = "
            .format(p1=player1.getFullName(), p2=player2.getFullName())
        )

        if winnerIndex == "0":
            winner = player1
        elif winnerIndex == "1":
            winner = player2
        else:
            print((" " * indent) + "Veuillez rentrer un nombre entre 0 et 1 pour désigner le vainqueur.")

    return winner
