#!/usr/bin/python3
"""
This program prints out pascals triangle
"""


def pascal_triangle(n):
    """
    Takes an integer n and returns a list of
    lists representing Pascal's triangle up to n rows.
    """
    pascal_list = [[1]]  # Start with the first row

    counter = 1  # Initialize counter, starting with the second row

    while counter < n:
        new_list = [1]  # Start each new row with a 1

        for x in range(1, len(pascal_list[counter-1])):
            # Sum of the two numbers above in the previous row
            new_list.append(pascal_list[counter-1][x-1] + pascal_list[counter-1][x])

        new_list.append(1)  # End each new row with a 1
        pascal_list.append(new_list)

        counter += 1  # Increment the counter

    return pascal_list

