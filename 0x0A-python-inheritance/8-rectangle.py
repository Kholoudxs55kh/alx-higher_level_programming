#!/usr/bin/python3
"""
Task 9
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle instantiation"""

    def __init__(self, width, height):
        """rectangle instantiation"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
