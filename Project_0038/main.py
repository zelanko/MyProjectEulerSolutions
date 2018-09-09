"""Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?"""

def is_pandigital(number):
    number = str(number)
    return  number.isnumeric() and len(number) == 9 and number.count('1') == 1 and number.count('2') == 1 and number.count('3') == 1 and number.count('4') == 1 and number.count('5') == 1 and number.count('6') == 1 and number.count('7') == 1 and number.count('8') == 1 and number.count('9') == 1 and number.count('0') == 0 

for i in range(193, 1000001):
    number = ""
    for y in range(1,9):
        number += str(i * y)

        if int(number) > 987654321:
            break

        if is_pandigital(number):
            print(number)
        
        
    
