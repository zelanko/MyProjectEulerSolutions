"""A unit fraction contains 1 in the numerator. The decimal representation of the unit
fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that
1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its
decimal fraction part."""

from decimal import getcontext, localcontext, ROUND_DOWN, Inexact

def recurrence_pattern(denominator: int, precision: int = 9999):
    """Find recurring pattern of digits in rational number using requested precision."""
    with localcontext() as ctx:
        ctx.prec = precision
        ctx.rounding = ROUND_DOWN

        decimal_fraction = ctx.divide(1, denominator)
        frac = str(decimal_fraction)[2:]
        pattern_confirmed = False
        offset = 0
        length = 1

        while not pattern_confirmed and offset + length <= len(frac):
            offset_and_length = offset + length
            proposed_pattern = frac[offset:offset_and_length]
            if int(proposed_pattern) == 0:
                length += 1
                continue

            find_index = frac.find(proposed_pattern, offset_and_length)
            find_count = frac.count(proposed_pattern, offset)
            if find_index == -1:
                offset += 1
                length = 1
                continue

            if offset_and_length == find_index and find_count == (len(frac) - offset) // length:
                pattern_confirmed = True
                break

            length += 1

    if pattern_confirmed is True:
        return_value = dict(pre=frac[0:offset], recurrence=proposed_pattern)
    else:
        return_value = recurrence_pattern(denominator, precision * 2)

    return return_value

max_pattern_length_n = 0
max_pattern_length = 0

for n in range(2, 1000):
    getcontext().clear_flags()
    decimal_fraction = getcontext().divide(1, n)
    if getcontext().flags[Inexact]:
        pattern = recurrence_pattern(n)
        pattern_length = len(pattern['recurrence'])
        if max_pattern_length < pattern_length:
            max_pattern_length = pattern_length
            max_pattern_length_n = n

        # print(n, len(pattern['recurrence']), decimal_fraction, f"0.{pattern['pre']}({pattern['recurrence']})")
print("value d", "length", sep=' | ')
print(max_pattern_length_n, max_pattern_length, sep=' | ')
