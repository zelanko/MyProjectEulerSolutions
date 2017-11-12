from math import factorial

int_value = factorial(100)

digits = [int(i) for i in str(int_value)]

print(f"100! = {int_value}\nlist {digits}\nsum {sum(digits)}")
