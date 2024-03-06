#!/usr/bin/python3

"""Generates the Pascal’s triangle"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row

    Args:
        n(int): The number of rows of Pascal's Triangle to generate

    Returns:
        list of lists of integers representing the Pascal’s triangle of n
    """
    if  n <= 0:
        return []

    triangle = []

    for row in range(n):
        current_row = [1]
        if  row > 0:
            prev_row = triangle[-1]
            for i in range(1, row):
                current_row.append(prev_row[i - 1] + prev_row[i])
            current_row.append(1)
        triangle.append(current_row)

    return triangle
