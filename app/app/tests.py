"""
Sample Tests for recipe-app-api app.
"""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Tests the calc module."""

    def test_add_numbers(self):
        """Test the addition of numbers."""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

