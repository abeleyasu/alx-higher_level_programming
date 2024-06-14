#!/usr/bin/python3
"""
Unit tests for the Circle class.
"""

import unittest
from circle import Circle

class TestCircle(unittest.TestCase):
    """
    Tests for the Circle class.
    """

    def setUp(self):
        """
        Set up a Circle instance for testing.
        """
        self.circle = Circle(5)

    def test_area(self):
        """
        Test the area method.
        """
        self.assertAlmostEqual(self.circle.area(), 78.53981633974483, places=5)

    def test_perimeter(self):
        """
        Test the perimeter method.
        """
        self.assertAlmostEqual(self.circle.perimeter(), 31.41592653589793, places=5)

if __name__ == "__main__":
    unittest.main()
