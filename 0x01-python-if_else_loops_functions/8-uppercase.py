#!/usr/bin/python3
def uppercase(str):
    if not str:
        return
    str1 = ''
    for c in str:
        if 'a' <= c <= 'z':
            str1 += chr(ord(c) - 32)
        else:
            str1 += c
    print("{}".format(str1), end='')
    print()
