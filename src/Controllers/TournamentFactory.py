from Models.player import Player
from Models.match import Match
from typing import List

class TournamentFactory:
    
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def generateMatchList(cls, playerList:List[Player])-> List[Match]:
        
        upperPlayers = []
        lowerPlayers = []
        
        matchList:List[Match] = []
        
        for playerIndex in range(0, playerList.count / 2):
            upperPlayer = playerList[playerIndex]
            lowerPlayer = playerList[playerIndex + playerList.count /2]         
            matchList.append(Match(upperPlayer, lowerPlayer))  

        return matchList    