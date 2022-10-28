from datetime import datetime
from enum import Enum
from typing import List
from typing_extensions import Self

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
    __m_encouteredPlayers:dict[Self] = None

    def __init__(self, firstName:str, lastName:str, birthday:datetime, gender:Gender) -> None:
        self.__m_firstName = firstName
        self.__m_lastName = lastName
        self.__m_birthDay = birthday
        self.__m_gender = gender
    
    @classmethod
    def deserialize(cls, serializedPlayer:dict) -> Self:
        cls.__m_lastName = serializedPlayer["Nom"]
        cls.__m_firstName = serializedPlayer["Prénom"]
        cls.__m_birthDay = serializedPlayer["Date de naissance"]
        cls.__m_gender = Gender(serializedPlayer["Genre"])
        cls.__m_score = serializedPlayer["Score"]
        cls.__m_assessement = serializedPlayer["Classement"]
        return cls
    
    def getScore(cls):
        return cls.__m_score
    
    def getAssessement(cls):
        return cls.__m_assessement
    
    def encountered(cls, player:Self)->bool:
        return False
    
    def encounter(cls, encounteredPlayer:Self):
        cls.__m_encouteredPlayers.append(encounteredPlayer)
        
    def serialize(cls)->dict:
        
        return {
            "Nom":cls.__m_lastName,
            "Prénom":cls.__m_firstName,
            "Date de naissance":cls.__m_birthDay,
            "Genre":cls.__m_gender.value,
            "Score":cls.__m_score,
            "Classement":cls.__m_assessement
        }