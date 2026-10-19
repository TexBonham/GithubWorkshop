import unittest

from fizzbuzz import fizzbuzz


class TestFizzbuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzbuzz(9), "Fizz")

    def test_buzz(self):
        self.assertEqual(fizzbuzz(10), "Buzz")

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")

    def test_plain_number(self):
        self.assertEqual(fizzbuzz(7), "7")

    def test_fizzbuzz_45(self):
        self.assertEqual(fizzbuzz(45), "FizzBuzz")


if __name__ == "__main__":
    unittest.main()
