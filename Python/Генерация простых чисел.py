def get_primes_optimized(n):
    sieve = [False if i % 2 == 0 else True for i in range(n)]
    primes = [2]
    for p in range(3, n, 2):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n, p * 2):
                sieve[i] = False
    return primes