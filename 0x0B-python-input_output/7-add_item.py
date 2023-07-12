#!/usr/bin/python3
""" task 8"""

from sys import argv
SaveToJfile = __import__("5-save_to_json_file").save_to_json_file
LoadFromJfile = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

try:
    Jlist = LoadFromJfile(filename)
except FileNotFoundError:
    Jlist = []

for arg in argv[1:]:
    Jlist.append(arg)

SaveToJfile(Jlist, filename)
