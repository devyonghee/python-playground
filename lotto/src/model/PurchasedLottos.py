from typing import Collection

from lotto.src.model.Lotto import Lotto
from lotto.src.model.Money import Money
from lotto.src.model.Rank import Ranks
from lotto.src.model.WinnerLotto import WinnerLotto


class PurchasedLottos:

    def __init__(self, lottos: Collection[Lotto], price_per_ticket: Money) -> None:
        self.__validate_lottos(lottos)
        self.__validate_price_per_ticket(price_per_ticket)
        self.__lottos = lottos
        self.__price_per_ticket = price_per_ticket

    @staticmethod
    def __validate_lottos(lottos):
        if not isinstance(lottos, Collection) \
                or not all(isinstance(lotto, Lotto) for lotto in lottos):
            raise TypeError(f'lottos({lottos}) must be {Lotto} {Collection} type')

    @staticmethod
    def __validate_price_per_ticket(price_per_ticket):
        if not isinstance(price_per_ticket, Money):
            raise TypeError(f'price_per_ticket({price_per_ticket}) must be {Money} type')

    @property
    def sum_lottos_price(self) -> Money:
        return self.__price_per_ticket * len(self.__lottos)

    def ranks(self, winner_lotto: WinnerLotto) -> Ranks:
        return winner_lotto.ranks(self.__lottos)

    @property
    def lottos(self) -> Collection[Lotto]:
        return self.__lottos
