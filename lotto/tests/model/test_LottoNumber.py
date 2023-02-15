import unittest
from unittest import TestCase

from parameterized import parameterized

from lotto.src.model.LottoNumber import LottoNumber


class TestLottoNumber(TestCase):

    @parameterized.expand([[1], [30], [45]])
    def test_create(self, number: int):
        self.assertIsNotNone(LottoNumber(number))

    def test_create_invalid_type_raised_type_error(self):
        self.assertRaises(TypeError, lambda: LottoNumber('1'))

    @parameterized.expand([[-1], [0], [46]])
    def test_create_out_of_range_raised_value_error(self, number: int):
        self.assertRaises(ValueError, lambda: LottoNumber(number))


if __name__ == '__main__':
    unittest.main()
