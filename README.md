# Coin Change Problem

## Description
This project tackles the classic **coin change problem** using dynamic programming. The goal is to determine the fewest number of coins required to make up a given total amount using a list of coin denominations.

## Function Prototype
```python
def makeChange(coins, total):
Parameters
coins: A list of integers representing the coin denominations available.
total: An integer representing the target amount.
Return
The function returns the minimum number of coins required to make up the total.
If the total is 0 or less, it returns 0.
If it is impossible to make up the total with the given coins, it returns -1.
Example

makeChange([1, 2, 25], 37)
# Returns 7 (25 + 10 + 2)

makeChange([1256, 54, 48, 16, 102], 1453)
# Returns -1 (not possible to make 1453 with the given coins)
Usage

Make sure to use Python 3.
The script is written in PEP 8 style.
Ensure the file has executable permissions.
Run the following commands to test:


Files
0-making_change.py: Contains the makeChange function that implements the dynamic programming approach.
0-main.py: A test file for validating the function with different inputs.
Requirements

Python 3.4 or later.
All code should be executable and follow PEP 8 guidelines.
Concepts Covered
Dynamic programming.
Algorithmic optimization.
Time and space complexity analysis.
