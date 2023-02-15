import unittest
from unittest import TestCase
from parameterized import parameterized

from racingcar.src.model.CarName import CarName
from racingcar.src.model.Distance import Distance
from racingcar.src.model.RacingCar import RacingCar
from racingcar.src.model.RandomMoveStrategy import RandomMoveStrategy
from racingcar.tests.model.test_MoveStrategy import OnlyGoMoveStrategy, OnlyStopMoveStrategy


class TestRacingCar(TestCase):

    def test_create(self):
        self.assertIsNotNone(RacingCar(CarName("test"), RandomMoveStrategy()))

    @parameterized.expand([[CarName("test"), ''], ['', RandomMoveStrategy()]])
    def test_create_invalid_type_raised_type_error(self, car_name, move_strategy):
        self.assertRaises(TypeError, lambda: RacingCar(car_name, move_strategy))

    @parameterized.expand([[OnlyStopMoveStrategy(), Distance(0)], [OnlyGoMoveStrategy(), Distance(1)]])
    def test_moved_distance(self, move_strategy, expected_distance):
        # given
        car = RacingCar(CarName('any'), move_strategy)
        # when & then
        self.assertEqual(expected_distance, car.moved_distance)


ONLY_GO_CAR = RacingCar(CarName('go'), OnlyGoMoveStrategy())
ONLY_STOP_CAR = RacingCar(CarName('stop'), OnlyStopMoveStrategy())

if __name__ == '__main__':
    unittest.main()
