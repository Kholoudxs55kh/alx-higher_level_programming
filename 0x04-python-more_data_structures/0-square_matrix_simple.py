#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    #   listt = []
    #   new_matrix = listt + matrix
    #   for D1 in new_matrix:
    #       for D2 in range(len(D1)):
    #            D1[D2] **= 2
    #    for D1 in matrix:
    #        for D2 in D1:
    #            mat_ = []
    #            mat_ += D2**2
    #    return mat_
    mat_ = []
    for D1 in matrix:
        listt = []
        for D2 in D1:
            row.append(D2**2)
        mat_.append(listt)
    return mat_
