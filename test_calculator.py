# Author: Max Radke         Date: 3/11/21

import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calculator.sub(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(calculator.mult(3, 4), 12)

    def test_division(self):
        self.assertEqual(calculator.div(9, 3), 3)

# call the tests
if __name__ == "__main__":
    unittest.main(verbosity=2)
