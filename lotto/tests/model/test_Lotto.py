from unittest import TestCase

from lotto.src.model.Lotto import Lotto
from lotto.src.model.LottoNumber import LottoNumber
from parameterized import parameterized

ONE_TO_SIX_LOTTO = Lotto([
    LottoNumber(1),
    LottoNumber(2),
    LottoNumber(3),
    LottoNumber(4),
    LottoNumber(5),
    LottoNumber(6)
])


class TestLotto(TestCase):

    def test_create(self):
        self.assertIsNotNone(Lotto([
            LottoNumber(1),
            LottoNumber(2),
            LottoNumber(3),
            LottoNumber(4),
            LottoNumber(5),
            LottoNumber(6)
        ]))

    def test_create_invalid_size_raised_value_error(self):
        self.assertRaises(ValueError, lambda: Lotto([
            LottoNumber(1),
            LottoNumber(2),
            LottoNumber(3),
            LottoNumber(4),
            LottoNumber(5)
        ]))

    def test_create_duplicate_values_raise_value_error(self):
        self.assertRaises(ValueError, lambda: Lotto([
            LottoNumber(1),
            LottoNumber(2),
            LottoNumber(3),
            LottoNumber(4),
            LottoNumber(5),
            LottoNumber(5)
        ]))

    def test_matched_count(self):
        # given
        four_to_nine_lotto = Lotto([
            LottoNumber(4),
            LottoNumber(5),
            LottoNumber(6),
            LottoNumber(7),
            LottoNumber(8),
            LottoNumber(9)
        ])
        # when
        count = ONE_TO_SIX_LOTTO.matched_count(four_to_nine_lotto)
        # then
        self.assertEqual(3, count)

    @parameterized.expand([[LottoNumber(1), True], [LottoNumber(7), False]])
    def test_contains(self, number: LottoNumber, expected: bool):
        self.assertEqual(expected, number in ONE_TO_SIX_LOTTO)
