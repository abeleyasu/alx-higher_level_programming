#!/usr/bin/python3
"""This module defines a MagicClass class."""


class MagicClass:
    """This class does exactly the same as the provided Python bytecode."""

    def __init__(self, radius=0):
        """Initialize a new instance of the MagicClass class.

        Args:
            radius (number, optional): The radius of the circle. Defaults to 0.
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """Compute and return the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * 3.14159265359

    def circumference(self):
        """Compute and return the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * 3.14159265359 * self.__radius
