from datetime import date
from enum import Enum
from typing import List
from typing_extensions import Self

class Gender(Enum):
    MALE = 0
    FEMALE = 1
    NOT_DEFINED = 2
    
class Player:
    
    __m_firstName:str
    __m_lastName:str
    __m_birthDay:date
    __m_gender:Gender
    __m_assessement:int
    __m_score:int
    __m_index:int
    __m_encouteredPlayers:List[Self]
    
    def __init__(self, firstName:str, lastName:str, birthday:date, gender:Gender) -> None:
        self.__m_firstName = firstName
        self.__m_lastName = lastName
        self.__m_birthDay = birthday
        self.__m_gender = gender
    
    def getScore(cls):
        return cls.__m_score
    
    def getAssessement(cls):
        return cls.__m_assessement
    
    def encountered(cls, player:Self)->bool:
        return False
    
    def encounter(cls, encounteredPlayer:Self):
        cls.__m_encouteredPlayers.append(encounteredPlayer)