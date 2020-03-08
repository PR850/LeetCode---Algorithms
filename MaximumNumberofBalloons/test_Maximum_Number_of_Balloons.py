import pytest
import unittest
from Maximum_Number_of_Balloons import maximumBalloonNumber


class TestBallon(unittest.TestCase):

    def test_it_will_reject_text_if_not_string(self):

        with self.assertRaises(TypeError):
            maximumBalloonNumber(232)


test_data = [
    ("balloonballoonballoon", 3),
    ("loollb", 0),
    ("loollbxxabooolaaannloo", 2),
    ("", 0)
]


@pytest.mark.parametrize("test_input, expected_result", test_data)
def testBalloons(test_input, expected_result):
    assert maximumBalloonNumber(test_input) == expected_result
