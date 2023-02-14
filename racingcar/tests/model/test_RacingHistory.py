from unittest import TestCase

from model.test_RacingCar import ONLY_GO_CAR, ONLY_STOP_CAR
from racingcar.src.model.Distance import Distance
from racingcar.src.model.RacingHistory import RacingHistory
from racingcar.src.model.Track import Track


class TestRacingHistory(TestCase):

    def test_last_furthest_tracks(self):
        # given
        zero_distance_track = Track(ONLY_GO_CAR, Distance(0))
        one_distance_track1 = Track(ONLY_STOP_CAR, Distance(1))
        one_distance_track2 = Track(ONLY_STOP_CAR, Distance(1))
        history = RacingHistory([
            (zero_distance_track, one_distance_track1, one_distance_track2),
        ])
        # when
        tracks = history.last_furthest_tracks
        # then
        for track in tracks:
            self.assertIn(track, (one_distance_track1, one_distance_track2))
