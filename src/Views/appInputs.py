from datetime import datetime
from Models.player import Player, Gender
from Models.tournament import TimeControl
from Config import config


def intInput(message: str, indent: int = 4) -> int:
    """ generic function allowing to ask the user to give one integer value
        and return the answer if the format is good """

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
    """ generic function allowing to ask the user to give one integer, between two values
        and return the given value if the format is good and if it is contained in the good
        specified values """

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
    """ Generic function allowing to ask a string to the user and return the given
    string without spaces at the begin / at the end  """

    return input((" " * indent) + message + " : ").strip()


def dateInput(message: str, indent: int = 4) -> datetime:
    """ generic function allowing to ask a date to the user, and retunr a datetime object if the format is good """

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
    """ generic function allowing to ask a gender to the user. Return a gender value
        if the format of the given answer is good """

    genderIn: Gender = None

    while (genderIn is None):
        try:
            genderValue = int(input((" " * indent) + "Genre Homme[0] Femme[1] : "))
            genderIn = Gender(genderValue)

        except Exception:
            pass

    return genderIn


def timeControlInput(indent: int = 4) -> TimeControl:
    """ generic function allowing to the user to choose a correct timecontrol """

    timeControl: TimeControl = None

    while (timeControl is None):
        try:
            timeControl = int(input((" " * indent) + "Format de temps Bullet[0] Blitz[1] Rapid[2]: "))
            timeControl = timeControl(timeControl)
        except Exception:
            pass

    return timeControl


def inputWinner(player1: Player, player2: Player, indent: int = 4) -> Player:
    """ generic function allowing to the user to designate a winner between two players or a tie.
        return the instance of the winner, or null in case of tie """

    winner: Player = None

    while True:
        winnerIndex = input(
            (" " * indent) + "{p1}[0] vs {p2}[1] (égalité = [2]): vainqueur = "
            .format(p1=player1.getFullName(), p2=player2.getFullName())
        )

        if winnerIndex == "0":
            winner = player1
            break
        elif winnerIndex == "1":
            winner = player2
            break
        elif winnerIndex == "2":
            break
        else:
            print(
                (" " * indent) + "Veuillez rentrer un nombre entre 0 et 2 pour désigner le vainqueur."
            )

    return winner
