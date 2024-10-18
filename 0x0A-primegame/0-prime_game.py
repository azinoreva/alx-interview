#!/usr/bin/python3
def isWinner(x, nums):
    """Determines the winner of the Prime Game."""
    if x <= 0 or not nums:
        return None
    
    max_num = max(nums)
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(max_num ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i: max_num + 1: i] = [False] * len(range(i * i, max_num + 1, i))
    
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + sieve[i]
    
    maria_wins = sum(1 for n in nums if prime_count[n] % 2 != 0)
    ben_wins = x - maria_wins
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
