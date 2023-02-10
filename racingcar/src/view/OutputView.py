from typing import Sequence

from racingcar.src.model.RacingHistory import RacingHistory
from racingcar.src.model.Track import Track


def print_history_result(racing_history: RacingHistory):
    print("\n실행 결과")
    for tracks in racing_history.history:
        for track in tracks:
            print(f'{track.car.name.value} : {"-" * track.distance.value}')
        print()


def print_winners(tracks: Sequence[Track]):
    print(f'{", ".join(map(lambda track: track.car.name.value, tracks))} 가 최종 우승 했습니다.')
