from racingcar.src.model.Movement import Movement


class MoveStrategy:

    def operated_movement(self) -> Movement:
        raise AssertionError('must be overridden method')