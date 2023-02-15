from typing import Collection

from lotto.src.model.Lotto import Lotto


class LottoMachine:

    def lottos(self, count: int) -> Collection[Lotto]:
        raise AssertionError('must be overridden method')
