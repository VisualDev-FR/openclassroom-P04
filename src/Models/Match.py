from Models.player import Player

class Match:
    
    __m_player_1 = None
    __m_player_2= None
    
    def __init__(self, player1:Player, player2:Player) -> None:
        player1.encounter(player2)
        player2.encounter(player1)