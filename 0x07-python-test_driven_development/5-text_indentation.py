#!/usr/bin/python3

"""
This module contains a function `text_indentation`
which indents text by 2 newlines after specific characters
"""


def text_indentation(text):
    """
    indents text after the characters, ".", "?" and ":"
    Args:
        text(str) text to be formatted
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in ['.', '?', ':']:
            result += "\n\n"
            i += 1
            # skipping any following spaces
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1  # skipping the special character itself
    print(result, end='')
