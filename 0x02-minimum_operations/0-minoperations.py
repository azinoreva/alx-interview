#!/usr/bin/python3
""" Script that computes a minimum operations
    Needed in a CopyAll - Paste task
"""


def minOperations(n):
    """
    This computes the minimum number
    of operations for tasks

    Args:
        n: input value
        Flist: List to save the operations
    Returns sum of operations
    """
    if n < 2:
        return 0
    Flist = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                Flist.append(i)
    return sum(Flist)
