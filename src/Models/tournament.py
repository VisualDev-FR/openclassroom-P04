from datetime import datetime
from enum import Enum
from Models.round import Round
from Models.player import Player
from Config import tournamentConst, config
import typing


class TimeControl(Enum):
    BULLET = 0
    BLITZ = 1
    RAPID = 2


class Tournament:

    __m_roundsList: typing.List[Round]
    __m_playersList: list
    __m_roundsCount: int
    __m_playersCount: int
    __m_name: str
    __m_location: str
    __m_date: datetime
    __m_timecontrol: TimeControl
    __m_Description: str

    def __init__(
            self,
            roundsCount: int,
            playersCount: int,
            name: str,
            location: str,
            date: datetime,
            timeControl: TimeControl,
            description: str
            ) -> None:

        self.__m_roundsCount = roundsCount
        self.__m_playersCount = playersCount
        self.__m_name = name
        self.__m_location = location
        self.__m_date = date
        self.__m_timecontrol = timeControl
        self.__m_Description = description
        self.__m_playersList = []
        self.__m_roundsList = []

    def getRounds(cls) -> typing.List[Round]:
        return cls.__m_roundsList

    def addPlayer(cls, player: Player) -> None:
        cls.__m_playersList.append(player)

    def getPlayersCount(cls) -> int:
        return cls.__m_playersCount

    def getRoundsCount(cls) -> int:
        return cls.__m_roundsCount

    def addRound(cls, roundToAdd: Round):
        return cls.__m_roundsList.append(roundToAdd)

    def getPlayers(cls) -> int:
        return cls.__m_playersList

    def getDate(cls) -> datetime:
        return cls.__m_date

    def getStrDate(cls) -> str:
        return cls.__m_date.strftime(config.DATE_FORMAT)

    def getName(cls) -> str:
        return cls.__m_name

    def getLocation(cls) -> str:
        return cls.__m_location

    def getStrTimecontrol(cls) -> str:
        return TimeControl(cls.__m_timecontrol).name

    def getDescription(cls) -> str:
        return cls.__m_Description

    def getSerializedRounds(cls) -> dict:

        serializedRounds = {}

        for round in cls.__m_roundsList:
            serializedRounds[round.getName()] = round.serialize()

        return serializedRounds

    def getSerializedPlayers(cls) -> dict:

        serializedPlayers = {}

        for player in cls.__m_playersList:
            serializedPlayers[player.getFullName()] = player.serialize()

        return serializedPlayers

    def serialize(cls) -> dict:

        return {
            tournamentConst.NAME_KEY: cls.__m_name,
            tournamentConst.LOCATION_KEY: cls.__m_location,
            tournamentConst.PLAYERS_COUNT_KEY: cls.__m_playersCount,
            tournamentConst.DATE_KEY: cls.__m_date.strftime(config.DATE_FORMAT),
            tournamentConst.ROUNDS_COUNT_KEY: cls.__m_roundsCount,
            tournamentConst.ROUNDS_KEY: cls.getSerializedRounds(),
            tournamentConst.PLAYERS_KEY: cls.getSerializedPlayers(),
            tournamentConst.TIME_CONTROL_KEY: cls.__m_timecontrol,
            tournamentConst.DESCRIPTION_KEY: cls.__m_Description
        }

    def getAssessementSortedPlayers(cls) -> typing.List[Player]:
        return sorted(cls.__m_playersList, key=lambda player: player.getAssessement())

    def getScoreSortedPlayers(cls) -> typing.List[Player]:
        return sorted(
            cls.__m_playersList, key=lambda player:
            (player.getScore(), -player.getAssessement()), reverse=True)

    def getNameSortedPlayers(cls) -> typing.List[Player]:
        return sorted(cls.__m_playersList, key=lambda player: player.getLastName())
