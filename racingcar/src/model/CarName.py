MAX_NAME_LENGTH = 5


class CarName:

    def __init__(self, name: str) -> None:
        self._validate_type(name)
        self._validate_length(name)
        self.name = name

    @staticmethod
    def _validate_type(name):
        if type(name) is not str:
            raise TypeError(f'name must be string type: {name}')

    @staticmethod
    def _validate_length(name):
        if not name.strip():
            raise ValueError('name must not be blank')
        if MAX_NAME_LENGTH < len(name):
            raise ValueError(f'name({name}) must be up to {MAX_NAME_LENGTH} characters')
