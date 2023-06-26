#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    li_len = 0
    elements = 0

    for i in my_list:
        li_len += 1

    try:
        if x >= li_len:
            for el in my_list:
                print("{}".format(el), end="")
                elements += 1
        else:
            for ele in range(0, x):
                print("{}".format(my_list[ele]), end="")
                elements += 1
    except:
        pass
    print()

    return elements
