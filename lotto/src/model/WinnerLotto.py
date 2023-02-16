from typing import Collection

from lotto.src.model.Lotto import Lotto
from lotto.src.model.LottoNumber import LottoNumber
from lotto.src.model.Rank import Ranks, Rank


class WinnerLotto:

    def __init__(self, lotto: Lotto, bonus: LottoNumber):
        if not isinstance(lotto, Lotto):
            raise TypeError(f'lotto({lotto}) must be {Lotto} type')
        if not isinstance(bonus, LottoNumber):
            raise TypeError(f'bonus({bonus}) must be {LottoNumber} type')
        if bonus in lotto:
            raise ValueError(f'bonus({bonus}) must not be in lotto({lotto})')
        self.__lotto = lotto
        self.__bonus = bonus

    def ranks(self, lottos: Collection[Lotto]) -> Ranks:
        self.__validate_lottos_type(lottos)
        return Ranks([self.__rank(lotto) for lotto in lottos])

    def __rank(self, lotto: Lotto):
        return Rank.value_of(lotto.matched_count(self.__lotto), self.__bonus in lotto)

    @staticmethod
    def __validate_lottos_type(lottos: Collection[Lotto]):
        if not isinstance(lottos, Collection) \
                or not all(isinstance(lotto, Lotto) for lotto in lottos):
            raise TypeError(f'lottos({lottos}) must be {Lotto} {Collection} type')
