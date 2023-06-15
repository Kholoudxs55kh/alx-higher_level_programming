#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    _dict = a_dictionary.copy()
    for i in _dict:
        _dict[i] *= 2
    return _dict
