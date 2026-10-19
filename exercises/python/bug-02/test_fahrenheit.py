import unittest

from fahrenheit import fahrenheit


class TestFahrenheit(unittest.TestCase):
    def test_boiling_point(self):
        self.assertEqual(fahrenheit(100), 212)

    def test_freezing_point(self):
        self.assertEqual(fahrenheit(0), 32)

    def test_negative_forty(self):
        self.assertEqual(fahrenheit(-40), -40)

    def test_body_temperature(self):
        self.assertAlmostEqual(fahrenheit(37), 98.6)


if __name__ == "__main__":
    unittest.main()
