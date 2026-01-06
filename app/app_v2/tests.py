from django.test import SimpleTestCase
from app_v2.views import division


class TestApp2Views(SimpleTestCase):
    """Tests for app_v2 views module."""
    def test_division(self):
        """Test division function."""
        res = division(10, 2)
        self.assertEqual(res, 5)

    def test_nonfactor_divisor(self):
        res = division(10, 3)
        self.assertEqual(res, 3)

    def test_divbyzeroerr(self):
        """Testing for the division by zero error."""
        self.assertRaises(ZeroDivisionError, division, 3, 0)
        with self.assertRaises(Exception) as ctx:
            division(3 ,0)
            self.assertTrue("Error: " in str(ctx.exception))