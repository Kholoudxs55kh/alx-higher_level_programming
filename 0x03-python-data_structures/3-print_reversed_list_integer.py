#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    myRevList = reversed(my_list)
    for i in myRevList:
        print("{:d}".format(i))
