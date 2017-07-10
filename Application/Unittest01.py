import unittest
from testing_math import multiply

class TestMultiply(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_numbers(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_strings(self):
        self.assertEqual(multiply('a', 3), 'aaa')

if __name__ == '__main__':
    unittest.main()
