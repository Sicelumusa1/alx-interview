#!/usr/bin/python3

"""
Calculates the fewest number of operations needed to result in
exactly n H characters
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in
    exactly n H characters

    Args:
        n (int): number of H charactes desired

    Returns:
        int: Feweat number of operations
    """
    if n <= 0:
        return 0

    operations = 0

    current_chars = 1

    clipboard = 0

    while current_chars < n:
        if n % current_chars == 0:
            clipboard = current_chars
        current_chars += clipboard
        operations += 1

    return operations
