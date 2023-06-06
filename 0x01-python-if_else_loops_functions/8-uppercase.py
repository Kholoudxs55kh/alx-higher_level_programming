#!/usr/bin/python3
def uppercase(str):
    o_str = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            o_str += "{}".format(chr(ord(i) - 32))
        else:
            o_str += "{}".format(i)
    print(o_str, end="\n")
