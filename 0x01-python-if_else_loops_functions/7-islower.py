#!/usr/bin/python3
def islower(c):
    if not c:
        raise ValueError("Input string cannot be empty")
    a = ord('a')
    z = ord('z')
    for char in c:
        if a <= ord(c) <= z:
            return True
    return False
