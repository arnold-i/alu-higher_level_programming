#!/usr/bin/python3
"""Defines an is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance or subclass instance of a_class.

    Args:
        obj: the object to check.
        a_class: the class to match against.
    """
    return isinstance(obj, a_class)
