import unittest
from my_code import division_calc

class CodeTest(unittest.TestCase):

    def test_division(self):
        self.assertEqual(division_calc(100, 20), 5)

    def test_positive(self):
        self.assertGreater(division_calc(100, -20), 0)

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            division_calc(100, 0)

if __name__ == '__main__':
    unittest.main()

