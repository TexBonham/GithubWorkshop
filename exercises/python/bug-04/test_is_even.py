import unittest

from is_even import is_even


class TestIsEven(unittest.TestCase):
    def test_four(self):
        self.assertEqual(is_even(4), True)

    def test_seven(self):
        self.assertEqual(is_even(7), False)

    def test_zero(self):
        self.assertEqual(is_even(0), True)

    def test_negative_odd(self):
        self.assertEqual(is_even(-3), False)


if __name__ == "__main__":
    unittest.main()
