#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    listt = my_list.copy()
    count = len(listt) - 1
    if idx < 0 or idx > count:
        return my_list
    if idx <= count:
        listt[idx] = element
    return listt
