from unittest import TestCase
from parameterized import parameterized

from lotto.src.model.Rank import Rank, Ranks


class TestRank(TestCase):

    @parameterized.expand([
        [6, False, Rank.FIRST],
        [5, True, Rank.SECOND],
        [5, False, Rank.THIRD],
        [4, True, Rank.FOURTH],
        [3, True, Rank.FIFTH],
        [1, True, Rank.MISS],
    ])
    def test_value_of(self, count: int, is_matched_bonus: bool, expected_rank: Rank):
        self.assertEqual(expected_rank, Rank.value_of(count, is_matched_bonus))


class TestRanks(TestCase):

    def test_create(self):
        self.assertIsNotNone(Ranks([]))
        self.assertIsNotNone(Ranks([Rank.FIRST]))

    def test_create_invalid_type_raised_type_error(self):
        self.assertRaises(TypeError, lambda: Ranks(['']))
