"""
author: Anton Nilsson
testcase 1:
in:
6 9
6 27
20 10000
20 100000
1000 1009

out:
9 divides 6!
27 does not divide 6!
10000 divides 20!
100000 does not divide 20!
1009 does not divide 1000!

"""

def sieve_of_eratosthenes(n: int) -> list[int]:
    prime_array = [False, False] + [True] * (n - 1)

    if n < 2:
        return []
    
    primes = [2]

    for i in range(3, n + 1, 2):
        if prime_array[i]:
            primes.append(i)

            for j in range(i**2, n + 1, i * 2):
                prime_array[j] = False

    return primes

def factorize(n: int, primes: list[int]) -> list[tuple[int, int]]:
    factors = list()

    for prime in primes:
        if n == 1 or prime**2 > n:
            break

        count = 0

        while n % prime == 0:
            count += 1
            n = n // prime

        if count > 0:
            factors.append((prime, count))

    if n > 1:
        factors.append((n, 1))
    
    return factors

def legendres_formula(n: int, primes: list[int]) -> list[tuple[int, int]]:
    factors = list()

    for prime in primes:
        if prime > n:
            break

        count = 0

        k = 1

        while n // prime**k > 0:
            count += n // prime**k
            k += 1

        if count > 0:
            factors.append((prime, count))

    return factors

def factovisors(n: int, m: int, primes: list[int]) -> bool:
    if n == 0:
        return m == 1
    if m == 0:
        return False
    
    m_factors = factorize(m, primes)
    m_primes = [prime for prime, _ in m_factors]
    n_factors = legendres_formula(n, m_primes)

    if len(m_factors) > len(n_factors):
        return False
    
    for m_factor, n_factor in zip(m_factors, n_factors):
        _, m_count = m_factor
        _, n_count = n_factor

        if m_count > n_count:
            return False
        
    return True

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()

    index = 0

    primes = sieve_of_eratosthenes(2**16)

    while index < len(lines):
        n, m = map(int, lines[index].split(" "))

        if factovisors(n, m, primes):
            output.append(f"{m} divides {n}!")
        else:
            output.append(f"{m} does not divide {n}!")

        index += 1

    open(1, "w").write("\n".join(output))