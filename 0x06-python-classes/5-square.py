#!/usr/bin/python3
""" Write a class Square that defines a square """


class Square:
    """ only squares ints """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if int(value) > -1 and value == int(value):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if not self.__size:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)
