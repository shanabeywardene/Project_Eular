import math

i = 2
j = 3

primes = [2]
upperbound = 100000

while j < upperbound:
    temp = 0
    l = int(math.sqrt(j))

    for k in range(l):
        if j % primes[k] == 0:
            temp = 1
            break
    if temp == 0:
        primes.append(j)
        print(j)
    j = j + 2

print(primes)