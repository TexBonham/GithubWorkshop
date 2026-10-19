import unittest

from factorial import factorial


class TestFactorial(unittest.TestCase):
    def test_five(self):
        self.assertEqual(factorial(5), 120)

    def test_three(self):
        self.assertEqual(factorial(3), 6)

    def test_one(self):
        self.assertEqual(factorial(1), 1)

    def test_zero(self):
        self.assertEqual(factorial(0), 1)


if __name__ == "__main__":
    unittest.main()
