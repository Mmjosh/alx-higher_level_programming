#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = len(my_list)
    if a == 0:
        return
    i = a - 1
    while i >= 0:
        print("{:d}".format(my_list[i]))
        i -= 1
