   import unittest
   from calculator import divide, is_even

   class TestCalculator(unittest.TestCase):
       def test_divide(self):
           self.assertEqual(divide(10, 2), 5)
           self.assertRaises(ZeroDivisionError, divide, 10, 0)

       def test_is_even(self):
           self.assertTrue(is_even(4))
           self.assertFalse(is_even(5))

   if __name__ == '__main__':
       unittest.main()