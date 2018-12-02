from test_framework import generic_test

import math

# WIP

# Given n, return all primes up to and including n.
def generate_primes(n):
    sieve = [True] * (n+1)
    primes = []
    for i in range(2, n+1):
        if not sieve[i]: continue
        primes.append(i)
        for j in range(i+i, n+1, i):
            sieve[j] = False

    return primes

def generate_primes1(n):
    primes = []
    for i in range(2, n+1):
        is_prime = True
        max_dev = math.sqrt(i)
        for prime in primes:
            if prime > max_dev: break
            if not (i % prime):
                is_prime = False
                break
        if is_prime: primes.append(i)

    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("prime_sieve.py", "prime_sieve.tsv",
                                       generate_primes))
