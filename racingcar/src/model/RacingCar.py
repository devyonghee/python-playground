from racingcar.src.model.Distance import Distance

from racingcar.src.model.MoveStrategy import MoveStrategy
from racingcar.src.model.CarName import CarName
from racingcar.src.model.Movement import Movement

GO_DISTANCE = Distance(1)
STOP_DISTANCE = Distance(0)


class RacingCar:

    def __init__(self, name: CarName, move_strategy: MoveStrategy) -> None:
        self.__validate_type(name, move_strategy)
        self.__name = name
        self.__move_strategy = move_strategy

    @property
    def name(self) -> CarName:
        return self.__name

    @property
    def moved_distance(self) -> Distance:
        if self.__move_strategy.movement() is Movement.GO:
            return GO_DISTANCE
        return STOP_DISTANCE

    @staticmethod
    def __validate_type(name, move_strategy):
        if not isinstance(name, CarName):
            raise TypeError(f'name({name}) must be CarName type')
        if not isinstance(move_strategy, MoveStrategy):
            raise TypeError(f'move_strategy({move_strategy}) must be MoveStrategy type')

    def __eq__(self, o: object) -> bool:
        return isinstance(o, RacingCar) \
            and self.__name == o.__name \
            and self.__move_strategy == o.__move_strategy
