#!/usr/bin/python3
# replaces/adds key/value in a dictionary, "key" will always be a string
# "value" will be any type.If the key exists, the value will be replaced
# if key doesn't exist, it will be created.
def update_dictionary(a_dictionary, key, value):
    if not isinstance(a_dictionary, dict):
        raise TypeError("Input {dictionary}")
    if not isinstance(key, str):
        raise TypeError("`key` must be string")
    a_dictionary[key] = value
    return a_dictionary
