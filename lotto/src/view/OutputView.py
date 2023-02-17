from typing import Collection

from lotto.src.model.Lotto import Lotto
from lotto.src.model.Rank import Ranks, Rank


def print_lottos(lottos: Collection[Lotto]):
    for lotto in lottos:
        print(f"[{', '.join([str(number.value) for number in lotto.numbers])}]")


def print_ranks(ranks: Ranks):
    for rank in [Rank.FIFTH, Rank.FOURTH, Rank.THIRD, Rank.SECOND, Rank.FIRST]:
        bonus_ball_text = ", 보너스 볼 일치 " if rank == Rank.SECOND else " "
        print(f'{rank.matched_count}개 일치{bonus_ball_text}({rank.price}원)- {ranks.count(rank)}')


def print_benefit_rate(rate: int):
    print(f'총 수익률은 {rate}입니다.(기준이 1이기 때문에 결과적으로 손해라는 의미임)')
