#!/usr/bin/python3
# a function that prints a list of integers
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            if i == len(row) - 1:
                print("{:d}".format(row[i]), end='')
            else:
                print("{:d}".format(row[i]), end=' ')
        print()
