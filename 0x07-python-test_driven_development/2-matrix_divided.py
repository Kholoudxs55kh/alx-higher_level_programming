#!/usr/bin/python3
""" 2nd Task """


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix
    """
    matrix_row_len = len(matrix[0])

    for row in range(len(matrix)):
        if len(matrix[row]) != matrix_row_len:
            raise TypeError("Each row of the matrix must have the same size")
        elif type(matrix[row]) is not list or type(matrix) is not list:
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
        for el in matrix[row]:
            if type(el) is not int and type(el) is not float:
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    return [[round(el / div, 2) for el in row]for row in matrix]
