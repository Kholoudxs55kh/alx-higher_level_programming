#!/usr/bin/python3
""" write unittests for the function def max_integer(list=[])"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInt:
    """ testing """
    def test_int(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_float(self):
        self.assertEqual(max_integer([1, 2, 3.5]), 3.5)


if __name__ == '__main__':
    unittest.main()
