from math import pow

product = int(pow(2, 1000))

sum_of_digits = 0 
for digit in str(product):
    sum_of_digits += int(digit)

print(sum_of_digits)