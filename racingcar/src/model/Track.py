from racingcar.src.model.Distance import Distance

from racingcar.src.model.RacingCar import RacingCar

INIT_DISTANCE = Distance(0)


class Track:

    def __init__(self, car: RacingCar, distance: Distance = INIT_DISTANCE) -> None:
        self.__validate_type(car, distance)
        self.__car = car
        self.__distance = distance

    @property
    def next_round_track(self) -> 'Track':
        return Track(self.__car, self.__distance + self.__car.movement.distance)

    def equal_distance(self, o: 'Track'):
        return self.__distance.__eq__(o.__distance)

    @property
    def car(self) -> RacingCar:
        return self.__car

    @property
    def distance(self) -> Distance:
        return self.__distance

    def __lt__(self, o: 'Track') -> bool:
        self.__validate_operated_type(o)
        return self.__distance.__lt__(o.__distance)

    def __gt__(self, o: 'Track') -> bool:
        self.__validate_operated_type(o)
        return self.__distance.__gt__(o.__distance)

    @staticmethod
    def __validate_type(car, distance):
        if not isinstance(car, RacingCar):
            raise TypeError(f'car({car}) must be RacingCar Type')
        if not isinstance(distance, Distance):
            raise TypeError(f'distance({distance}) must be Distance Type')

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Track) \
            and self.__car == o.__car \
            and self.__distance == o.__distance

    @staticmethod
    def __validate_operated_type(value: 'Track'):
        if not isinstance(value, Track):
            raise TypeError(f'operated track must be track type')
