import unittest
from src.FizzBuzz import *
from parameterized import parameterized, parameterized_class
import math

class FizzBuzzParameterizedPackage(unittest.TestCase):
    def setUp(self):
        self.tmp = FizzBuzz()

    @parameterized.expand([
        (5, "Buzz"),
        (3, "Fizz"),
        (15, "FizzBuzz"),
    ])
    def test_one_parameterized(self,number, expected):
        self.assertEqual(self.tmp.game(number), expected)


@parameterized_class(('number', 'expected'), [
        (5, "Buzz"),
        (3, "Fizz"),
        (15, "FizzBuzz"),
        (69, "Fizz"),
        (300, "FizzBuzz"),
        (240, "FizzBuzz"),
        (753, "Fizz"),
        (600, "FizzBuzz"),
        (505, "Buzz"),
        (33, "Fizz"),
        (21, "Fizz"),
        (905, "Buzz"),
])
class FizzBuzzParameterizedPackage2(unittest.TestCase):
    def setUp(self):
        self.tmp = FizzBuzz()

    def test_second_parameterized(self):
        self.assertEqual(self.tmp.game(self.number), self.expected)


if __name__ == '__main__':
    unittest.main()
