#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """This class represents a square with private instance attributes: size."""

    def __init__(self, size=0):
        """Initialize a new instance of the Square class.

        Args:
            size (number, optional): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size attribute.

        Args:
            value (number): The new value for the size attribute.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        self.__validate_size(value)
        self.__size = value

    def __validate_size(self, value):
        """Validate the size attribute.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Compute and return the area of the square.

        Returns:
            number: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Override the equality comparison."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Override the inequality comparison."""
        return not self == other

    def __lt__(self, other):
        """Override the less-than comparison."""
        return self.area() < other.area()

    def __le__(self, other):
        """Override the less-than-or-equal-to comparison."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Override the greater-than comparison."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Override the greater-than-or-equal-to comparison."""
        return self.area() >= other.area()


# Test cases
if __name__ == "__main__":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
