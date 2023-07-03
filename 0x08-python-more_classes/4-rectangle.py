#!/usr/bin/python3
""" 2nd task """


class Rectangle:
    """
    class with methods and instance attributes
    """

    def __init__(self, width=0, height=0):
        """
        Initialie width and height
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        @getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
           Setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        @getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
           Setter
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        print the rectangle with the character #
        """
        if self.width == 0 or self.height == 0:
            return ""

        recta = ""
        for high in range(self.__height):
            for wid in range(self.__width):
                recta += "#"
            if high != self.__height - 1:
                recta += "\n"
        return recta

    def __repr__(self):
        """
        print the rectangle with the character #
        """
        return "Rectangle({}, {})".format(self.width, self.height)
