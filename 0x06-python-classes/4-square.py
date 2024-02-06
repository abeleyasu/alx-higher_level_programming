#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """This class represents a square with private instance attribute: size."""

    def __init__(self, size=0):
        """Initialize a new instance of the Square class.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.__size = size
        self.__validate_size()

    @property
    def size(self):
        """Getter method to retrieve the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size attribute.

        Args:
            value (int): The new value for the size attribute.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        self.__size = value
        self.__validate_size()

    def __validate_size(self):
        """Validate the size attribute.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Compute and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2


# Test cases
if __name__ == "__main__":
    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)
