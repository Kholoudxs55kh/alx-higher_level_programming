#!/usr/bin/python3
""" task 2 """
from models.base import Base


class Rectangle(Base):
    """inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        @getter
        """
        return self.__width

    @property
    def height(self):
        """
        @getter
        """
        return self.__height

    @property
    def x(self):
        """
        @getter
        """
        return self.__x

    @property
    def y(self):
        """
        @getter
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
           Setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
           Setter
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """
           Setter
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """
           Setter
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    """ task 4 """

    def area(self):
        """returns the area value"""

        return self.__width * self.__height

    """ task 5 """

    def display(self):
        """prints in stdout the Rectangle instance with #"""

        for c in range(self.__y):
            print()
        for c in range(self.__height):
            for c in range(self.__x):
                print(' ', end='')
            for c in range(self.__width):
                print('#', end='')
            print()

    """ task 6 """

    def __str__(self):
        """returns a readable sntnc """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    """ task 7 & 8 """
    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """

        if args:
            attribute_names = ['id', 'width', 'height', 'x', 'y']

            for attribute_name, value in zip(attribute_names, args):
                setattr(self, attribute_name, value)

        else:
            for key, val in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, val)
