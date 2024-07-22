#!/usr/bin/python3

"""
This module contains a function `say_my_name` which prints out a
name in the format, 'first_name' 'last_name'.
"""


def say_my_name(first_name, last_name=""):
    """
    Print My name is <first_name> <last_name>
    Args:
        first_name(string) the first value
        last_name(string) the second value
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
