#!/usr/bin/python3
# computing the square value of all integers of a matrix
# without altering/modifying the original matrix
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = list(map(lambda x: x * x, row))
        new_matrix.append(new_row)
    return new_matrix
