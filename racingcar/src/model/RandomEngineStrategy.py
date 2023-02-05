from typing import Type, TypeVar
from racingcar.src.model.EngineStrategy import MoveStrategy
from racingcar.src.model.Movement import Movement
import random

T = TypeVar('T', bound='RandomMoveStrategy')

MAX_RANGE = 10
MOVE_CYCLE_LIMIT = 4


def is_over_than_move_limit() -> bool:
    return MOVE_CYCLE_LIMIT <= random.randrange(MAX_RANGE)


class RandomEngineStrategy(MoveStrategy):
    _instance = None

    def __new__(cls: Type[T]) -> T:
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def operated_movement(self) -> Movement:
        return Movement.GO if is_over_than_move_limit() else Movement.STOP
