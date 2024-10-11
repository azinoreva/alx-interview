#!/usr/bin/python3
"""Module for calculating the perimeter of an island in a grid."""

def island_perimeter(grid):
    """Calculates the perimeter of the island described in the grid.
    
    Args:
        grid (list of list of int): 2D grid where 0 = water, 1 = land.
    
    Returns:
        int: Island perimeter.
    """
    num_rows = len(grid)
    num_cols = len(grid[0])
    total_perimeter = 0

    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == 1:
                if row == 0 or grid[row-1][col] == 0:
                    total_perimeter += 1
                if row == num_rows-1 or grid[row+1][col] == 0:
                    total_perimeter += 1
                if col == 0 or grid[row][col-1] == 0:
                    total_perimeter += 1
                if col == num_cols-1 or grid[row][col+1] == 0:
                    total_perimeter += 1

    return total_perimeter

