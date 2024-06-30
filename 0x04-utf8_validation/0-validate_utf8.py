#!/usr/bin/python3
""" Module to determince unicode validation
"""


def validUTF8(data):
    """ Determines if a given data set represents a valid UTF-8 encoding.
    """
    num_bytes = 0

    for byte in data:
        if type(byte) != int or byte < 0 or byte > 0x10ffff:
            return False

        byte = byte & 0xFF
        if num_bytes == 0:
            # Determine the number of bytes in this UTF-8 character
            if (byte >> 5) == 0b110:  # 2-byte character
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                num_bytes = 3
            elif (byte >> 7):  # 1-byte character must start with 0
                return False
        else:
            # If this byte is a continuation byte, it must start with 10xxxxxx
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
