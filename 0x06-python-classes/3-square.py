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
    my_square_1 = Square(3)
    print("Area: {}".format(my_square_1.area()))

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    my_square_2 = Square(5)
    print("Area: {}".format(my_square_2.area()))
