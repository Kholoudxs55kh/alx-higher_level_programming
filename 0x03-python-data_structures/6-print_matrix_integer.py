#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for listt in matrix:
        for i in listt:
            print("{:d}".format(i), end=" " if i != listt[-1] else "")
        print()
