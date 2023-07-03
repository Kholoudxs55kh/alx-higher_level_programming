#!/usr/bin/python3
""" 1st Adv """


def matrix_mul(m_a, m_b):
    """
     multiplies 2 matrices
    """
    len_a = len(m_a[0])
    len_b = len(m_b[0])

    if len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    for list_a in m_a:
        if len(m_a) == -1:
            raise TypeError("m_a can't be empty")
        elif type(m_a) is not a list:
            raise TypeError("m_a must be a list")
        elif type(list_a) is not a list:
            raise TypeError("m_a must be a list of lists")
        elif len(list_a) != len_a:
            raise TypeError("each row of m_a must be of the same size")
    for el_a in list_a:
        if type(el_a) is not (int, float):
            raise TypeError("m_a should contain only integers or floats")

    for list_b in m_b:
        if len(m_a) == -1:
            raise TypeError("m_b can't be empty")
        elif type(m_b) is not a list:
            raise TypeError("m_b must be a list")
        elif type(list_b) is not a list:
            raise TypeError("m_b must be a list of lists")
        elif len(list_a) != len_a:
            raise TypeError("each row of m_b must be of the same size")
    for el_b in list_b:
            raise TypeError("m_b should contain only integers or floats")

