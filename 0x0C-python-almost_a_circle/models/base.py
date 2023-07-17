#!/usr/bin/python3
""" task 0 """
import json


class Base:
    """ class Base """

    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation of list_dictionaries"""

        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        my_list = []
        filename = cls.__name__ + ".json"

        if list_objs is not None:
            for i in list_objs:
                my_list.append(i.to_dictionary())
        with open(filename, mode='w') as filee:
            filee.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """returns List of the JSON string representation"""

        if json_string is None:
            return []
        return json.loads(json_string)
