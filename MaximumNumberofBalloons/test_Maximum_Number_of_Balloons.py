import unittest
from Maximum_Number_of_Balloons import maximumBalloonNumber


class TestBallon(unittest.TestCase):

    def test_it_will_reject_text_if_not_string(self):

        with self.assertRaises(TypeError):
            maximumBalloonNumber(232)

    def test_how_many_ballons(self):
        result = maximumBalloonNumber("balloonballoonballoon")
        self.assertEqual(result, 3)

    def test_how_many_ballons2(self):
        result = maximumBalloonNumber("loollb")
        self.assertEqual(result, 0)

    def test_how_many_ballons3(self):
        result = maximumBalloonNumber("loollbxxabooolaaannloo")
        self.assertEqual(result, 2)

    def test_how_many_ballons4(self):
        result = maximumBalloonNumber("")
        self.assertEqual(result, 0)
