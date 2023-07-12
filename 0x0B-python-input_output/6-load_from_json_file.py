#!/usr/bin/python3
""" Task 1 """


import json


def load_from_json_file(filename):
    """
    reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, "r", encoding="utf-8") as File:
        return json.load(File)
