#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    to_del = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            to_del.append(key)
    for i in to_del:
        del a_dictionary[i]
    return a_dictionary
