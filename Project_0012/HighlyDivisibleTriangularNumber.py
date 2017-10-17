from pyprimes import factors
from itertools import chain, combinations

def all_divisors_primes(n):
  finalset = []
  primefactors = factors(n)
  powerset = chain.from_iterable(combinations(primefactors, r) for r in range(1, len(primefactors) + 1))
  for s in powerset:
    divisor = 1
    for d in s:
      divisor *= d
    finalset.append(divisor)
  
  finalset.insert(0, 1)
  
  return list(set(finalset))

n = 0
nthValue = 0
divisor_count = 0
max_divisor_count = 0

while divisor_count < 500:
  n += 1
  nthValue += n
  divisor_count = len(all_divisors_primes(nthValue))

print(nthValue)
