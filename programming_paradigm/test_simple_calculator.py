import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Create a new calculator before each test."""
        self.calc = SimpleCalculator()

    # ---------- ADD ----------
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertAlmostEqual(self.calc.add(2.5, 0.5), 3.0)

    # ---------- SUBTRACT ----------
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(3, 10), -7)
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3, places=7)

    # ---------- MULTIPLY ----------
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-3, 5), -15)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertAlmostEqual(self.calc.multiply(2.5, 2.0), 5.0)

    # ---------- DIVIDE ----------
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(3, 2), 1.5)
        self.assertAlmostEqual(self.calc.divide(5.5, 2.2), 2.5, places=7)
        self.assertIsNone(self.calc.divide(10, 0))  # division by zero
        self.assertAlmostEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(0, 5), 0)

if __name__ == "__main__":
    unittest.main()
