#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    listt = []
    new_matrix = listt + matrix
    for D1 in new_matrix:
        for D2 in range(len(D1)):
            D1[D2] **= 2
    return new_matrix
