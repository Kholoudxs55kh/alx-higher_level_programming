#!/usr/bin/python3
""" 1st Task """


def add_integer(a, b=98):
    """
        adds two ints
    """

    if type(a) is float:
        a = int(a)
    elif type(a) is not int:
        raise TypeError("a must be an integer")
    elif type(b) is float:
        b = int(b)
    elif type(b) is not int:
        raise TypeError("b must be an integer")

    return int(a + b)
