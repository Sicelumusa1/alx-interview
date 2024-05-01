#!/usr/bin/python3

"""
Determine the fewest number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total

    Args:
        coins (List[int]): List of coin denominations
        total (int): Amount to make

    Returns:
        int: Fewest number of coins needed to make the given total
    """
    if total <= 0:
        return 0

    # Create a DP array with total + 1 elements, initialized to infinity
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate over each amount from 1 to total
    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] != float('inf'):
                dp[amount] = min(dp[amount], 1 + dp[amount - coin])
    # Check the result for the target total
    return dp[total] if dp[total] != float('inf') else -1
