#!/usr/bin/python3
""" Task 2 """


def append_write(filename="", text=""):
    """
     writes a string to a text file and returns the number of chars written
    """
    with open(filename, "a", encoding="utf-8") as File:
        return File.write(text)
