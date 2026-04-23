primes = list(range(2, 101))

for i in range(2, 11):
    for j in primes:
        if j != i and j % i == 0:
            primes.remove(j)

print(primes)