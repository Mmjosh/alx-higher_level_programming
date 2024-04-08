#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key not in a_dictionary:
        return a_dictionary
    if not isinstance(key, str):
        raise TypeError("`key` must be a string")
    del a_dictionary[key]
    return a_dictionary
