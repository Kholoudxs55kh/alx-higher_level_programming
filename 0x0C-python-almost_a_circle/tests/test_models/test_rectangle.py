#!/usr/bin/python3
"""Unittest for Rectangle"""


import unittest
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Rectangle class test"""
    def setUp(self):
        """Resets nb_objects"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Prints out the id"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        self.assertTrue(type(r3), Rectangle)

    def test_one_param(self):
        """Passing one parameter"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1)

    def test_all_param(self):
        """Passing all parameters"""
        r1 = Rectangle(1, 1, 1, 1, 1)

    def test_string(self):
        """Passing string"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, "string")
        with self.assertRaises(TypeError):
            r1 = Rectangle("string", 1)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, "4")

    def test_no_param(self):
        """Passing nothing"""
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_excess_param(self):
        """Excess parameters"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, 1, 1, 1)

    def test_float(self):
        """Float parameter"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1.2, 1, 1, 3)

    def test_NaN(self):
        """NaN parameter"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, float("nan"), 1, 1)

    def test_inf(self):
        """inf parameter"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, float("inf"), 1, 1)

    def test_unknown(self):
        """unknown parameter"""
        with self.assertRaises(NameError):
            r1 = Rectangle(a)

    def test_None(self):
        """None parameter"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, None, 1, 1)

    def test_neg(self):
        """Neg parameter"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2, 1, 1)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, 3, -4)


    def test_area(self):
        """Prints out area"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.area(), 20)

    def test_display(self):
        """Tests rectangle output"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(2, 2)
        r1.display()
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "##\n##\n"


    def test_display_x_y(self):
        """Tests rectangle output with x and y"""
        output = StringIO()
        sys.stdout = output
        r2 = Rectangle(3, 2, 1, 0)
        r2.display()
        sys.stdout = sys.__stdout__
        assert output.getvalue() == " ###\n ###\n"

    def test_str(self):
        """Tests __str__"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(4, 6, 2, 1, 12)
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Rectangle] (12) 2/1 - 4/6\n"
