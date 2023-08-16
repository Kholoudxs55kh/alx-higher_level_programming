#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ testing """
    def test_int(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_int(self):
        self.assertEqual(max_integer([1, 5, 3]), 5)


    def test_float(self):
        self.assertEqual(max_integer([1, 2, 3.5]), 3.5)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_charWithNums(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'k', 4])

    def test_charsOnly(self):
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')

    def test_varInside(self):
        with self.assertRaises(NameError):
            max_integer([1, 2, k, 4])

    def test_OneEle(self):
        self.assertEqual(max_integer([1]), 1)


if __name__ == '__main__':
    unittest.main()
