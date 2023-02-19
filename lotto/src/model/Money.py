from typing import Union


class Money:

    def __init__(self, value: Union[int, float]):
        self.__validate_value(value)
        self.__value = float(value)

    def __floordiv__(self, other: 'Money') -> int:
        self.__validate_money_type(other)
        return int(self.__value // other.__value)

    def __add__(self, other: 'Money') -> 'Money':
        self.__validate_money_type(other)
        return Money(self.__value + other.__value)

    def __radd__(self, other) -> 'Money':
        return self + other

    def __truediv__(self, other) -> float:
        if isinstance(other, Money):
            return self.__value / other.__value
        raise TypeError(f'unsupported type({other}) to multiple money')

    def __mul__(self, other: Union[int, float, 'Money']) -> 'Money':
        if type(other) is float:
            return Money(self.__value * other)
        if type(other) is int:
            return Money(self.__value * float(other))
        if isinstance(other, Money):
            return Money(self.__value * other.__value)
        raise TypeError(f'not supported type({other}) to multiple money')

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Money) \
            and self.__value == o.__value

    @property
    def value(self) -> float:
        return self.__value

    @staticmethod
    def __validate_money_type(other: 'Money'):
        if not isinstance(other, Money):
            raise TypeError(f'operated money({other}) must be Money type')

    @staticmethod
    def __validate_value(value):
        if type(value) is not int \
                and type(value) is not float:
            raise TypeError(f'money value({value}) must be int or float type')

        if value < 0:
            raise ValueError(f'money value({value}) must not be negative')
