import unittest
import my_code1

class CodeTest(unittest.TestCase):

    def test_add_items(self):
        with self.assertRaises(TypeError):
            my_code1.add_items('r', 3)

    def test_read_file(self):
        with self.assertRaises(FileNotFoundError):
            my_code1.read_file('test2.txt')

if __name__ == '__main__':
    unittest.main()