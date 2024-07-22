#!/usr/bin/python3

"""
This module contains a function `print_square` which
prints out a square using the character `#`
"""


def print_square(size):
    """
    prints out a square using `#`
    Args:
        size(int) side length/dimension of the square
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
