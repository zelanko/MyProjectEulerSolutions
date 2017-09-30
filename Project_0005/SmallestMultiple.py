candidate = 2520

found = False

while not found:
    for n in range(2, 21):
        if candidate % n != 0:
            candidate += 1
            break
    else:
        found = True

print(candidate)
