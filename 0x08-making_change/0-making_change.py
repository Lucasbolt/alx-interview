#!/usr/bin/python3
"""
fewest coins challenge.
"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    coins.sort(reverse=True)
    coins_count = 0

    for coin in coins:
        if total <= 0:
            break
        coins_count += total // coin
        total %= coin

    return coins_count if total == 0 else -1
