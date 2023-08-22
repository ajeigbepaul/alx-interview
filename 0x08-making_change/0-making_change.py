#!/usr/bin/python3
"""
Main file for testing
"""

def makeChange(coins, total):
    if total <= 0:
        return 0

    # Create a list to store the minimum number of coins needed for each value
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for value in range(coin, total + 1):
            dp[value] = min(dp[value], dp[value - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

# Test cases
print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
