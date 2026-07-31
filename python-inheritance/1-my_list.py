#!/usr/bin/python3
"""Defines a MyList class that inherits from list."""


class MyList(list):
    """Represents a list with a sorted-print method."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
