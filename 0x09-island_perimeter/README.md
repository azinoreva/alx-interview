Island Perimeter
This module provides a function to calculate the perimeter of an island represented in a 2D grid.

Function
island_perimeter(grid)
Calculates the perimeter of an island in a grid where:

0 represents water
1 represents land
Parameters:
grid: A list of lists (2D grid) of integers where each element is either 0 or 1.
Returns:
int: The total perimeter of the island.
Example:
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

print(island_perimeter(grid))  # Output: 12

Requirements
Python 3.x
