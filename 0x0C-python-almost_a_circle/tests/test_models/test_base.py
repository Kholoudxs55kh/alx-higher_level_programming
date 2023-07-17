#!/usr/bin/python3
"""Unittest for Base"""


import unittest
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """ Base Class """

    def test_id(self):
        """ id """

        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(12)
        self.assertEqual(b3.id, 12)

        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_id_string(self):
        """string"""

        b1 = Base("string")
        self.assertEqual(b1.id, "string")

    def test_id_None(self):
        """None"""

        b1 = Base(None)
        self.assertEqual(b1.id, 4)

    def test_id_float(self):
        """float"""

        b1 = Base(1.2)
        self.assertEqual(b1.id, 1.2)

    def test_id_NaN(self):
        """float nan"""

        b1 = Base(float("nan"))
        self.assertEqual(b1.id is float("nan"), False)

    def test_id_inf(self):
        """float inf"""

        b1 = Base(float("inf"))
        self.assertEqual(b1.id is float("inf"), False)






if __name__ == '__main__':
    unittest.main()
