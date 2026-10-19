import unittest

from add_tax import add_tax


class TestAddTax(unittest.TestCase):
    def test_quarter_tax(self):
        self.assertEqual(add_tax(10, 0.25), 12.5)

    def test_no_tax(self):
        self.assertEqual(add_tax(20, 0), 20)

    def test_rounds_to_cents(self):
        self.assertEqual(add_tax(9.99, 0.07), 10.69)

    def test_free_item(self):
        self.assertEqual(add_tax(0, 0.5), 0)


if __name__ == "__main__":
    unittest.main()
