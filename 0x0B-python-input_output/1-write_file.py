#!/usr/bin/python3
""" Task 2 """


def write_file(filename="", text=""):
    """
     writes a string to a text file and returns the number of chars written
    """
    with open(filename, "w", encoding="utf-8") as File:
        return File.write(text)
