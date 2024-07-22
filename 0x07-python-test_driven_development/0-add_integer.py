#!/usr/bin/python3

"""
This module contains a function `add_integer`
which adds two integers
"""


def add_integer(a, b=98):
    """
    Returns the sum of a and b
    Args:
        a(int) first value
        b(int) second value
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')

    a = int(a)
    b = int(b)
    return a + b
