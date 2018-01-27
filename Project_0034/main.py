"""Digit factorials

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included."""

from math import factorial


# Tested 10..9999999; 145..40585 is the smallest range including all such numbers.
equality_found = [n for n in range(145, 40586) if sum(map(factorial, map(int, str(n)))) == n]

print(f'{equality_found}; sum: {sum(equality_found)}')
