"""Digit fifth powers
Problem 30 (https://projecteuler.net/problem=30)
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits."""

from sys import maxsize

def i_eq_sum_of_digits_to_nth_power(i: int, pwr: int = 4):
    seq_of_pwrs = [int(x) ** pwr for x in str(i)]
    return sum(seq_of_pwrs) == i

written_as_nth_power_sum = [n for n in range(2, 200000) if i_eq_sum_of_digits_to_nth_power(n, 5)]

print(written_as_nth_power_sum)
print(f"sum: {sum(written_as_nth_power_sum)}")    
