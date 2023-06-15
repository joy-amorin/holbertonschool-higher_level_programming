#!/usr/bin/python3
"""
function that prints a text with 2 new lines
after each of these characters: ., ? and :

"""


def text_indentation(text):
    """
    function
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in (".", "?", ":"):
            print("\n")
            while text[i + 1] == ' ':
                i += 1
        i += 1
