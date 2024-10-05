#!/usr/bin/python3
"""
Main file for testing the makeChange function
"""

makeChange = __import__('0-making_change').makeChange

# Test cases
print(makeChange([1, 2, 25], 37))  # Expected output: 7 (25 + 10 + 2)
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Expected output: -1 (not possible)
print(makeChange([1, 5, 10, 25], 63))  # Expected output: 6 (25 + 25 + 10 + 1 + 1 + 1)
print(makeChange([1, 5, 10], 0))  # Expected output: 0 (no change needed)
print(makeChange([5, 10, 20], 3))  # Expected output: -1 (not possible to make 3)

