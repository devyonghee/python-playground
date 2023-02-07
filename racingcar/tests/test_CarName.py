import unittest
from unittest import TestCase

from racingcar.src.model.CarName import CarName
from parameterized import parameterized


class TestCarName(TestCase):

    def test_create(self):
        self.assertIsNotNone(CarName('car'))

    @parameterized.expand([[1], ['']])
    def test_create_invalid_type_or_blank_thrown_error(self, name_value):
        self.assertRaises((TypeError, ValueError), lambda: CarName(name_value))

    def test_create_over_max_length_thrown_value_error(self):
        self.assertRaises(ValueError, lambda: CarName('123456'))


if __name__ == '__main__':
    unittest.main()
