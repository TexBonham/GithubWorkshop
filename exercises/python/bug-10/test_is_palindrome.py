import unittest

from is_palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    def test_lowercase_word(self):
        self.assertEqual(is_palindrome("level"), True)

    def test_capital_letters(self):
        self.assertEqual(is_palindrome("Racecar"), True)

    def test_with_spaces(self):
        self.assertEqual(is_palindrome("taco cat"), True)

    def test_not_a_palindrome(self):
        self.assertEqual(is_palindrome("python"), False)


if __name__ == "__main__":
    unittest.main()
