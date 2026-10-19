import unittest

from average import average


class TestAverage(unittest.TestCase):
    def test_three_numbers(self):
        self.assertEqual(average([2, 4, 6]), 4)

    def test_single_number(self):
        self.assertEqual(average([5]), 5)

    def test_decimals(self):
        self.assertAlmostEqual(average([1, 2]), 1.5)

    def test_negative_numbers(self):
        self.assertEqual(average([-3, 3]), 0)


if __name__ == "__main__":
    unittest.main()
