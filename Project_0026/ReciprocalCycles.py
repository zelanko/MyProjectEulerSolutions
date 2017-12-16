"""A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part."""

from decimal import Decimal, getcontext
import decimal

precision = 599
getcontext().rounding=decimal.ROUND_DOWN
getcontext().prec = precision

longest_repetition_pattern = 0

for n in range(2, 1000):
    frac = str(Decimal(1) / Decimal(n))[2:][:precision]
    
    if len(frac) == precision:
        pattern_confirmed = False
        offset = 0
        length = 1
        
        while not pattern_confirmed and not offset + length > precision:
            offset_and_length = offset + length
            proposed_pattern = frac[offset:offset_and_length]
            if (int(proposed_pattern) == 0):
                length += 1
                continue

            find_index = frac.find(proposed_pattern, offset_and_length)
            find_count = frac.count(proposed_pattern, offset)
            if (find_index == -1):
                offset += 1
                length = 1
                continue

            if offset_and_length == find_index and find_count == (len(frac) - offset) // length:
                pattern_confirmed = True
                print(f"n: {n}, 0.{frac[0:offset]}({proposed_pattern})")
                break

            length += 1

        if not pattern_confirmed: print(f"No repetition found: {frac}")
    else:
        print(f'n: {n}, 0.{frac}')

        
