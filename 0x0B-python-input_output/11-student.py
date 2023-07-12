#!/usr/bin/python3
"""task 10"""


class Student:
    """Instantiation"""

    def __init__(self, first_name, last_name, age):
        """Initialize"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        _dict = {}
        for i in attrs:
            try:
                _dict[i] = self.__dict__[i]
            except FileNotFoundError:
                pass
        return _dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except FileNotFoundError:
                pass
