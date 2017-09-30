# 1 .. 100, inclusive
r = range(1, 101)

sumOfR = sum(r)

sumOfSquaresOfRsMembers = 0

for n in r:
    sumOfSquaresOfRsMembers += n*n

print('(sum(1..100)) ^ 2 = ' + str(sumOfR * sumOfR))

print('sum(1^2..100^2) = ' + str(sumOfSquaresOfRsMembers))

print('difference = ' + str(sumOfR * sumOfR - sumOfSquaresOfRsMembers))