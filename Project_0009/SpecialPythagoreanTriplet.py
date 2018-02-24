"""Special Pythagorean triplet

[Problem 9](https://projecteuler.net/problem=9)

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc."""
for a in range(1, 333):
    minB = a + 1
    maxBExclusive = int((1000 - minB) / 2) + 1

    for b in range(minB, maxBExclusive):
        c = 1000 - b - a
        if a ** 2 + b ** 2 == c ** 2:
            print(f'{a} x {b} x {c} = {a*b*c}')
