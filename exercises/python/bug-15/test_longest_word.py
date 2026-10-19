import unittest

from longest_word import longest_word


class TestLongestWord(unittest.TestCase):
    def test_mixed_lengths(self):
        self.assertEqual(longest_word(["hi", "hello", "hey"]), "hello")

    def test_single_word(self):
        self.assertEqual(longest_word(["python"]), "python")

    def test_longest_last(self):
        self.assertEqual(longest_word(["a", "bb", "ccc"]), "ccc")

    def test_empty_list(self):
        self.assertEqual(longest_word([]), "")


if __name__ == "__main__":
    unittest.main()
