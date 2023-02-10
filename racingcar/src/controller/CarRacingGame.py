from racingcar.src.model import CarName
from racingcar.src.model.CarRacingStadium import CarRacingStadium
from racingcar.src.model.RacingCar import RacingCar
from racingcar.src.model.RandomMoveStrategy import RandomMoveStrategy
from racingcar.src.view.InputView import input_car_name, input_cycle_count


def race():
    cars = [RacingCar(name, RandomMoveStrategy()) for name in CarName.separate_names(input_car_name())]
    cycle_count = input_cycle_count()

    history = CarRacingStadium(cars).race_history(cycle_count)
