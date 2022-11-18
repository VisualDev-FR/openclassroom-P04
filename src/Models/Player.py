from datetime import datetime
from enum import Enum
from typing_extensions import Self

FIRST_NAME_KEY = "PRENOM"
LAST_NAME_KEY = "NOM"
BIRTHDAY_KEY = "DATE_DE_NAISSANCE"
GENDER_KEY = "GENRE"
SCORE_KEY = "SCORE"
ASSESSEMENT_KEY = "CLASSEMENT"  

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

    def __init__(self, firstName:str, lastName:str, birthday:datetime, gender:Gender) -> None:
        self.__m_firstName = firstName
        self.__m_lastName = lastName
        self.__m_birthDay = birthday
        self.__m_gender = gender
    
    @classmethod
    #TODO: créer des constantes pour les clés de dictonnaire
    def deserialize(self, serializedPlayer:dict) -> Self:
        self.__m_lastName = serializedPlayer[LAST_NAME_KEY]
        self.__m_firstName = serializedPlayer[FIRST_NAME_KEY]
        self.__m_birthDay = serializedPlayer[BIRTHDAY_KEY]
        self.__m_gender = Gender(serializedPlayer[GENDER_KEY])
        self.__m_score = serializedPlayer[SCORE_KEY]
        self.__m_assessement = serializedPlayer[ASSESSEMENT_KEY]
        return self

    def increaseScore(self):
        self.__m_score += 1
    
    def getScore(cls):
        return cls.__m_score
    
    def getAssessement(cls):
        return cls.__m_assessement

    def encountered(cls, player:Self)->bool:
        return cls.__m_encounteredPlayers.__contains__(player)
    
    def encounter(cls, encounteredPlayer:Self):
        cls.__m_encounteredPlayers.append(encounteredPlayer)
        
    def serialize(cls)->dict:
        
        return {
            LAST_NAME_KEY:cls.__m_lastName,
            FIRST_NAME_KEY:cls.__m_firstName,
            BIRTHDAY_KEY:cls.__m_birthDay,
            GENDER_KEY:cls.__m_gender.value,
            SCORE_KEY:cls.__m_score,
            ASSESSEMENT_KEY:cls.__m_assessement
        }