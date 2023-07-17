#!/usr/bin/python3
""" task 0 """
import json
import csv
from os import path


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

    @classmethod
    def create(cls, **dictionary):
        """returns Instance with all attributes already set"""

        if cls.__name__ == "Rectangle":
            rec = cls(1, 1)
        else:
            rec = cls(1)
        rec.update(**dictionary)
        return rec

    @classmethod
    def load_from_file(cls):
        """returns List of instances"""

        filename = cls.__name__ + ".json"
        _list = []

        if path.isfile(filename):
            with open(filename) as filee:
                _output = cls.from_json_string(filee.read())
            for i in _output:
                _list.append(cls.create(**i))
        return _list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes the CSV string representation of list_objs to a file"""

        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".csv"

        with open(filename, mode="w", newline="") as filee:
            csv_writer = csv.writer(filee)

            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    row = [obj.id, obj.width, obj.height, obj.x, obj.y]
                elif cls.__name__ == "Square":
                    row = [obj.id, obj.size, obj.x, obj.y]

                csv_writer.writerow(row)
