#!/usr/bin/python3
# printing a dictionary by ordered keys(all keys are assumed to be
# strings sorted in alphabetical order) only keys at first level are
# sorted, keys of a dictionary inside the main dictionary are not
# sorted. Dictionary values can have any type.
def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary.keys()):
        value = a_dictionary[key]
        if isinstance(value, dict):
            print_sorted_dictionary(value)
        else:
            print("{}: {}".format(key, value))
