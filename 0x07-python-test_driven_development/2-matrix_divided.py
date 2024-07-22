#!/usr/bin/python3

"""
This module contains a function `matrix_divided` which divides
all elements of a matrix by a certain value `div`
"""


def matrix_divided(matrix, div):
    """
    divides all elements of matrix by div
    Args:
        matrix(list of lists) first value
        div(int or float) second value
    Returns:
        list of lists: a new matrix with each element divided by div
    """
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(err)
    if len(matrix) == 0:
        return []

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    first_size = len(matrix[0])
    new_matrix = []
    for a_item in matrix:
        if not isinstance(a_item, list):
            raise TypeError(err)
        if len(a_item) != first_size:
            raise TypeError('Each row of the matrix must have the same size')

        new_list = []
        for item in a_item:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError(err)
            result = round((item / div), 2)
            new_list.append(result)
        new_matrix.append(new_list)

    return new_matrix
