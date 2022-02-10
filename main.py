i = 2
j = 3

primes = [2]
upperbound = 1000

while j < upperbound:
    temp = 0
    for k in primes:
        if j % k == 0:
            temp = 1
            break
    if temp == 0:
        primes.append(j)
        print(j)
    j = j + 2

print(primes)
