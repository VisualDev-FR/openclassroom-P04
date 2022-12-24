from datetime import datetime
from Models.player import Player
from Config import config, roundConsts


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
        """ method used to set the end of the tournament."""
        cls.__m_end = datetime.now()

    def getIndex(cls) -> int:
        return cls.__m_index

    def getName(cls) -> str:
        return cls.__m_name

    def addMatch(cls, player1: Player, player2: Player) -> None:
        player1.encounter(player2)
        cls.__m_matchList.append(
            (
                [player1, 0],
                [player2, 0]
            )
        )

    def getMatchs(cls) -> list:
        return cls.__m_matchList

    def getEndTime(cls) -> datetime:
        return cls.__m_end

    def serializeMatch(cls, match: tuple) -> dict:

        p1: Player = match[0][0]
        p2: Player = match[1][0]

        p1_score: int = match[0][1]
        p2_score: int = match[1][1]

        serializedMatch = {
            roundConsts.PLAYER_1_KEY: p1.getFullName(),
            roundConsts.PLAYER_2_KEY: p2.getFullName(),
            roundConsts.PLAYER_1_SCORE_KEY: p1_score,
            roundConsts.PLAYER_2_SCORE_KEY: p2_score
        }

        return serializedMatch

    def serialize(cls) -> dict:

        matchList = []

        # serialize all matches of the current instance
        for i in range(len(cls.__m_matchList)):
            matchList.append(cls.serializeMatch(cls.__m_matchList[i]))

        # serialize the current instance of the round
        serializedRound = {
            roundConsts.ROUND_NAME_KEY: cls.__m_name,
            roundConsts.BEGIN_KEY: datetime.strftime(cls.__m_begin, config.HOUR_FORMAT),
            roundConsts.END_KEY: datetime.strftime(cls.__m_end, config.HOUR_FORMAT),
            roundConsts.MATCH_LIST_KEY: matchList
        }

        return serializedRound
