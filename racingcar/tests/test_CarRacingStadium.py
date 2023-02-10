import unittest
from unittest import TestCase
from racingcar.src.model.CarRacingStadium import CarRacingStadium
from racingcar.src.model.Distance import Distance
from racingcar.src.model.RacingHistory import RacingHistory
from racingcar.src.model.Track import Track
from test_RacingCar import ONLY_GO_CAR


class TestCarRacingStadium(TestCase):

    def test_create(self):
        self.assertIsNotNone(CarRacingStadium((ONLY_GO_CAR,)))

    def test_create_invalid_type_raised_type_error(self):
        self.assertRaises(TypeError, lambda: CarRacingStadium(["test"]))

    def test_race_history(self):
        # given
        one_go_car_in_stadium = CarRacingStadium((ONLY_GO_CAR,))
        cycle_count = 3
        # when
        history = one_go_car_in_stadium.race_history(cycle_count)
        # then
        self.assertEqual(RacingHistory([
            [Track(ONLY_GO_CAR, Distance(1))],
            [Track(ONLY_GO_CAR, Distance(2))],
            [Track(ONLY_GO_CAR, Distance(3))]
        ]), history)


if __name__ == '__main__':
    unittest.main()
