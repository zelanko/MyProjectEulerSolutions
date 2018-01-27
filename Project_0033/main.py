"""Digit cancelling fractions

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to
simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling
the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and
containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the
denominator."""
from typing import Tuple
from fractions import Fraction

int_tuple = Tuple[int, int]

def split_digits(num_denom: int_tuple) -> Tuple[int_tuple, int_tuple]:
    return divmod(num_denom[0], 10), divmod(num_denom[1], 10)

non_trivial = list()

for numerator in range(10, 99):
    for denominator in range(numerator + 1, 100):
        split_num, split_denom = split_digits((numerator, denominator))

        # If both are a power of ten ...
        if not split_num[1] and not split_denom[1]:
            continue

        intersection = set(split_num) & set(split_denom)

        # If no digits in common ...
        if not intersection:
            continue

        remove_digit = intersection.pop()

        den_list = list(split_denom)
        den_list.remove(remove_digit)
        denom = den_list[0]

        num_list = list(split_num)
        num_list.remove(remove_digit)
        num = num_list[0]

        # If either number ends up being zero ...
        if not num or not denom:
            continue

        # If the the fractions are equal ...
        if numerator/denominator == num/denom:
            non_trivial.append((num, denom))
            # print(
            #     f'split_digits({numerator}, {denominator}): {split_num}, {split_denom}; intersection: {remove_digit}; num: {num}, denum:{denom}')

num, denom = 1, 1
for n, d in non_trivial:
    num *= n
    denom *= d

print(f'{Fraction(num, denom).denominator}')
