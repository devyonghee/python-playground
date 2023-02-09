from typing import Collection

from racingcar.src.model.RacingCar import RacingCar
from racingcar.src.model.Track import Track

MIN_CYCLE_COUNT = 1


class CarRacingStadium:

    def __init__(self, cars: Collection[RacingCar]) -> None:
        self.__validate_cars_type(cars)
        self.__tracks = tuple(map(lambda car: Track(car), cars))

    def race_history(self, cycle_count: int) -> Collection[Collection[Track]]:
        self.__validate_count(cycle_count)

        current_tracks = self.__tracks
        history: list[Collection[Track]] = []
        for i in range(cycle_count):
            current_tracks: Collection[Track] = [track.next_round_track for track in current_tracks]
            history.append(current_tracks)
        return history

    @staticmethod
    def __validate_count(cycle_count: int):
        if type(cycle_count) is not int:
            raise TypeError(f'cycle_count({cycle_count}) must be int type')
        if cycle_count < MIN_CYCLE_COUNT:
            raise ValueError(f'cycle_count({cycle_count}) must be equal or greater than {MIN_CYCLE_COUNT}')

    @staticmethod
    def __validate_cars_type(cars: Collection[RacingCar]):
        if any(not isinstance(car, RacingCar) for car in cars):
            raise TypeError(f'all cars({cars}) must be RacingCars type')
