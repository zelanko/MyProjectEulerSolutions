from .all_divisors_primes import all_divisors_primes

def properDivisors(integral_number):
    divisors = all_divisors_primes(integral_number)
    divisors.remove(integral_number)
    return divisors
