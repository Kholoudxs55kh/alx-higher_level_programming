#!/usr/bin/python3
"""task 2 adv."""


def add_attribute(objectt, attribute, value):
    """
    Add a new attribute to an object if possible.
    """

    if not hasattr(objectt, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(objectt, attribute, value)
