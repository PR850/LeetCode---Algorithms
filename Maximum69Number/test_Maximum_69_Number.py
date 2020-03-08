import unittest
import pytest
from Maximum_69_Number import maximum69Number

# python -m unittest test_Maximum_69_Number.py
# pytest -v test_Maximum_69_Number.py


class TestMax69Num(unittest.TestCase):
    def should(self):
        with self.assertRaises(TypeError):
            maximum69Number('res')


test_data = [
    (6996, 9996),
    (9996, 9999),
    (9999, 9999),
    (9669, 9969)
]


@pytest.mark.parametrize("test_input, expected_result", test_data)
def testMax(test_input, expected_result):
    assert maximum69Number(test_input) == expected_result
