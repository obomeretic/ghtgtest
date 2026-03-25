"""Test module for ghtgtest"""

import unittest

class TestApp(unittest.TestCase):
    """Test cases for the application"""
    
    def test_hello(self):
        """Test hello world"""
        self.assertTrue(True)
    
    def test_sum(self):
        """Test sum function"""
        numbers = [1, 2, 3, 4, 5]
        expected = 15
        result = sum(numbers)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
