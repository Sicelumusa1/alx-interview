#!/usr/bin/python3

"""
Defines a function that returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid

    Args:
        grid (List[int]): matrix representing the island

    Returns:
        int: perimeter
    """
    row_length = len(grid)
    col_length = len(grid[0])

    perim = 0
    connections = 0

    for i in range(0, row_length):
        for j in range(0, col_length):
            if grid[i][j] == 1:
                # Add all 4 sides
                perim += 4

                # Check the top
                if i != 0 and grid[i - 1][j] == 1:
                    # There is a connection
                    connections += 1
                # Check the left
                if j != 0 and grid[i][j - 1] == 1:
                    # There is a connection
                    connections += 1
    return perim - (connections * 2)
