for a in range(1, 333):
    minB = a + 1
    maxBExclusive = int((1000 - minB) / 2) + 1

    for b in range(minB, maxBExclusive):
        c = 1000 - b - a
        if a ** 2 + b ** 2 == c ** 2:
            print('{} x {} x {} = {}'.format(a, b, c, a*b*c))
