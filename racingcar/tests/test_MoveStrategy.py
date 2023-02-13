from racingcar.src.model.MoveStrategy import MoveStrategy
from racingcar.src.model.Movement import Movement


class OnlyGoMoveStrategy(MoveStrategy):
    def movement(self) -> Movement:
        return Movement.GO


class OnlyStopMoveStrategy(MoveStrategy):
    def movement(self) -> Movement:
        return Movement.STOP
