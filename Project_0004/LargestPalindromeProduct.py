"""Largest palindrome product

[Problem 4](https://projecteuler.net/problem=4)

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

def palindromic(value):
    numberString = str(value)
    if numberString.isdigit():
        return numberString == numberString[::-1]
    else:
        return False

bottom = 999
maxPalindrome = 0

for bottom in range(999, 99, -1):
    for x in range(999, bottom - 1, -1):
        if palindromic(bottom * x):
            maxPalindrome = max([maxPalindrome, bottom * x])

print(maxPalindrome)
