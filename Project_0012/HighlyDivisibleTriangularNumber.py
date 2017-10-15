import time

elapsed = 0

def all_divisors(n):
  t0 = time.perf_counter()
  r = [i for i in range(1, n // 2 + 1) if n % i == 0]
  r.append(n)
  elapsed = time.perf_counter() - t0
  return r, elapsed

maxDivisorCount, n, nthValue, divisorList, divisorCount = 1, 1, 1, [1], 1

while divisorCount < 150:
  n += 1
  nthValue += n
  divisorList, elapsed = all_divisors(nthValue)
  divisorCount = len(divisorList)

  # if divisorCount > maxDivisorCount:
  #   maxDivisorCount = divisorCount
  print('nthValue: {}, n: {}, divisorCount: {}, elapsed: {}'.format(nthValue, n, divisorCount, elapsed))
  print(divisorList)



print(nthValue)
