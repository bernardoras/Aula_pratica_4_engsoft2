import unittest
from fraction import Fraction

class TestFraction(unittest.TestCase):

    def test_greatest_common_divisor(self):

        self.assertEqual(4, Fraction.greatest_common_divisor(4, 0))
        self.assertEqual(4, Fraction.greatest_common_divisor(0, 4))
        self.assertEqual(6, Fraction.greatest_common_divisor(18, 12))

    def test_get_simplified_num_and_denom(self):

        self.assertEqual((2, 1), Fraction.get_simplified_num_and_denom(Fraction(4, 2)))
        self.assertEqual((3, 2), Fraction.get_simplified_num_and_denom(Fraction(9, 6)))
        self.assertEqual((0, 1), Fraction.get_simplified_num_and_denom(Fraction(0, 6)))

    def test_least_common_multiple(self):

        self.assertEqual(0, Fraction.least_common_multiple(0, 4))
        self.assertEqual(0, Fraction.least_common_multiple(4, 0))
        self.assertEqual(4, Fraction.least_common_multiple(4, 1))
        self.assertEqual(16, Fraction.least_common_multiple(16, 8))
        self.assertEqual(24, Fraction.least_common_multiple(12, 8))

    def test_constructor_raises_zero_division_error_on_zero_denominator(self):
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0)

    def test_constructor_simplifies_fraction(self):
        fraction = Fraction(2, 4)
        self.assertEqual(fraction, Fraction(1, 2))

    def test_constructor_eliminates_double_neg_signs(self):
        fraction = Fraction(-1, -1)
        self.assertEqual(fraction, Fraction(1, 1))

    def test_constructor_puts_denom_sign_in_num(self):
        fraction = Fraction(1, -1)
        self.assertEqual(fraction, Fraction(-1, 1))

    def test_eq_fraction_and_non_fraction_are_not_eq(self):
        self.assertNotEqual(Fraction(1, 1), [])

    def test_eq_different_fractions(self):
        self.assertNotEqual(Fraction(1, 1), Fraction(1, 2))

    def test_add_equal_denom_simplify_fraction(self):
        fraction = Fraction(3, 4)
        fraction.add(Fraction(1, 4))
        self.assertEqual(fraction, Fraction(1, 1))

    def test_add_different_denom_simplify_fraction(self):
        fraction = Fraction(3, 4)
        fraction.add(Fraction(0, 6))
        self.assertEqual(fraction, Fraction(3, 4))

    def test_subtract_equal_denom_simplify_fraction(self):
        fraction = Fraction(3, 4)
        fraction.subtract(Fraction(1, 4))
        self.assertEqual(fraction, Fraction(1, 2))

    def test_subtract_different_denom_simplify_fraction(self):
        fraction = Fraction(3, 4)
        fraction.subtract(Fraction(0, 6))
        self.assertEqual(fraction, Fraction(3, 4))