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
