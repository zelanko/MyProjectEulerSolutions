"""Millionth Permutation"""

from itertools import permutations, islice

p = permutations(range(10))

s = islice(p, 999999, 1000000)

result = ""

for d in next(s, None): 
    result += str(d)

print(result)
