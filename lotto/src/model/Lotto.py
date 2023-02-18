from typing import Collection

from lotto.src.model.LottoNumber import LottoNumber

LOTTO_SIZE = 6


class Lotto:

    def __init__(self, numbers: Collection[LottoNumber]):
        self.__validate_numbers(numbers)
        self.__numbers = numbers

    @staticmethod
    def __validate_numbers(numbers):
        Lotto.__validate_size(numbers)
        Lotto.__validate_duplicate(numbers)

    @staticmethod
    def __validate_size(numbers):
        if len(numbers) is not LOTTO_SIZE:
            raise ValueError(f'numbers({numbers}) size must be {LOTTO_SIZE}')

    @staticmethod
    def __validate_duplicate(numbers):
        if len(set(numbers)) is not len(numbers):
            raise ValueError(f'numbers({numbers}) must not have duplicate values')

    @property
    def numbers(self) -> Collection[LottoNumber]:
        return self.__numbers

    def matched_count(self, lotto: 'Lotto') -> int:
        self.__validate_lotto_type(lotto)
        return len(set(self.__numbers) & set(lotto.__numbers))

    def __contains__(self, number: LottoNumber) -> bool:
        if not isinstance(number, LottoNumber):
            raise TypeError(f'number({number}) must be {LottoNumber} type')
        return number in self.__numbers

    @staticmethod
    def __validate_lotto_type(lotto):
        if not isinstance(lotto, Lotto):
            raise TypeError(f'lotto({lotto}) must be {Lotto} type')
