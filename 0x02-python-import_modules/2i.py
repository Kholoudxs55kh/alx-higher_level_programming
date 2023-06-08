#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    if argc == 0:
        print("0 arguments.")
    elif argc >= 1:
        print("{} arguments:".format(argc))
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, arg))
#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    if argc == 0:
        print("0 arguments.")
    elif argc >= 1:
        print("{} arguments:".format(argc))
        for i in range(argc):
            print("{:d}: {:s}".format(i + 1, sys.argv[i + 1]))
