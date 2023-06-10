#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mylist = []
    count = len(my_list)
    for i in range(count):
        if my_list[i] % 2 == 0:
            mylist.append(True)
        else:
            mylist.append(False)
    return mylist
