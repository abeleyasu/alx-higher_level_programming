#!/usr/bin/python3
"""
Unit tests for the Rectangle class.
"""

import unittest
from rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """
    Tests for the Rectangle class.
    """

    def setUp(self):
        """
        Set up a Rectangle instance for testing.
        """
        self.rectangle = Rectangle(3, 4)

    def test_area(self):
        """
        Test the area method.
        """
        self.assertEqual(self.rectangle.area(), 12)

    def test_perimeter(self):
        """
        Test the perimeter method.
        """
        self.assertEqual(self.rectangle.perimeter(), 14)

if __name__ == "__main__":
    unittest.main()
