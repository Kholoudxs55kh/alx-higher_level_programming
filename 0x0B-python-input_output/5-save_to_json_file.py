#!/usr/bin/python3
""" task 4 """


import json


def save_to_json_file(my_obj, filename):
    """returns the JSON representation of an object (string)"""
    with open(filename, 'w', encoding='utf-8') as File:
        return json.dump(my_obj, File)
