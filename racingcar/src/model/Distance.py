from typing import TypeVar, Type

DEFAULT_POSITION = 0

T = TypeVar('T', bound='Position')


def distance_argument_value(args, kwargs):
    if args:
        return args[0]
    elif kwargs:
        return kwargs['value']
    else:
        return DEFAULT_POSITION


class Distance:
    _factory: dict = {}

    def __new__(cls: Type[T], *args, **kwargs) -> T:
        distance_value = distance_argument_value(args, kwargs)
        if distance_value not in cls._factory:
            cls._factory[distance_value] = super().__new__(cls)
        return cls._factory[distance_value]

    def __init__(self, value: int = DEFAULT_POSITION):
        self.__validate_type(value)
        self.__validate_zero_or_positive(value)
        self.__value = value

    def __add__(self, other: 'Distance') -> 'Distance':
        return Distance(self.__value + other.__value)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Distance) and self.__value == other.__value

    @staticmethod
    def __validate_type(value):
        if type(value) is not int:
            raise TypeError(f'distance value({value}) must be int type')

    @staticmethod
    def __validate_zero_or_positive(value):
        if value < 0:
            raise ValueError(f'distance({value}) must be zero or positive')
