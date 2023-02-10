from typing import Sequence

from racingcar.src.model.Track import Track


class RacingHistory:

    def __init__(self, history: Sequence[Sequence[Track]]) -> None:
        if not len(history):
            raise ValueError('history must not be empty')
        self.__history = [*history]

    @property
    def last_furthest_tracks(self) -> Sequence[Track]:
        furthest_track = None
        furthest_tracks = []
        for track in self.last_tracks():
            if furthest_track is None or furthest_track < track:
                furthest_track = track
                furthest_tracks = [furthest_track]
                continue
            if furthest_track.equal_distance(track):
                furthest_tracks.append(track)
        return furthest_tracks

    def last_tracks(self) -> Sequence[Track]:
        return self.__history[-1]

    @property
    def history(self) -> Sequence[Sequence[Track]]:
        return [*self.__history]

    def __eq__(self, o: object) -> bool:
        return isinstance(o, RacingHistory) \
            and self.__history == o.__history
