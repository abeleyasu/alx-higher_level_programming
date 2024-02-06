#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """This class represents a square with private instance attributes: size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new instance of the Square class.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

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
        self.__validate_size(value)
        self.__size = value

    @property
    def position(self):
        """Getter method to retrieve the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to set the position attribute.

        Args:
            value (tuple): The new value for the position attribute.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        self.__validate_position(value)
        self.__position = value

    def __validate_size(self, value):
        """Validate the size attribute.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def __validate_position(self, value):
        """Validate the position attribute.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Compute and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using the character '#' and the specified position."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Return a string representation of the square (same as my_print)."""
        result = ""
        if self.__size == 0:
            result += "\n"
        else:
            for _ in range(self.__position[1]):
                result += "\n"
            for _ in range(self.__size):
                result += " " * self.__position[0] + "#" * self.__size + "\n"
        return result[:-1]  # Remove the trailing newline


# Test cases
if __name__ == "__main__":
    my_square = Square(5, (0, 0))
    print(my_square)

    print("--")

    my_square = Square(5, (4, 1))
    print(my_square)
