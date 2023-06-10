#!/usr/bin/python3
def no_c(my_string):
    _string = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            _string += i
    return _string
