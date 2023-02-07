import unittest
from unittest import TestCase
from parameterized import parameterized
from racingcar.src.model.CarName import CarName
from racingcar.src.model.RacingCar import RacingCar
from racingcar.src.model.RandomMoveStrategy import RandomMoveStrategy


class TestRacingCar(TestCase):

    def test_create(self):
        self.assertIsNotNone(RacingCar(CarName("test"), RandomMoveStrategy()))

    @parameterized.expand([[CarName("test"), ''], ['', RandomMoveStrategy()]])
    def test_create_invalid_type_thrown_type_error(self, car_name, move_strategy):
        self.assertRaises(TypeError, RacingCar(car_name, move_strategy))


if __name__ == '__main__':
    unittest.main()
