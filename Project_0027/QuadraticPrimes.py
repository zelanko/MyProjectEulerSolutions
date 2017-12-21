"""Taken from https://projecteuler.net/problem=27

Considering quadratics of the form:

    n² + an + b, where |a| < 1000 and |b| ≤ 1000

    where |n| is the modulus / absolute value of n
    e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the
maximum number of primes for consecutive values of n, starting with n = 0."""
from itertools import product, count
from pyprimes import isprime

min_length = 0

for a, b in product(range(-999, 1000), range(-1000, 1001)):
    for n in count():
        result = n * n + a * n + b
        if isprime(result) is False:
            if min_length < n - 1:
                min_length = n - 1
                print(a, b, min_length)
            break
