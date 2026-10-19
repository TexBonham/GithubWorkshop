import unittest

from reverse_string import reverse_string


class TestReverseString(unittest.TestCase):
    def test_simple_word(self):
        self.assertEqual(reverse_string("abc"), "cba")

    def test_sentence(self):
        self.assertEqual(reverse_string("hi there"), "ereht ih")

    def test_single_letter(self):
        self.assertEqual(reverse_string("x"), "x")

    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")


if __name__ == "__main__":
    unittest.main()
