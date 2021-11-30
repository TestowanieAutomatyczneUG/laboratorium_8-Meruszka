import unittest
from assertpy import *
from src.FizzBuzz import *

f = FizzBuzz()
class TestFizzBuzz(unittest.TestCase):
    def test_Fizz_3(self):
        assert_that(f.game(3)).is_equal_to("Fizz")

    def test_Fizz_3_5(self):
        assert_that(f.game).raises(ValueError).when_called_with(3.5)

    def test_Fizz_3_3(self):
        assert_that(f.game).raises(ValueError).when_called_with(3.3)

    def test_Fizz_5(self):
        assert_that(f.game(5)).is_equal_to("Buzz")

    def test_Fizz_5_5(self):
        assert_that(f.game).raises(ValueError).when_called_with(5.5)

    def test_Fizz_5_3(self):
        assert_that(f.game).raises(ValueError).when_called_with(5.3)

    def test_Exp_list(self):
        assert_that(f.game).raises(ValueError).when_called_with([])

    def test_Exp_obj(self):
        assert_that(f.game).raises(ValueError).when_called_with({})

    def test_FizzBuzz_15(self):
        assert_that(f.game(15)).is_equal_to("FizzBuzz")

    def test_FizzBuzz_30(self):
        assert_that(f.game(30)).is_equal_to("FizzBuzz")

    def test_Exp_7(self):
        assert_that(f.game).raises(TypeError).when_called_with(7)

    def test_Exp_53(self):
        assert_that(f.game).raises(TypeError).when_called_with(53)

    def test_Exp_11111111111(self):
        assert_that(f.game).raises(TypeError).when_called_with(11111111111)

    def test_FizzBuzz_45(self):
        assert_that(f.game(45)).is_instance_of(str)

    def test_Fizz_55(self):
        assert_that(f.game(55)).is_not_equal_to("Fizz")

    def test_Fizz_600(self):
        assert_that(f.game(600)).is_not_equal_to("Fizz")

    def test_FizzBuzz_879(self):
        assert_that(f.game(879)).is_not_equal_to("Buzz")

    def test_Fizz_500(self):
        assert_that(f.game(500)).is_same_as("Buzz")

    def test_FizzBuzz_300(self):
        assert_that(f.game(300)).is_same_as("FizzBuzz")

    def test_Fizz_333(self):
        assert_that(f.game(333)).is_same_as("Fizz")

    def test_Fizz_666(self):
        assert_that(f.game(666)).is_subset_of("FizzBuzz")

    def test_Fizz_999(self):
        assert_that(f.game(999)).is_subset_of("FizzBuzz")

    def test_Buzz_555(self):
        assert_that(f.game(555)).is_subset_of("FizzBuzz")

    def test_FizzBuzz_1200(self):
        assert_that(f.game(1200)).ends_with("zz")

    def test_FizzBuzz_1233(self):
        assert_that(f.game(1233)).ends_with("zz")

    def test_FizzBuzz_1355(self):
        assert_that(f.game(1355)).ends_with("zz")

    def test_Fizz_3333(self):
        assert_that(f.game(3333)).matches(r'F\w')

    def test_Buzz_5555(self):
        assert_that(f.game(5555)).matches(r'B\w')


