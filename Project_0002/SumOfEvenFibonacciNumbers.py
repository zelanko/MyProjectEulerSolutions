highestFibonacciNumberToSum = 4000000

fib0, fib1, accumulator = 1, 2, 0

while fib0 <= highestFibonacciNumberToSum:
  if fib0 % 2 == 0: accumulator += fib0
  fib0, fib1 = fib1, fib0 + fib1

print(accumulator)