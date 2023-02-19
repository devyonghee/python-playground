from enum import Enum, auto
from typing import Collection, Callable

from lotto.src.model.Money import Money


class Rank(Enum):
    FIRST = (6, Money(2000000000), lambda count: lambda matched_count, is_matched_bonus: matched_count == count)
    SECOND = (5, Money(30000000),
              lambda count: lambda matched_count, is_matched_bonus: matched_count == count and is_matched_bonus)
    THIRD = (5, Money(1500000),
             lambda count: lambda matched_count, is_matched_bonus: matched_count == count and not is_matched_bonus)
    FOURTH = (4, Money(50000), lambda count: lambda matched_count, is_matched_bonus: matched_count == count)
    FIFTH = (3, Money(5000), lambda count: lambda matched_count, is_matched_bonus: matched_count == count)
    MISS = (2, Money(0), lambda count: lambda matched_count, is_matched_bonus: matched_count <= count,)

    def __init__(self,
                 matched_count: int,
                 price: Money,
                 condition_factory: Callable[[int], Callable[[int, bool], bool]]) -> None:
        self.__matched_count = matched_count
        self.__price = price
        self.__condition = condition_factory(matched_count)

    @property
    def price(self) -> Money:
        return self.__price

    @property
    def matched_count(self) -> int:
        return self.__matched_count

    @staticmethod
    def value_of(count: int, is_matched_bonus: bool) -> 'Rank':
        return next(rank for rank in Rank if rank.__condition(count, is_matched_bonus))


class Ranks:

    def __init__(self, ranks: Collection[Rank]):
        if not isinstance(ranks, Collection) \
                or not all(isinstance(rank, Rank) for rank in ranks):
            raise TypeError(f'rank({ranks}) must be {Rank} {Collection} type')
        self.__ranks = ranks

    @property
    def sum_price(self) -> Money:
        return sum([rank.price for rank in self.__ranks], Money(0))

    def count(self, target: Rank) -> int:
        return len([rank for rank in self.__ranks if rank == target])
