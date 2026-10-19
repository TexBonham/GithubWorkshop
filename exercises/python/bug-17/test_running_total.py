import unittest

from running_total import running_total


class TestRunningTotal(unittest.TestCase):
    def test_three_numbers(self):
        self.assertEqual(running_total([1, 2, 3]), [1, 3, 6])

    def test_with_negative(self):
        self.assertEqual(running_total([5, -2, 4]), [5, 3, 7])

    def test_single_number(self):
        self.assertEqual(running_total([9]), [9])

    def test_empty_list(self):
        self.assertEqual(running_total([]), [])


if __name__ == "__main__":
    unittest.main()
