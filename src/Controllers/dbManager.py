from tinydb import TinyDB, where
from Config import playerConst, config
from Models.player import Player
from Models.tournament import Tournament
from Views import appView
import json
import typing

PLAYERS_TABLE = "PLAYERS"
TOURNAMENT_TABLE = "TOURNAMENT"


def savePlayer(playerToSave: Player):
    """ Allow to save one player instance into the database """

    # database buffer
    db = TinyDB(config.DATABASE_PATH)

    # insert serialized player into the database
    db.table(PLAYERS_TABLE).insert(playerToSave.serialize())


def saveTournament(tournamentToSave: Tournament):
    """ Allow to save one tournament instance into the database """

    # database buffer
    db = TinyDB(config.DATABASE_PATH)

    # insert serialized tournament into the database
    db.table(TOURNAMENT_TABLE).insert(tournamentToSave.serialize())


def getPlayers() -> typing.List[Player]:
    """ return the entire table of players, contained into the database """

    # database buffer
    db = TinyDB(config.DATABASE_PATH)

    # read players table and sort players by last name
    serializedPlayers = sorted(db.table(PLAYERS_TABLE).all(), key=lambda k: k[playerConst.LAST_NAME_KEY])

    # create new array of Players
    players = []

    for player in serializedPlayers:
        # deserialisze all players and add the to the array of Players
        players.append(Player.deserialize(player))

    # return array of players
    return players


def getTournaments() -> dict:
    """ return the entire table of tournaments contained into the database """
    return TinyDB(config.DATABASE_PATH).table(TOURNAMENT_TABLE).all()


def updatePlayer(playerToUpdate: Player):
    """ Remove and replace a specified player into the database, given a player instance """

    # database buffer
    db = TinyDB(config.DATABASE_PATH)

    # remove the player from the database
    db.table(PLAYERS_TABLE).remove(
        (where(playerConst.FIRST_NAME_KEY) == playerToUpdate.getFirstName()) &
        (where(playerConst.LAST_NAME_KEY) == playerToUpdate.getLastName()))

    # add the updated player into the database
    db.table(PLAYERS_TABLE).insert(playerToUpdate.serialize())


def prettifyTournamentDatabase():
    """ debug function, allowing to display the entire tournament database into the terminal """

    db = TinyDB(config.DATABASE_PATH).table(TOURNAMENT_TABLE).all()

    print(json.dumps(db, indent=4))

    appView.pressAnyKeyToExit()


def prettifyPlayerDatabase():
    """ debug function allowing to display the entire players database into the terminal """

    db = TinyDB(config.DATABASE_PATH).table(PLAYERS_TABLE).all()

    print(json.dumps(db, indent=4))

    appView.pressAnyKeyToExit()
