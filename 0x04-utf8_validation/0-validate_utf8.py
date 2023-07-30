#!/usr/bin/python3
"""
this module defines the utf8-validation function.
"""


def validUTF8(data):
    """
    Checks if a list of integers are valid UTF-8 codepoints.
    """
    skip = 0
    for i, byte in enumerate(data):
        if skip > 0:
            skip -= 1
            continue
        if not 0 <= byte <= 0x10ffff:
            return False
        elif byte <= 0x7f:
            skip = 0
        elif byte >> 6 == 2:
            skip = 1
        elif byte >> 6 == 3:
            skip = 2
        elif byte >> 6 == 4:
            skip = 3
        else:
            return False
    return skip == 0
