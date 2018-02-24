"""Sum square difference

[Problem 6](https://projecteuler.net/problem=6)

The sum of the squares of the first ten natural numbers is,

> 1<sup>2</sup> + 2<sup>2</sup> + ... + 10<sup>2</sup> = 385

The square of the sum of the first ten natural numbers is,

> (1 + 2 + ... + 10)<sup>2</sup> = 55<sup>2</sup> = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""


# 1 .. 100, inclusive
r = range(1, 101)

sumOfR = sum(r)

sumOfSquaresOfRsMembers = 0

for n in r:
    sumOfSquaresOfRsMembers += n*n

print('(sum(1..100)) ^ 2 = ' + str(sumOfR * sumOfR))

print('sum(1^2..100^2) = ' + str(sumOfSquaresOfRsMembers))

print('difference = ' + str(sumOfR * sumOfR - sumOfSquaresOfRsMembers))