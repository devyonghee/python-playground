from enum import Enum, auto

from racingcar.src.model.Distance import Distance


class Movement(Enum):
    GO = (Distance(1))
    STOP = (Distance(0))

    def __init__(self, distance: Distance):
        self.__distance = distance

    @property
    def distance(self) -> Distance:
        return self.__distance
