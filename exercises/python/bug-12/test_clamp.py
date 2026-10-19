import unittest

from clamp import clamp


class TestClamp(unittest.TestCase):
    def test_inside_range(self):
        self.assertEqual(clamp(5, 0, 10), 5)

    def test_too_low(self):
        self.assertEqual(clamp(-3, 0, 10), 0)

    def test_too_high(self):
        self.assertEqual(clamp(42, 0, 10), 10)

    def test_on_the_edge(self):
        self.assertEqual(clamp(10, 0, 10), 10)


if __name__ == "__main__":
    unittest.main()
