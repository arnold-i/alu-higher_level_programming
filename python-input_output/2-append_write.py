#!/usr/bin/python3
"""Defines an append_write function."""


def append_write(filename="", text=""):
    """Append a string to a UTF-8 text file and return the char count.

    Args:
        filename: the name of the file to append to.
        text: the string to append.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
