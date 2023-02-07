from racingcar.src.model.MoveStrategy import MoveStrategy
from racingcar.src.model.CarName import CarName
from racingcar.src.model.Movement import Movement


class RacingCar:

    def __init__(self, name: CarName, move_strategy: MoveStrategy) -> None:
        self._validate_type(move_strategy, name)
        self.name = name
        self.move_strategy = move_strategy

    @staticmethod
    def _validate_type(move_strategy, name):
        if not isinstance(name, CarName):
            raise TypeError(f'name({name}) must be CarName type')
        if not isinstance(move_strategy, MoveStrategy):
            raise TypeError(f'move_strategy({move_strategy}) must be MoveStrategy type')

    def movement(self) -> Movement:
        return self.move_strategy.operated_movement()
