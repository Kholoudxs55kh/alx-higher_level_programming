#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    count = len(my_list)
    for i in range(count):
        print("{:d}".format(my_list[i]))
    if my_list is None:
        return
