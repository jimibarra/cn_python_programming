import unittest


def subtract_divide(dividend, x, y):
    try:
        z = x - y
        return dividend / z
    #except ZeroDivisionError:
    except ValueError:
        return f"this won't work, {x} - {y} is 0 or lower."


class TestMath(unittest.TestCase):
    def test_check_division(self):
        self.assertEqual(subtract_divide(100, 50, 30), 5)

    # @unittest.skip('still debugging')
    def test_check_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            subtract_divide(100, 20, 20)


#result = subtract_divide(100, 20, 20)
#print(result)

if __name__ == '__main__':
    unittest.main()
