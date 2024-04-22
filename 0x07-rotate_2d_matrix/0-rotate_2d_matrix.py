#!/usr/bin/python3

"""
Module to rotate a 2D matrix
"""


def rotate_2d_matrix(matrix):
    """
    Modifies a matrix by rotating it 90 degrees in-place

    Args:
        matrix (list[list[int]]): A matrix to modify

    Returns:
        None
    """
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right

            # Save top-left to a temporal variable
            temp = matrix[top][left + i]

            # Move bottom-left to top-left position
            matrix[top][left + i] = matrix[bottom - i][left]

            # Move bottom-right to bottom-left position
            matrix[bottom - i][left] = matrix[bottom][right - i]

            # Move top-right to bottom-right position
            matrix[bottom][right - i] = matrix[top + i][right]

            # Move temp value to top-right position
            matrix[top + i][right] = temp
        left += 1
        right -= 1
