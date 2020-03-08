import unittest
import pytest
from How_Many_Numbers_Are_Smaller_Than_the_Current_Number import smallerNumbersThanCurrent

# python -m unittest test_How_Many_Numbers_Are_Smaller_Than_the_Current_Number.py


class TestHowManySmaller(unittest.TestCase):

    def check_if_list_contain_only_integers(self):
        with self.assertRaises(TypeError):
            smallerNumbersThanCurrent(['3'])

    def check_if_list_is_not_empty(self):
        with self.assertRaises(IndexError):
            smallerNumbersThanCurrent([])


test_data = [
    ([8, 1, 2, 2, 3], [4, 0, 1, 1, 3]),
    ([7, 7, 7, 7], [0, 0, 0, 0]),
    ([-1, 1, 4, 5], [0, 1, 2, 3]),
    ([-1, 5, 4, 2], [0, 3, 2, 1]),
    ([1], [0])
]


@pytest.mark.parametrize("test_input, expected_result", test_data)
def testNumbers(test_input, expected_result):
    assert smallerNumbersThanCurrent(test_input) == expected_result
