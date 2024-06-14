#!/usr/bin/python3
"""
This module defines a Circle class for geometric calculations.
"""

class Circle:
    """
    Represents a circle with a radius.
    """
    def __init__(self, radius):
        """
        Initializes the circle with the given radius.
        """
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle.
        Returns the area as a float.
        """
        import math
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculates the perimeter of the circle.
        Returns the perimeter as a float.
        """
        import math
        return 2 * math.pi * self.radius
