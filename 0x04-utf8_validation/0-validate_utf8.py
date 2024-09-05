#!/usr/bin/python3
"""
This module provides a function to validate whether a given dataset
of integers represents a valid UTF-8 encoding.
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list of int): A list where each integer represents 1 byte of data.
                            Each integer should be in the range [0, 255].

    Returns:
        bool: True if data represents a valid UTF-8 encoding, otherwise False.

    A character in UTF-8 can be 1 to 4 bytes long. The first byte determines
    how many bytes are in the character, and the subsequent bytes must follow
    the pattern 10xxxxxx for multi-byte characters.
    """
    
    num_bytes = 0
    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        byte = byte & 0xFF

        if num_bytes == 0:
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7):
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False
            num_bytes -= 1

    return num_bytes == 0

