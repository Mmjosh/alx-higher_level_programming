#!/usr/bin/python3
def islower(c):
    a = ord('a')
    z = ord('z')
    for char in c:
        if a <= ord(c) <= z:
            return True
    return False
