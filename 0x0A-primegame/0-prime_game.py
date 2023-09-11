#!/usr/bin/python3
"""
this module defines the prime game program
"""


def isWinner(x, nums):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def can_win(n):
        if n <= 1:
            return False
        if dp[n] != -1:
            return dp[n]

        for i in range(2, n + 1):
            if is_prime(i) and n % i == 0:
                # Try removing i and check if the opponent can win
                if not can_win(n - i):
                    dp[n] = True
                    return True

        dp[n] = False
        return False

    max_wins = 0
    winner = None

    for n in nums:
        dp = [-1] * (n + 1)
        maria_wins = can_win(n)

        if maria_wins:
            max_wins += 1

    if max_wins == 0:
        return None
    elif max_wins % 2 == 0:
        return "Ben"
    else:
        return "Maria"
