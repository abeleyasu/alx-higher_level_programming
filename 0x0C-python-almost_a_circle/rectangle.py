#!/usr/bin/python3
"""
This module defines a Rectangle class for geometric calculations.
"""

class Rectangle:
    """
    Represents a rectangle with width and height.
    """
    def __init__(self, width, height):
        """
        Initializes the rectangle with the given width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates the area of the rectangle.
        Returns the area as a float.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.
        Returns the perimeter as a float.
        """
        return 2 * (self.width + self.height)
