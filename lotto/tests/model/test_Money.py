import unittest
from unittest import TestCase
from parameterized import parameterized

from lotto.src.model.Money import Money


class TestMoney(TestCase):

    @parameterized.expand([[0], [1000], [10000]])
    def test_create(self, value):
        self.assertIsNotNone(Money(value))

    def test_create_invalid_type_raised_type_error(self):
        self.assertRaises(TypeError, lambda: Money('1'))

    def test_create_negative_value_raised_value_error(self):
        self.assertRaises(ValueError, lambda: Money(-1))

    @parameterized.expand([[100, 10], [300, 3], [1000, 1]])
    def test_floordiv_ten_thousand(self, dividend, expected_quotient):
        self.assertEqual(expected_quotient, Money(1000) // Money(dividend))

    @parameterized.expand([[10, Money(1000)], [10.0, Money(1000)], [Money(10), Money(1000)]])
    def test_multiply_hundred_with(self, multiplied_target, expected_money):
        self.assertEqual(expected_money, Money(100) * multiplied_target)


if __name__ == '__main__':
    unittest.main()
