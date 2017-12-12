"""NonAbundantSums"""
import sys
sys.path.append('..')

from reuse import properDivisors

final_sum = sum(range(1,12))

abundant_numbers = list()

sums_of_two_abundant = set()

for x in range(12, 28124):
    if x < sum(properDivisors(x)):
        abundant_numbers.append(x)
        for y in abundant_numbers:
            if (x + y < 28124):
                sums_of_two_abundant.add(x + y)
    if x not in sums_of_two_abundant:
        final_sum += x

print(final_sum)
