#!/usr/bin/python3

"""
Determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding

    Args:
        data: The data to validate
    """
    #  Track the number of bytes expected for the next character
    num_bytes = 0

    #  Iterate through each integer in the data set
    for byte in data:
        # Check if the most significant bit is 0
        if num_bytes == 0:
            if byte >> 7 == 0b0:
                continue  # Valid single-byte character
            elif byte >> 5 == 0b110:
                num_bytes = 1  # Expecting 1 more byte for 2 byte char
            elif byte >> 4 == 0b1110:
                num_bytes = 2  # Expecting 2 more byte for 3 byte char
            elif byte >> 3 == 0b11110:
                num_bytes = 3  # Expecting 3 more byte for 4 byte char
            else:
                return False  # Invalid start byte
        else:
            # Check continuation pattern
            if byte >> 6 != 0b10:
                return False  # Invalid continuation byte

            num_bytes -= 1  # Successfully processed a character
    # Ensure all characters were fully processed
    return num_bytes == 0 and num_bytes != -1
