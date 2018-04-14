"""Circular primes
Problem 35 
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?"""

from pyprimes import primes_below, isprime

empty_set = frozenset()

def circular_shifts(first_number: int):
    """Get the circular shifts for i."""
    shifts = [first_number]
    last = first_number

    s = str(last)
    max_shifts = len(s)
    i = 1
    while i < max_shifts: 
        new_number = int(s[-1] + s[:-1])
        if new_number not in shifts:
            shifts.append(new_number)
        i += 1
        last = new_number
        s = str(last)
    return shifts

def circular_primes(candidate: int):
    """Return the set of circular primes of i."""
    candidates = circular_shifts(candidate)
    for shift in candidates:
        if (not isprime(shift)):
            return empty_set

    return candidates

circular_prime_set = set([2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97])

for x in primes_below(1_000_000):
    if x in circular_prime_set:
        continue

    circular_prime_set = circular_prime_set.union(circular_primes(x))

print(len(circular_prime_set))
