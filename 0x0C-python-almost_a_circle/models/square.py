#!/usr/bin/python3
""" square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ start of task 10 """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Readable"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """int: Assigns value to size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
