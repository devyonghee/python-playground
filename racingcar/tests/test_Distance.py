import unittest
from unittest import TestCase

from racingcar.src.model.Distance import Distance
from parameterized import parameterized


class TestDistance(TestCase):

    @parameterized.expand([[0], [3], [100]])
    def test_create(self, value):
        self.assertIsNotNone(Distance(value))

    def test_create_invalid_type_raised_type_error(self):
        self.assertRaises(TypeError, lambda: Distance(''))

    def test_create_negative_raised_value_error(self):
        self.assertRaises(ValueError, lambda: Distance(-1))

    def test_add(self):
        # given & when
        sumDistance = Distance(2) + Distance(5)
        # then
        self.assertEqual(Distance(7), sumDistance)

    def test_operator(self):
        # given
        two = Distance(2)
        five = Distance(5)
        # when & then
        self.assertEqual(two < five, True)
        self.assertEqual(two > five, False)


if __name__ == '__main__':
    unittest.main()
