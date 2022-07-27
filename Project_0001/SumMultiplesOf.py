"""Multiples of 3 and 5

Problem 1

https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""
import time
start = time.perf_counter_ns()
multiples = set(range(3, 1000, 3)) | set(range(5, 1000, 5))
sum = sum(multiples)
summed = time.perf_counter_ns()
print("Sum of specified multiples: {0}".format(sum))
printed = time.perf_counter_ns()
total = printed - start
print("Performance(ns):\n\tCalc: {0}\n\tPrint: {1}\n\tTotal: {2} ({3} s)".format(summed - start, printed-summed, total, total/1000000000))
