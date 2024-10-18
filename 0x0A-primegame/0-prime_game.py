#!/usr/bin/python3
def isWinner(x, nums):
    """Determines the winner of the Prime Game"""
    if x <= 0 or not nums:
        return None
    
    # Find the maximum number in nums
    max_num = max(nums)
    
    # Step 1: Precompute primes using Sieve of Eratosthenes
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_num ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = False
    
    # Step 2: Compute the number of primes up to each number
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if sieve[i] else 0)
    
    # Step 3: Simulate each game
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1  # Ben wins if the number of primes is even
        else:
            maria_wins += 1  # Maria wins if the number of primes is odd
    
    # Step 4: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

