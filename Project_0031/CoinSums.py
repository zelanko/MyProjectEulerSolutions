"""Coin sums
Problem 31 (https://projecteuler.net/problem=31)

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general
circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?"""

from itertools import combinations, chain, repeat

target_value = 200

COINS = [1, 2, 5, 10, 20, 50, 100, 200] 

COIN_INDEX = {coin: index for index, coin in enumerate(COINS)}

def sum_coin_list(coin_list: list):
    return sum(coin_list[i] * COINS[i] for i in range(0, len(coin_list)))
   
coin_combination_count = 0

# with open('out.txt', mode='w') as file:
target_2lb_value = target_value
max_2lb_coins = target_2lb_value // 200
for coins_2lb in range(0, max_2lb_coins + 1):
    target_1lb_value = target_2lb_value - coins_2lb * 200
    max_1lb_coins = target_2lb_value // 100
    for coins_1lb in range(0, max_1lb_coins + 1):
        target_50p_value = target_1lb_value - coins_1lb * 100
        max_50p_coins = target_1lb_value // 50
        for coins_50p in range(0, max_50p_coins + 1):
            target_20p_value = target_50p_value - coins_50p * 50
            max_20p_coins = target_20p_value // 20
            for coins_20p in range(0, max_20p_coins + 1):
                target_10p_value = target_20p_value - coins_20p * 20
                max_10p_coins = target_10p_value // 10
                for coins_10p in range(0, max_10p_coins + 1):
                    target_5p_value = target_10p_value - coins_10p * 10
                    max_5p_coins = target_5p_value // 5
                    for coins_5p in range(0, max_5p_coins + 1):
                        target_2p_coins = target_5p_value - coins_5p * 5
                        max_2p_coins = target_2p_coins // 2
                        for coins_2p in range(0, max_2p_coins + 1):
                            # coins = (target_2p_coins - 2 * coins_2p, coins_2p, coins_5p, coins_10p, coins_20p, coins_50p, coins_1lb, coins_2lb)
                            # file.write(f"{coins}; sum: {sum_coin_list(coins)}\n")
                            coin_combination_count += 1

print(coin_combination_count)
