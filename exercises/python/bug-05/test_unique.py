import unittest

from unique import unique


class TestUnique(unittest.TestCase):
    def test_removes_repeats_keeping_order(self):
        self.assertEqual(unique([1, 2, 2, 3, 1]), [1, 2, 3])

    def test_no_duplicates_unchanged(self):
        self.assertEqual(unique(["a", "b", "c"]), ["a", "b", "c"])

    def test_all_the_same(self):
        self.assertEqual(unique([7, 7, 7]), [7])

    def test_empty_list(self):
        self.assertEqual(unique([]), [])


if __name__ == "__main__":
    unittest.main()
