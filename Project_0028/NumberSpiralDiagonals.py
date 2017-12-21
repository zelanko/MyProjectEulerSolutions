"""Number spiral diagonals
Problem 28 (https://projecteuler.net/problem=28)
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

[21]  22  23  24 [25]
 20  [7]  0  [9]  10
 19   6  [1]  2   11
 18  [5]  4  [3]  12
[17]  16  15  14 [13]

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?"""

# 1, 3, 5, 7, 9, 13, 17, 21, 25
#  1, 1, 1, 1, 3,  3,  3,  3

from itertools import repeat

nth_member = 1
members = [nth_member]
for x in range(2, 1001, 2):
    for y in repeat(x, 4):
        nth_member += y
        members.append(nth_member)

print(sum(members))
