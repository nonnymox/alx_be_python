import unittest


# Buggy function from Exercise 1
def square(num):
    # Intentional bug: Returning the number itself instead of its square
    return num


# Test case for the buggy function
class TestSquareFunction(unittest.TestCase):

    def test_valid_input(self):
        # Test with a valid input
        self.assertEqual(square(4), 16)  # This should fail due to the bug

    def test_zero_input(self):
        # Test with zero
        self.assertEqual(square(0), 0)  # This should pass, but with the bug it might fail

    def test_negative_input(self):
        # Test with a negative number
        self.assertEqual(square(-3), 9)  # This should fail due to the bug

    def test_invalid_input(self):
        # Test with invalid input (non-integer)
        with self.assertRaises(TypeError):
            square("a")


# Running the tests
if __name__ == '__main__':
    unittest.main()
