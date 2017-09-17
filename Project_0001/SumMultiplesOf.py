multiples = set(range(3, 1000, 3)) | set(range(5, 1000, 5))

accumulator = 0

for i in multiples:
  accumulator += i

print(accumulator)
