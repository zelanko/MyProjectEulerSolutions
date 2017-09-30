from pyprimes import primes

n = 1

for p in primes():
    if n == 10001:
        print('{}: {}'.format(n, p))
        break
    n += 1