#!/usr/bin/python3
""" Task 1 """


def read_file(filename=""):
    """
    reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, "r", encoding="utf-8") as File:
        print(File.read(), end="")
