"""Pandigital products

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly
once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand,
multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand / multiplier / product identity can be written as
a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in
your sum.
"""

# We store a product if,
# sorted(f"{multiplier}{multiplicand}{product}"}) == ['1','2','3','4','5','6','7','8','9']

import sys
sys.path.append('..')
from reuse import properDivisors

from itertools import count
from pyprimes import factors

products_to_sum = set()

factors_seen = set()
for p in range(4000, 10000):
    factors_seen.clear()
    for divisor in properDivisors(p):
        # if divisor in factors_seen:
        #     break

        multiplicand = p // divisor

        factors_seen.add(multiplicand)

        identity_digit_string = f"{divisor}{multiplicand}{p}"
        if len(identity_digit_string) == 9 and sorted(identity_digit_string) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            products_to_sum.add(p)
            print(f"{divisor} * {multiplicand} = {p}; sum: {sum(products_to_sum)}")
            break





