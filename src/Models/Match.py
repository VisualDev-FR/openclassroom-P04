from Models.player import Player

class Match:
    
    __m_player_1:Player
    __m_player_2:Player
    __m_winner:Player
    
    def __init__(self, player1:Player, player2:Player) -> None:  
        player1.encounter(player2)
        player2.encounter(player1)
        self.__m_player_1 = player1
        self.__m_player_2 = player2

    def setWinner(cls, playerIndex:int):

        if not playerIndex in range(1,2):
            raise ValueError("player index out of bounds, must be 1 or 2.")
            exit()

        cls.__m_winner = (cls.__m_player_1, cls.__m_player_2)[playerIndex == 2]
        cls.__m_winner.increaseScore()
            

    def getWinner(cls)->Player:
        return cls.__m_winner
