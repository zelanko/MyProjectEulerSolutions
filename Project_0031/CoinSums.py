"""Coin sums
Problem 31 (https://projecteuler.net/problem=31)

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general
circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?"""

from itertools import filterfalse 

def unique_non_terminals(iterable):
    """iterator for unique non-terminals"""
    # 1 is always a terminal
    seen = {1}

    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item

def derive_valid_patterns(pattern: tuple):
    """Derive single-change patterns from the provided pattern.
    
    Keyword arguments:
    pattern -- tuple 

    Keyword returns:
    returns a list of tuples
    """
    new_patterns = set()

    for value in unique_non_terminals(pattern):
        derivative_pattern = list(pattern)
        derivative_pattern.remove(value)
        derivative_pattern.extend(TRANSFORMATIONS[value])
        new_patterns.add(tuple(sorted(derivative_pattern)))
    
    return new_patterns

TRANSFORMATIONS = {
    200: (100, 100),
    100: (50, 50),
    50: (10, 20, 20),
    20: (10, 10),
    10: (5, 5),
    5: (1, 2, 2),
    2: (1, 1)
}

pattern_queue = {(200,)}

valid_patterns = set()

# Empty sequense == False
while pattern_queue:
    COIN_PATTERN = pattern_queue.pop()
    valid_patterns.add(COIN_PATTERN)
    for p in derive_valid_patterns(COIN_PATTERN):
        if (p not in valid_patterns and p not in pattern_queue):
            pattern_queue.add(p)

# # Output the sorted results.
# with open("./patterns.txt", "w") as out:
#     for p in sorted(list(valid_patterns), reverse=True):
#         out.write(f"Sum:{sum(p)};{p}\n")

print(len(valid_patterns))
