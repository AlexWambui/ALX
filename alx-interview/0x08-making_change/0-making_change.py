#!/usr/bin/python3
"""A module for making change
"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to make
    change for a total amount.

    Args:
      coins: A list of coin values.
      total: The total amount to make change for.

    Returns:
      The fewest number of coins needed to make
      change for the total amount.
    """
    if total <= 0:
        return 0
    remaining_amount = total
    number_of_coins = 0
    coin_index = 0
    sorted_coins = sorted(coins, reverse=True)
    while remaining_amount > 0:
        if coin_index >= len(sorted_coins):
            return -1
        if remaining_amount - sorted_coins[coin_index] >= 0:
            remaining_amount -= sorted_coins[coin_index]
            number_of_coins += 1
        else:
            coin_index += 1
    return number_of_coins
