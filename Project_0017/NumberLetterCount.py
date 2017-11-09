from num2words import num2words

# 'one', 'two', ..., 'twentyone', ..., 'onethousand'
numbers = [num2words(n, lang='en_GB').replace('-', '').replace(' ', '') for n in range(1, 1001)]

# "onetwo...twentyone...onethousand"
num_string = ''.join(numbers)

print(len(num_string))
