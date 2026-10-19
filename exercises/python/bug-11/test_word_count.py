import unittest

from word_count import word_count


class TestWordCount(unittest.TestCase):
    def test_simple_sentence(self):
        self.assertEqual(word_count("the quick brown fox"), 4)

    def test_extra_spaces(self):
        self.assertEqual(word_count("hello   world"), 2)

    def test_empty_string(self):
        self.assertEqual(word_count(""), 0)

    def test_single_word(self):
        self.assertEqual(word_count("hi"), 1)


if __name__ == "__main__":
    unittest.main()
