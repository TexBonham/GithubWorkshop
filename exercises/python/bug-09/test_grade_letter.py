import unittest

from grade_letter import grade_letter


class TestGradeLetter(unittest.TestCase):
    def test_top_score(self):
        self.assertEqual(grade_letter(90), "A")

    def test_b_grade(self):
        self.assertEqual(grade_letter(85), "B")

    def test_c_boundary(self):
        self.assertEqual(grade_letter(70), "C")

    def test_d_grade(self):
        self.assertEqual(grade_letter(65), "D")

    def test_failing(self):
        self.assertEqual(grade_letter(42), "F")


if __name__ == "__main__":
    unittest.main()
