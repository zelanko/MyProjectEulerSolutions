from num2words import num2words

character_count = 0

for n in range(1, 1001):
    character_count += len(num2words(n, lang='en_GB').replace('-', '').replace(' ', ''))

print(character_count)
