from datetime import datetime
from enum import Enum
from typing_extensions import Self
from Config import playerConst, config


class Gender(Enum):
    HOMME = 0
    FEMME = 1


class Player:

    __m_firstName: str = ""
    __m_lastName: str = ""
    __m_birthDay: datetime = None
    __m_gender: Gender = None
    __m_assessement: int = 0
    __m_score: int = 0
    __m_encounteredPlayers: dict[Self] = None

    def __init__(self, firstName: str, lastName: str, birthday: datetime, gender: Gender, assessement: int) -> None:
        self.__m_firstName = firstName
        self.__m_lastName = lastName
        self.__m_birthDay = birthday
        self.__m_gender = gender
        self.__m_assessement = assessement

    @classmethod
    def deserialize(self, serializedPlayer: dict) -> Self:
        lastName = serializedPlayer[playerConst.LAST_NAME_KEY]
        firstName = serializedPlayer[playerConst.FIRST_NAME_KEY]
        birthDay = datetime.strptime(serializedPlayer[playerConst.BIRTHDAY_KEY], config.DATE_FORMAT)
        gender = Gender[serializedPlayer[playerConst.GENDER_KEY]].value
        assessement = serializedPlayer[playerConst.ASSESSEMENT_KEY]

        return Player(
            firstName=firstName,
            lastName=lastName,
            birthday=birthDay,
            gender=gender,
            assessement=assessement
        )

    def increaseScore(self) -> None:
        self.__m_score += 1

    def setScore(cls, newScore: int) -> None:
        cls.__m_score = newScore

    def getScore(cls) -> int:
        return cls.__m_score

    def getFullName(cls, reverse: bool = True) -> str:
        if reverse:
            return "{lastName} {firstName}".format(firstName=cls.__m_firstName, lastName=cls.__m_lastName)
        else:
            return "{firstName} {lastName}".format(firstName=cls.__m_firstName, lastName=cls.__m_lastName)

    def getFirstName(cls) -> str:
        return cls.__m_firstName

    def getLastName(cls) -> str:
        return cls.__m_lastName

    def getAssessement(cls) -> int:
        return cls.__m_assessement

    def setAssessement(cls, assessement: int):
        cls.__m_assessement = assessement

    def encountered(cls, player: Self) -> bool:
        return cls.__m_encounteredPlayers.__contains__(player)

    def encounter(cls, encounteredPlayer: Self):
        cls.__m_encounteredPlayers.append(encounteredPlayer)

    def serialize(cls) -> dict:

        return {
            playerConst.LAST_NAME_KEY: cls.__m_lastName,
            playerConst.FIRST_NAME_KEY: cls.__m_firstName,
            playerConst.BIRTHDAY_KEY: cls.__m_birthDay.strftime(config.DATE_FORMAT),
            playerConst.GENDER_KEY: Gender(cls.__m_gender).name,
            playerConst.SCORE_KEY: cls.__m_score,
            playerConst.ASSESSEMENT_KEY: cls.__m_assessement
        }
