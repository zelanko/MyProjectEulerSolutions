"""Double-base palindromes
Problem 36 
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)"""

def is_palendrome(number: int):
    int_str = str(number)
    return int_str == int_str[::-1]
    
def is_binary_palindrome(number: int):
    bin_str = bin(number)[2:]
    return bin_str == bin_str[:: - 1]
    
print(sum([x for x in range(1, 1_000_000) if is_palendrome(x) and is_binary_palindrome(x)]))