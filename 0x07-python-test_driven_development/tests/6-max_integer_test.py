import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test case for the `max_integer` function."""

    def test_max_at_end(self):
        """Test when the max int is at the end of the list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_start(self):
        """Test when the max int is at the start of the list"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test when the max int is at the middle of the list"""
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

    def test_one_element(self):
        """Tests a list with only one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Tests an empty list"""
        self.assertIsNone(max_integer([]))

    def test_all_negative(self):
        """Tests a list with only negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_values(self):
        """Tests a list with a mix of +ve and -ve numbers"""
        self.assertEqual(max_integer([-1, 3, 2, 1]), 3)

    def test_large_numbers(self):
        """Tests a list with large numbers"""
        self.assertEqual(max_integer([1, 1000000, 3, 999999]), 1000000)

    def test_floats(self):
        """tests a list with floats"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 0.5]), 3.5)

    def test_mixed_types(self):
        """tests a list with mixed data types"""
        with self.assertRaises(TypeError):
            max_integer([1, 'two', 3, 4])


if __name__ == '__main__':
    unittest.main()
