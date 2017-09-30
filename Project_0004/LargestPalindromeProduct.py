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