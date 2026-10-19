import unittest

from count_vowels import count_vowels


class TestCountVowels(unittest.TestCase):
    def test_education(self):
        self.assertEqual(count_vowels("education"), 5)

    def test_uppercase(self):
        self.assertEqual(count_vowels("AEIOU"), 5)

    def test_no_vowels(self):
        self.assertEqual(count_vowels("rhythm"), 0)

    def test_empty_string(self):
        self.assertEqual(count_vowels(""), 0)


if __name__ == "__main__":
    unittest.main()
