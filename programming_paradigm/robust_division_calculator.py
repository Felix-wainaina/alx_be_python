#!/usr/bin/env python3
"""
robust_division_calculator.py

Provides a safe_divide function that performs division
with proper error handling for invalid inputs and zero division.
"""

def safe_divide(numerator, denominator):
    """Safely divide two numbers with error handling."""
    try:
        # Try converting to floats
        num = float(numerator)
        den = float(denominator)

        # Attempt the division
        result = num / den
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
