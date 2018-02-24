"""Summation of primes

[Problem 10](https://projecteuler.net/problem=10)

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""

from pyprimes import primes_below

print(sum(primes_below(2000000)))