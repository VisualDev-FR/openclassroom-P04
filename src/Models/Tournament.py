from datetime import datetime
from enum import Enum
from typing import List

from Models.match import Match
from Models.round import Round
from Models.player import Player

class TimeControl(Enum):
    BULLET = 1
    BLITZ = 2
    RAPID = 3

class Tournament:

    ROUNDS_COUNT:int = 4            #Count of rounds for one tournament
    PLAYERS_COUNT:int = 8           #Count of players in the tournament
        
    __m_name:str                    #Name of the tournament
    __m_location:str                #Location of the tournament
    __m_date:datetime                  #Date of the tournament
    __m_roundsList:List[Round]      #List of all tournament's rounds
    __m_playersList:List[Player]    #List of the tournament's players
    __m_timecontrol:TimeControl     #Used time control for the tournament
    __m_Description:str             #Description of the tournament

    def __init__(self, timeControl:TimeControl, name:str, ) -> None:
        pass
    

        
