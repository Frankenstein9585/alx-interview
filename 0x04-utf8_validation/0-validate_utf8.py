#!/usr/bin/python3
"""This file contains a function that checks valid UTF-8 encoding"""


def validUTF8(data):
    """Determines if a given data set
    represents a valid UTF-8 encoding"""
    is_utf8 = 0
    for int_ in data:
        byte = int_ & 255
        if is_utf8:
            if byte >> 6 != 2:
                return False
            is_utf8 -= 1
            continue
        while (1 << abs(7 - is_utf8)) & byte:
            is_utf8 += 1
        if is_utf8 == 1 or is_utf8 > 4:
            return False
        is_utf8 = max(is_utf8 - 1, 0)
    return is_utf8 == 0
