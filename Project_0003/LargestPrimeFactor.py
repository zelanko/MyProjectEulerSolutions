"""Largest prime factor

[Problem 3](https: // projecteuler.net / problem=3)

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

from pyprimes import factors
import time
start = time.perf_counter_ns()
number = 600851475143

largest_prime_factor = max(factors(number))
end = time.perf_counter_ns()
message = "Greatest prime factor of '{0:,d}': '{1:,d}'\nElapsed: {2:,d} ns".format(number, largest_prime_factor, end - start)

print(message)