import random
from typing import Collection, Type

from lotto.src.model.Lotto import Lotto, LOTTO_SIZE
from lotto.src.model.LottoMachine import LottoMachine
from lotto.src.model.LottoNumber import LottoNumber, MIN_NUMBER, MAX_NUMBER


class AutoLottoMachine(LottoMachine):
    __instance = None
    __all_numbers = [LottoNumber(number) for number in range(MIN_NUMBER, MAX_NUMBER + 1)]

    def __new__(cls: Type['AutoLottoMachine']) -> 'AutoLottoMachine':
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def lottos(self, count: int) -> Collection[Lotto]:
        self.__validate_count_type(count)
        self.__validate_negative(count)
        return [Lotto(random.sample(self.__all_numbers, LOTTO_SIZE)) for _ in range(count)]

    @staticmethod
    def __validate_count_type(count):
        if type(count) is not int:
            raise TypeError(f'count must be {int} type')

    @staticmethod
    def __validate_negative(count):
        if count < 0:
            raise ValueError(f'count({count}) must be greater than or equal to 0')
