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
    if n <= 1:
        return 0

    operations = 0

    # Check if n is even
    while n % 2 == 0:
        n //= 2
        operations += 2

    # if n is odd, find the largest divisor other 1
    divisor = 3
    while divisor * divisor <= n:
        while n % divisor == 0:
            n //= divisor
            operations += divisor
        divisor += 2

    # If n is still greater than 1, it's a prime number
    if n > 1:
        operations += n

    return operations
