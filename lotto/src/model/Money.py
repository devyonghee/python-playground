class Money:

    def __init__(self, value: int):
        self.__validate_value(value)
        self.__value = value

    def __floordiv__(self, other: 'Money') -> int:
        if not isinstance(other, Money):
            raise TypeError(f'operated money({other}) must be Money type')
        return self.__value // other.__value

    @staticmethod
    def __validate_value(value):
        if type(value) is not int:
            raise TypeError(f'money value({value}) must be int type')

        if value < 0:
            raise ValueError(f'money value({value}) must not be negative')
