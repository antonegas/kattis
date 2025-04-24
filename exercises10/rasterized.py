"""
author: Anton Nilsson
testcase 1:
in:
2
2
6

out:
3
11

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

def get_divisors(n: int, primes: list[int]) -> list[int]:
    divisors = {1}

    for prime in primes:
        if n == 1 or prime**2 > n:
            break

        while n % prime == 0:
            divisors.update({prime * divisor for divisor in divisors})
            n = n // prime

    if n != 1:
        divisors.update({n * divisor for divisor in divisors})
    
    return [*divisors]

def phi(n: int, primes: list[int]) -> int:
    result = n

    for prime in primes:
        if n == 1 or prime**2 > n:
            break
        if n % prime != 0:
            continue

        while n % prime == 0:
            n = n // prime
        
        result -= result // prime

    if n > 1:
        result -= result // n

    return result

def rasterized_lines(n: int, primes: list[int]):
    return sum([phi(divisor + 1, primes) for divisor in get_divisors(n, primes)])

if __name__ == "__main__":
    primes = sieve_of_eratosthenes(10**7)

    for _ in range(int(input())):
        print(rasterized_lines(int(input()), primes))