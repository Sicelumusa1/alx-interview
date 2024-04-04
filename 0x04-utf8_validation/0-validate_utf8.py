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
        if num_bytes == 0:
            if byte >> 7 == 0b0:
                continue
            elif byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False

            num_bytes -= 1

    return num_bytes == 0
