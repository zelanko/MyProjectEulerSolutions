"""Coin sums
Problem 31 (https://projecteuler.net/problem=31)

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general
circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?"""

from itertools import repeat, chain, combinations

def TwoPoundsByCoin(coin_value: int):
    return [c for c in repeat(coin_value, 200 // coin_value)]


_1p  = TwoPoundsByCoin(1)
_2p  = TwoPoundsByCoin(2)
_5p  = TwoPoundsByCoin(5)
_10p = TwoPoundsByCoin(10)
_20p = TwoPoundsByCoin(20)
_50p = TwoPoundsByCoin(50)
_1lb = TwoPoundsByCoin(100)
_2lb = TwoPoundsByCoin(200)

all_coins = [c for c in chain(_1p, _2p, _5p, _10p, _20p, _50p, _1lb, _2lb)]

for coin_count in range(1, 201):
    print({c for c in combinations(all_coins, coin_count) if sum(c) == 200})
