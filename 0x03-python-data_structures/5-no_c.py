#!/usr/bin/python3
def no_c(my_string):
    #    return my_string.replace('c', '').replace('C', '')
    #    not allowe y a3ma y a3maaaa :DDD
    _string = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            _string += i
    return _string
