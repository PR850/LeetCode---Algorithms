import unittest
import Maximum-69-Number

# python -m unittest test_Maximum_69_Number.py


class TestMax_69_Num(unittest.TestCase):
    def test_ot_will_reject_input_if_not_integer(self):
        with self.assertRaises(TypeError):
            maximum69Number('res')

    def test_max(self):
        result = maximum69Number(6996)
        self.assertEqual(result, 9996)

    def test_max2(self):
        result = maximum69Number(9996)
        self.assertEqual(result, 9999)

    def test_max3(self):
        result = maximum69Number(9669)
        self.assertEqual(result, 9969)

    def test_max4(self):
        result = maximum69Number(9999)
        self.assertEqual(result, 9999)
