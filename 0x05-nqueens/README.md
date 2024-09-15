Here's a concise README for your N Queens project:

---

# N Queens Solver

This project solves the N Queens puzzle using a backtracking algorithm. The goal is to place N queens on an N×N chessboard so that no two queens attack each other.

## Usage

To run the program, use the following syntax:

```bash
./nqueens.py N
```

- **N**: An integer (≥ 4) representing the size of the chessboard (N×N).

### Example:

```bash
$ ./nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

### Input Validation:
- If **N** is not provided, the program prints:
  ```bash
  Usage: nqueens N
  ```
- If **N** is not a valid integer, the program prints:
  ```bash
  N must be a number
  ```
- If **N** is less than 4, the program prints:
  ```bash
  N must be at least 4
  ```

## Requirements
- Python 3.x
- Only the `sys` module is used.

## Algorithm
The program uses backtracking to explore possible placements of queens row by row, ensuring no queens can attack each other. Each valid solution is printed in the form of a list of [row, column] pairs.

