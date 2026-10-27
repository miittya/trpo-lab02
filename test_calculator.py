import unittest

from calculator import add, divide


class CalculatorTests(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_divide_numbers(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_fractional_result(self):
        self.assertAlmostEqual(divide(1, 3), 0.3333333333)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == "__main__":
    unittest.main()