import unittest
from src.calculator import add, divide, multiply, subtract

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(10, add(8, 2))

    def test_subtract(self):
        self.assertEqual(9, subtract(15, 6))

    def test_divide(self):
        self.assertEqual(4, divide(20, 5))

    def test_multiply(self):
        self.assertEqual(50, multiply(10, 5))