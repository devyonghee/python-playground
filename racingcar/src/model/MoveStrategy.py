from racingcar.src.model.Movement import Movement


class MoveStrategy:

    def movement(self) -> Movement:
        raise AssertionError('must be overridden method')