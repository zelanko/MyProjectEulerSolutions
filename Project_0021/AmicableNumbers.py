import reuse

def d(int_n):
    divisors = reuse.all_divisors_primes(int_n)
    divisors.remove(int_n)
    return sum(divisors)

results = dict()

for n in range(2, 10000):
    d_n = d(n)
    if n != d_n and d_n < 10000 and d_n > 1:
        results[n] = d_n

amicable_numbers = set()

for k, v in iter(results.items()):
    if v in results and results[v] == k:
        amicable_numbers.add(k)
        amicable_numbers.add(v)

print(sorted(amicable_numbers))
print(sum(amicable_numbers))
