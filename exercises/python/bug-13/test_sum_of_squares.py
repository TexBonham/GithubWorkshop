import unittest

from sum_of_squares import sum_of_squares


class TestSumOfSquares(unittest.TestCase):
    def test_three_numbers(self):
        self.assertEqual(sum_of_squares([1, 2, 3]), 14)

    def test_empty_list(self):
        self.assertEqual(sum_of_squares([]), 0)

    def test_negatives(self):
        self.assertEqual(sum_of_squares([-2, 2]), 8)

    def test_single_number(self):
        self.assertEqual(sum_of_squares([5]), 25)


if __name__ == "__main__":
    unittest.main()
