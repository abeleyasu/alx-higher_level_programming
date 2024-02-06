#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """This class represents a square with a private instance attribute: size."""

    def __init__(self, size):
        """Initialize a new instance of the Square class.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
