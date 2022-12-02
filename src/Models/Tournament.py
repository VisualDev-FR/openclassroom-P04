from datetime import datetime
from enum import Enum
from Models.round import *
from Models.player import *
from Config.tournamentConst import *

class TimeControl(Enum):
    BULLET = 0
    BLITZ = 1
    RAPID = 2

class Tournament:

    __m_roundsList:list      #List of all tournament's rounds
    __m_playersList:list    #List of the tournament's players

    __m_roundsCount:int             #Number of rounds played in the tournament
    __m_playersCount:int            #Number of players participating to the tournament
    __m_name:str                    #Name of the tournament
    __m_location:str                #Location of the tournament
    __m_date:datetime               #Date of the tournament
    __m_timecontrol:TimeControl     #Used time control for the tournament
    __m_Description:str             #Description of the tournament

    def __init__(self, roundsCount:int, playersCount:int, name:str, location:str, date:datetime, timeControl:TimeControl, description:str) -> None:
        self.__m_roundsCount = roundsCount
        self.__m_playersCount = playersCount
        self.__m_name = name
        self.__m_location = location
        self.__m_date = date
        self.__m_timecontrol = timeControl
        self.__m_Description = description 

        self.__m_playersList = []
        self.__m_roundsList = []

    def addPlayer(cls, player:Player)->None:
        cls.__m_playersList.append(player)

    def getPlayersCount(cls)->int:
        return cls.__m_playersCount

    def getRoundsCount(cls)->int:
        return cls.__m_roundsCount

    def addRound(cls, roundToAdd:Round):
        return cls.__m_roundsList.append(roundToAdd)

    def getPlayers(cls)->int:
        return cls.__m_playersList

    def getSerializedRounds(cls)->dict:
        
        serializedRounds = {}

        for round in cls.__m_roundsList:
            serializedRounds[round.getName()] = round.serialize()
        
        return serializedRounds

    def getSerializedPlayers(cls)->dict:
        
        serializedPlayers = {}

        for player in cls.__m_playersList:
            serializedPlayers[player.getFullName()] = player.serialize()
        
        return serializedPlayers

    def serialize(cls)->dict:

        return {
            NAME_KEY:cls.__m_name,
            LOCATION_KEY:cls.__m_location,
            DATE_KEY:cls.__m_date.strftime(DATE_FORMAT),
            ROUNDS_COUNT_KEY:cls.__m_roundsCount,
            ROUNDS_KEY:cls.getSerializedRounds(),
            PLAYERS_KEY:cls.getSerializedPlayers(),
            TIME_CONTROL_KEY:cls.__m_timecontrol,
            DESCRIPTION_KEY:cls.__m_Description
        }        

    @classmethod
    #TODO: créer des constantes pour les clés de dictonnaire
    def deserialize(self, serializedPlayer:dict) -> Self:
        lastName = serializedPlayer[LAST_NAME_KEY]
        firstName = serializedPlayer[FIRST_NAME_KEY]
        birthDay = serializedPlayer[BIRTHDAY_KEY]
        gender = Gender(serializedPlayer[GENDER_KEY])
        assessement = serializedPlayer[ASSESSEMENT_KEY]
        
        return Player(
            firstName = firstName,
            lastName = lastName,
            birthday = birthDay,
            gender = gender,
            assessement = assessement
        )        
