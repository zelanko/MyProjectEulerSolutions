"""Smallest multiple

[Problem 5](https://projecteuler.net/problem=5)

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

candidate = 2520

found = False

while not found:
    for n in range(2, 21):
        if candidate % n != 0:
            candidate += 1
            break
    else:
        found = True

print(candidate)
