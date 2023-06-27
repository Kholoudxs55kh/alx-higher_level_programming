#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    res_list = []
    for el in range(list_length):
             try:
                 res_list += [my_list_1[el] / my_list_2[el]]
             except ZeroDivisionError:
                 res_list.append(0)
                 print("divission by 0")
             except IndexError:
                 res_list.append(0)
                 print("out of range")
             except TypeError:
                 res_list.append(0)
                 print("wrong type")
             finally:
                 pass
    return res_list
