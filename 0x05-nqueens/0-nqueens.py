#!/usr/bin/python3

"""
A program that solves the N queens problem
"""

import sys


def is_safe(board, row, col, n):
    """
    Checks if it is safe to place a queen at a given position

    Args:
        board (list): current state of the chessboard
        row (int): current row being considered
        col (int): current column being considered
        n (int): size of the board

    Returns:
        bool: True if it's safe to place a queen at a given position
              False otherwise
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is a queen in the left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Chech if there is a queen in the right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens_util(board, row, n):
    """
    Utility function to solve N Queens problem recursively

    Args:
        board (list): current state of the chessboard
        row (int): current row being considered
        n (int): size of the board
    """
    if row == n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens_util(board, row + 1, n)
            board[row][col] = 0


def solve_nqueens(n):
    """
    Solve the N Queens problem for the given board size

    Args:
        n (str): Size of the chessboard represented as a string.
    """
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * n for _ in range(n)]
    solve_nqueens_util(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    solve_nqueens(sys.argv[1])
