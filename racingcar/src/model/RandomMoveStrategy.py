from typing import Type, TypeVar
from racingcar.src.model.MoveStrategy import MoveStrategy
from racingcar.src.model.Movement import Movement
import random

T = TypeVar('T', bound='RandomMoveStrategy')

MAX_RANGE = 10
MOVE_CYCLE_LIMIT = 4


class RandomMoveStrategy(MoveStrategy):
    __instance = None

    def __new__(cls: Type[T]) -> T:
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def movement(self) -> Movement:
        return Movement.GO if self.__is_over_than_move_limit() else Movement.STOP

    @staticmethod
    def __is_over_than_move_limit():
        return MOVE_CYCLE_LIMIT <= random.randrange(MAX_RANGE)
