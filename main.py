def prime_generator(n):
    for possiblePrime in range(2, n + 1):
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            yield possiblePrime

for prime in prime_generator(100):
    print(prime)
