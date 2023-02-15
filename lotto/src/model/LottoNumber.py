MIN_NUMBER = 1
MAX_NUMBER = 45


class LottoNumber:

    def __init__(self, number: int) -> None:
        self.__validate_number(number)
        self.__number = number

    @staticmethod
    def __validate_number(number):
        if type(number) is not int:
            raise TypeError('number must be int type')
        if number < MIN_NUMBER or MAX_NUMBER < number:
            raise ValueError(f'number({number}) must be between {MIN_NUMBER} and {MAX_NUMBER}')

    def __hash__(self) -> int:
        return self.__number

    def __eq__(self, o: object) -> bool:
        return isinstance(o, LottoNumber) \
            and self.__number == o.__number
