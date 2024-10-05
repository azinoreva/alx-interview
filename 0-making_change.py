#!/usr/bin/python3
"""
This module defines the makeChange function which solves the coin change problem.
"""

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list of int): A list of coin denominations.
        total (int): The target total amount.

    Returns:
        int: The fewest number of coins needed to meet the total.
            - Returns 0 if the total is 0 or less.
            - Returns -1 if the total cannot be met by any number of coins.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

