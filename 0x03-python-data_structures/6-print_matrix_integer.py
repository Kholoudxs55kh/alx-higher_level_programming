#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for listt in matrix:
        for i in range(len(listt)):
            print("{:d}".format(listt[i]), end=" ")
        print()
