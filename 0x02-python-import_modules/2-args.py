#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:\n1: {:s}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(argc))
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{:d}: {:s}".format(i, arg))
