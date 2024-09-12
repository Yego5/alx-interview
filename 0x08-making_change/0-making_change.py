#!/usr/bin/python3
'''
module:
Making Change Algorithm
'''


def makeChange(coins, total):
    '''
    determine the fewest number of coins needed to meet a given amount total
    from a pile of coins of different values...
    '''

    if total <= 0:
        return 0

    else:
        dp = sorted(coins)
        dp.reverse()
        dp_count = 0
        for i in dp:
            while (total >= i):
                dp_count += 1
                total -= i
        if total == 0:
            return dp_count
        return -1

    # if total <= 0:
    #     return 0

    # # list to store the minimum number of coins needed for each amount
    # dp = [float('inf')] * (total + 1)
    # # minimum number of coins needed to make change for 0 is 0
    # dp[0] = 0

    # for coin in coins:
    #     for amount in range(coin, total + 1):
    #         dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # return dp[total] if dp[total] != float('inf') else -1
