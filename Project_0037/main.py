"""The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes."""

from pyprimes import isprime, primes_above

def truncates(n: int):
    mystr = str(n)
    mystrlen = len(mystr)
    for x in range(1, mystrlen):
        yield int(mystr[x:mystrlen])
        yield int(mystr[0:x])

truncatable_primes = set()

for root_prime in primes_above(7):
    complex_found = False
    for truncate in truncates(root_prime):
        if complex_found:
            break
        complex_found = not(isprime(truncate))

    if not(complex_found):
        print(root_prime)
        truncatable_primes.add(root_prime)
        if len(truncatable_primes) == 11:
            break

print()
print("Sum: ", sum(truncatable_primes))
