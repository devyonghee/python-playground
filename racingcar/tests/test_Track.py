from unittest import TestCase

from racingcar.src.model.CarName import CarName
from racingcar.src.model.Distance import Distance
from racingcar.src.model.Track import Track
from test_RacingCar import ONLY_GO_CAR, ONLY_STOP_CAR


class TestTrack(TestCase):

    def test_create(self):
        self.assertIsNotNone(Track(ONLY_GO_CAR))
        self.assertIsNotNone(Track(ONLY_GO_CAR, Distance(10)))

    def test_next_round_track_go_plus_distance(self):
        # given
        zero_distance_track = Track(ONLY_GO_CAR)
        # when & then
        self.assertEqual(Track(ONLY_GO_CAR, Distance(1)), zero_distance_track.next_round_track)

    def test_next_round_track_stop_equal_distance(self):
        # given
        zero_distance_track = Track(ONLY_STOP_CAR)
        # when & then
        self.assertEqual(zero_distance_track, zero_distance_track.next_round_track)
