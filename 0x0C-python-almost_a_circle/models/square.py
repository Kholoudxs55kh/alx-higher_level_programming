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

    """ task 7 & 8 """
    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """

        if args:
            attribute_names = ['id', 'size', 'x', 'y']

            for attribute_name, value in zip(attribute_names, args):
                setattr(self, attribute_name, value)

        else:
            for key, val in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, val)

    def to_dictionary(self):
        """Returns dictionary representation of Square"""

        _dict = super().to_dictionary()
        _dict["size"] = _dict["width"]
        del _dict["width"], _dict["height"]
        return _dict
