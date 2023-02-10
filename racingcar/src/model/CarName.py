from typing import Sequence

MAX_NAME_LENGTH = 5


class CarName:

    def __init__(self, name: str) -> None:
        self.__validate_type(name)
        self.__validate_length(name)
        self.__name = name

    @staticmethod
    def __validate_type(name):
        if type(name) is not str:
            raise TypeError(f'name must be string type: {name}')

    @staticmethod
    def __validate_length(name):
        if not name.strip():
            raise ValueError('name must not be blank')
        if MAX_NAME_LENGTH < len(name):
            raise ValueError(f'name({name}) must be up to {MAX_NAME_LENGTH} characters')

    def __eq__(self, o: object) -> bool:
        return isinstance(o, CarName) \
            and self.__name == o.__name


DELIMITER = ','


def separate_names(names: str) -> Sequence[CarName]:
    if type(names) is not str or not names.strip():
        raise TypeError(f'names({names}) must not be blank string')
    return [CarName(name) for name in names.strip().split(DELIMITER)]
