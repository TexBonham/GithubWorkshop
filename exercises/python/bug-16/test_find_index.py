import unittest

from find_index import find_index


class TestFindIndex(unittest.TestCase):
    def test_found_in_middle(self):
        self.assertEqual(find_index([5, 6, 7], 6), 1)

    def test_found_at_start(self):
        self.assertEqual(find_index([5, 6, 7], 5), 0)

    def test_not_found(self):
        self.assertEqual(find_index([5, 6, 7], 99), -1)

    def test_empty_list(self):
        self.assertEqual(find_index([], 1), -1)


if __name__ == "__main__":
    unittest.main()
