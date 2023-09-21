#!/usr/bin/python3
"""
This file contains a function that determines the fewest
number of coins needed to meet a given amount, given a pile
of coins of different values
"""


def makeChange(coins: list, total: int) -> int:
    """Returns the fewest number of coins needed to meet the total"""
    original_total = total
    if total <= 0:
        return 0
    number_of_coins = 0
    count = 1
    for _ in range(len(coins)):
        # print(f'Run {count}')
        # print(f'Coins Available: {coins}')
        max_coin = max(coins)
        # if original_total % max_coin == 0:
        #     no_of_coins = original_total / max_coin
        #     if no_of_coins <= number_of_coins:
        #         return no_of_coins
        # print(f'Max coin: {max_coin}')
        coins.remove(max_coin)
        number_of_denomination = total // max_coin
        # print(f'Number of denomination: {number_of_denomination}')
        number_of_coins += number_of_denomination
        # print(f'Total Number of coins: {number_of_coins}')
        number_left = total % max_coin
        # print(f'Amount left unchanged: {number_left}')
        total = number_left
        # print(total)
        count += 1
        if total == 0:
            return number_of_coins
    return -1
# print('----')
# print(change)
