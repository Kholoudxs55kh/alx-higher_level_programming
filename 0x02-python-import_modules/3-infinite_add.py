#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = sys.argv[1:]
    result = 0
    for arg in argc:
        result += int(arg)
    print(result)
