from datetime import datetime
from Models.player import Player
from Config import config


class Round:

    __m_matchList: list
    __m_name: str
    __m_index: int
    __m_begin: datetime
    __m_end: datetime

    def __init__(self, index: int) -> None:
        self.__m_matchList = []
        self.__m_name = "Round {i}".format(i=index)
        self.__m_index = index
        self.__m_begin = datetime.now()
        self.__m_end = None

    def end(cls) -> None:
        # print("------------------------------------------------EEEEEEEEEEEEEEEEEEEEEEEEND")
        cls.__m_end = datetime.now()

    def getIndex(cls) -> int:
        return cls.__m_index

    def getName(cls) -> str:
        return cls.__m_name

    def addMatch(cls, player1: Player, player2: Player) -> None:
        cls.__m_matchList.append(
            (
                [player1, player1.getScore],
                [player2, player2.getScore]
            )
        )

    def getMatchs(cls) -> list:
        return cls.__m_matchList

    def getEndTime(cls) -> datetime:
        return cls.__m_end

    def serialize(cls) -> dict:

        serializedRound = {
            "Debut": datetime.strftime(cls.__m_begin, config.HOUR_FORMAT),
            "Fin": datetime.strftime(cls.__m_end, config.HOUR_FORMAT)
        }

        for i in range(len(cls.__m_matchList)):

            player1: Player = cls.__m_matchList[i][0][0]
            player2: Player = cls.__m_matchList[i][1][0]

            serializedRound["Match " + str(i)] = player1.getFullName() + " vs " + player2.getFullName()

        return serializedRound
