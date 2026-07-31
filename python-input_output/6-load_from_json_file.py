#!/usr/bin/python3
"""Defines a load_from_json_file function."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file.

    Args:
        filename: the name of the JSON file to read.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
