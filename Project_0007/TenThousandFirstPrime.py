"""# 10001st prime

[Problem 7](https://projecteuler.net/problem=7)

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""

from pyprimes import primes

for n, p in enumerate(primes()):
    if n == 10001:
        print(f'{n}: {p}')
        break
