#!/usr/bin/python3
""" task 1 """


class MyList(list):
    """
    a class MyList that inherits from list:
    """

    def __init__(self):
        """initializes the object"""

        super().__init__()

    def print_sorted(self):
        """prints the list, but sorted"""

        print(sorted(self))
