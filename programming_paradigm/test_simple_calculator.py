import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Create a new calculator before each test."""
        self.calc = SimpleCalculator()

    # ---------- ADDITION ----------
    def test_add_integers(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_add_floats(self):
        self.assertAlmostEqual(self.calc.add(2.5, 0.5), 3.0)
        self.assertAlmostEqual(self.calc.add(-1.2, 1.2), 0.0)

    def test_add_large_numbers(self):
        self.assertEqual(self.calc.add(10**12, 10**12), 2 * 10**12)

    # ---------- SUBTRACTION ----------
    def test_subtract_integers(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(3, 10), -7)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_subtract_floats(self):
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3, places=7)
        self.assertAlmostEqual(self.calc.subtract(-1.0, -2.0), 1.0)

    # ---------- MULTIPLICATION ----------
    def test_multiply_integers(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-3, 5), -15)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_multiply_floats(self):
        self.assertAlmostEqual(self.calc.multiply(2.5, 2.0), 5.0)
        self.assertAlmostEqual(self.calc.multiply(-1.5, -2.0), 3.0)

    # ---------- DIVISION ----------
    def test_divide_integers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(3, 2), 1.5)

    def test_divide_floats(self):
        self.assertAlmostEqual(self.calc.divide(5.5, 2.2), 2.5, places=7)
        self.assertAlmostEqual(self.calc.divide(-4.5, -1.5), 3.0)

    def test_divide_by_zero_returns_none(self):
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_divide_negative_and_zero(self):
        self.assertAlmostEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(0, 5), 0)

if __name__ == "__main__":
    unittest.main()
