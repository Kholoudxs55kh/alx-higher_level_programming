#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    argc = sys.argv[1:]
    for arg in argc:
        result += int(arg)
    print(result)
