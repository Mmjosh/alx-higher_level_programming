#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # if a tuple is < 2, use 0 for each missing integer
    if len(tuple_a) < 2:
        tuple_a = tuple_a + (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b = tuple_b + (0,) * (2 - len(tuple_b))
    x = tuple_a[0] + tuple_b[0]
    y = tuple_a[1] + tuple_b[1]
    return (x, y)
