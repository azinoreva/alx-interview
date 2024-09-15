#!/usr/bin/python3
import sys
from typing import List

def print_solution(solution: List[List[int]]) -> None:
    """
    Prints a single solution to the N queens puzzle.

    Args:
        solution (List[List[int]]): A list of lists representing the positions of queens.
                                    Each sublist contains [row, column] for one queen.
    """
    print(solution)

def is_safe(board: List[int], row: int, col: int, N: int) -> bool:
    """
    Determines if it's safe to place a queen at a given position.

    Args:
        board (List[int]): A list where the index represents the row and the value
                           at that index represents the column of the queen.
        row (int): The row where the queen is being placed.
        col (int): The column where the queen is being placed.
        N (int): The size of the chessboard (N x N).

    Returns:
        bool: True if it's safe to place the queen, False otherwise.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(board: List[int], row: int, N: int) -> None:
    """
    Solves the N queens puzzle using backtracking.

    Args:
        board (List[int]): A list where the index represents the row and the value
                           at that index represents the column of the queen.
        row (int): The current row being processed.
        N (int): The size of the chessboard (N x N).
    """
    if row == N:
        solution = [[i, board[i]] for i in range(N)]
        print_solution(solution)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens(board, row + 1, N)

def nqueens(N: int) -> None:
    """
    Initializes the board and starts solving the N queens puzzle.

    Args:
        N (int): The size of the chessboard (N x N).
    """
    board = [-1] * N
    solve_nqueens(board, 0, N)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(N)

