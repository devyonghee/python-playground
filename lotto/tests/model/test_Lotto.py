from unittest import TestCase

from lotto.src.model.Lotto import Lotto
from lotto.src.model.LottoNumber import LottoNumber


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
