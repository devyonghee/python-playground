from typing import Collection

from lotto.src.model.Lotto import Lotto
from lotto.src.model.LottoMachine import LottoMachine
from lotto.src.model.Money import Money
from lotto.src.model.PurchasedLottos import PurchasedLottos

LOTTO_PRICE = Money(1000)


class LottoStore:

    def __init__(self, lotto_machine: LottoMachine):
        if not isinstance(lotto_machine, LottoMachine):
            raise TypeError(f'lotto_generator({lotto_machine}) must be {LottoMachine}')
        self.__lotto_generator = lotto_machine

    def purchased_lottos(self, received_money: Money) -> PurchasedLottos:
        self.__validate_money(received_money)
        purchased_count = received_money // LOTTO_PRICE
        return PurchasedLottos(self.__lotto_generator.lottos(purchased_count), LOTTO_PRICE)

    @staticmethod
    def __validate_money(received_money):
        if not isinstance(received_money, Money):
            raise TypeError(f'received_money({received_money}) must be {Money} type')
