#!/usr/bin/python3
"""Defines a BaseGeometry class with validation."""


class BaseGeometry:
    """Represents base geometry."""

    def area(self):
        """Raise an Exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name: the name of the value (assumed to be a string).
            value: the value to validate.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
