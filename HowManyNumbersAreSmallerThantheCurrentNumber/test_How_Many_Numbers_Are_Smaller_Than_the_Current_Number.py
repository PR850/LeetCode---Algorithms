import unittest
from How_Many_Numbers_Are_Smaller_Than_the_Current_Number import smallerNumbersThanCurrent

# python -m unittest test_How_Many_Numbers_Are_Smaller_Than_the_Current_Number.py


class TestHowManySmaller(unittest.TestCase):

    def check_if_list_contain_only_integers(self):
        with self.assertRaises(TypeError):
            smallerNumbersThanCurrent(['3'])

    def check_if_list_is_not_empty(self):
        with self.assertRaises(IndexError):
            smallerNumbersThanCurrent([])

    def test_HowManySmaller(self):
        result = smallerNumbersThanCurrent([8, 1, 2, 2, 3])
        self.assertEqual(result, [4, 0, 1, 1, 3])

    def test_HowManySmaller_2(self):
        result = smallerNumbersThanCurrent([7, 7, 7, 7])
        self.assertEqual(result, [0, 0, 0, 0])

    def test_HowManySmaller_3(self):
        result = smallerNumbersThanCurrent([-1, 1, 4, 5])
        self.assertEqual(result, [0, 1, 2, 3])

    def test_HowManySmaller_4(self):
        result = smallerNumbersThanCurrent([-1, 5, 4, 2])
        self.assertEqual(result, [0, 3, 2, 1])

    def test_HowManySmaller_5(self):
        result = smallerNumbersThanCurrent([1])
        self.assertEqual(result, [0])
