from datetime import datetime
from enum import Enum
from typing_extensions import Self
from Config.playerConst import * 
from Config.config import *

class Gender(Enum):
    HOMME = 0
    FEMME = 1
    
class Player:

    __m_firstName:str = ""
    __m_lastName:str = ""
    __m_birthDay:datetime = None
    __m_gender:Gender = None
    __m_assessement:int = 0
    __m_score:int = 0
    __m_encounteredPlayers:dict[Self] = None

    def __init__(self, firstName:str, lastName:str, birthday:datetime, gender:Gender, assessement:int) -> None:
        self.__m_firstName = firstName
        self.__m_lastName = lastName
        self.__m_birthDay = birthday
        self.__m_gender = gender
        self.__m_assessement = assessement
    
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

    def increaseScore(self)->None:
        self.__m_score += 1

    def setScore(cls, newScore:int)->None:
        cls.__m_score = newScore
    
    def getScore(cls)->int:
        return cls.__m_score
    
    def getFullName(cls)->str:
        return "{firstName} {lastName}".format(firstName = cls.__m_firstName, lastName=cls.__m_lastName)
    
    def getFirstName(cls)->str:
        return cls.__m_firstName    

    def getLastName(cls)->str:
        return cls.__m_lastName

    def getAssessement(cls)->int:
        return cls.__m_assessement

    def setAssessement(cls, assessement:int):
        cls.__m_assessement = assessement

    def encountered(cls, player:Self)->bool:
        return cls.__m_encounteredPlayers.__contains__(player)
    
    def encounter(cls, encounteredPlayer:Self):
        cls.__m_encounteredPlayers.append(encounteredPlayer)

    def setAssessement(cls, assessement:int):
        cls.__m_assessement = assessement
        
    def serialize(cls)->dict:

        return {
            LAST_NAME_KEY:cls.__m_lastName,
            FIRST_NAME_KEY:cls.__m_firstName,
            BIRTHDAY_KEY:cls.__m_birthDay.strftime(DATE_FORMAT),
            GENDER_KEY:cls.__m_gender.value,
            SCORE_KEY:cls.__m_score,
            ASSESSEMENT_KEY:cls.__m_assessement
        }