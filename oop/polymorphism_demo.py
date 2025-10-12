#!/usr/bin/env python3
import math

class Shape:
    """Base class representing a general shape."""
    def area(self):
        # This method should be overridden by subclasses
        raise NotImplementedError("Subclasses must implement the area method")


class Rectangle(Shape):
    """Derived class representing a rectangle."""
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    """Derived class representing a circle."""
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
