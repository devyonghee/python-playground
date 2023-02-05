from unittest import mock
from parameterized import parameterized
from racingcar.src.model.Movement import Movement
from racingcar.src.model.RandomEngineStrategy import RandomEngineStrategy
import unittest

random_engine = RandomEngineStrategy()


class TestRandomEngineStrategy(unittest.TestCase):

    @parameterized.expand([[0, Movement.STOP], [3, Movement.STOP], [4, Movement.GO], [9, Movement.GO]])
    def test_operated_movement(self, return_random_value, expected_movement):
        with mock.patch('random.randrange') as mock_randrange:
            mock_randrange.return_value = return_random_value
            self.assertIs(random_engine.operated_movement(), expected_movement)
