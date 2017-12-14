previous = 0
current = 1
index = 1

while len(str(current)) < 1000:
    temp = current
    current += previous
    previous = temp
    index += 1

print(index)