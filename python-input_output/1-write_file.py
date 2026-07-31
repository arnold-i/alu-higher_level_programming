#!/usr/bin/python3
"""Defines a write_file function."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file and return the char count.

    Args:
        filename: the name of the file to write to.
        text: the string to write.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
