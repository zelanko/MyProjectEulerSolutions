"""solution confirmed in this document. I don't have a good computational way to calculate it."""
from math import factorial

def paths_for_square_grid(side_length):
    """Calculate the count of possible paths through a square grid of given side_length"""
    return factorial(side_length * 2) // (factorial(side_length) * factorial(side_length))

axis_length = 20
paths = paths_for_square_grid(axis_length)
print(paths)
