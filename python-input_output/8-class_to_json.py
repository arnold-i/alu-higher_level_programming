#!/usr/bin/python3
"""Defines a class_to_json function."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON serialization.

    Args:
        obj: an instance of a class with serializable attributes.
    """
    return obj.__dict__
