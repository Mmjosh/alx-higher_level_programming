#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = len(my_list)
    if a == 0:
        return
    for x in range(a - 1, -1, -1):
        print("{:d}".format(my_list[x]))
