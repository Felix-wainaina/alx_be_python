#!/usr/bin/env python3

class Calculator:
    """A simple calculator demonstrating class and static methods."""

    # Class attribute shared by all instances
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Perform addition without needing class or instance data."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Access class attribute using cls, then perform multiplication."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
