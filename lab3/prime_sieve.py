"""
author: Anton Nilsson
testcase 1:
in:
9973 6
1
2
3
4
9972
9973

out:
1229
0
1
1
0
0
1

"""

def get_bit(array: bytearray, index: int):
    """
    Get the value of a specific bit in a bytearray.
    """
    return int(not bool(array[index >> 3] & (1 << (index % 8))))

def clear_bit(array: bytearray, index: int):
    """
    Clears a value of a specific bit in a bytearray.
    """
    array[index >> 3] = array[index >> 3] | (1 << (index % 8))

def set_bit(array: bytearray, index: int):
    """
    Sets a value of a specific bit in a bytearray.
    """
    array[index >> 3] = array[index >> 3] & ~(1 << (index % 8))

def sieve_of_eratosthenes(n: int) -> tuple[bytearray, int]:
    """
    Finds all prime numbers less than or equal to n.

    algorithm: The algorithm used is sieve of Eratosthenes. It works by iterativly seeing 
    if a number has not been marked as not being prime. If a number p is prime then all 
    numbers p + p * m can be marked as not being prime.
    time complexity: O(n*loglogn)
    where:
    - n is the number of values which is checked to be prime or not.
    why:
    - O(n) from the outer loop.
    - O(n*loglogn) from the inner loop running n/p iterations per prime number p. There are 
    approximately n/ln(n) primes less than or equal to n and the k:th prime is roughly equal 
    to k*ln(k). The total number of iterations can then be approximated by the sum from 2 to 
    n/ln(n) over n/k*ln(k) which can in turn be approximated by an integral to be 
    roughly n*ln(ln(n)).
    - O(n+n*loglogn) = O(n*loglogn).
    reference: https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html#implementation

    parameters:
    - n: the value which the search for prime numbers should go up to.
    returns:
    - A bytearray where a bit in that array indicates if the corresponding number is prime 
    and the number of primes and the number of primes less than or equal to n.
    """

    # Initialize a bytearray where a 0 represents that a number is prime. 
    # Start the count at one since we start counting primes from three and up.
    prime_array = bytearray(n // 8 + 1)
    count = 1

    # 0 and 1 are not prime numbers.
    clear_bit(prime_array, 0)
    clear_bit(prime_array, 1)

    # If n is less than 2 there is no prime numbers less than or equal to n.
    if n < 2:
        return prime_array, 0

    # Seperate loop to for numbers divisible by two to speed up the next loop.
    for i in range(4, n + 1, 2):
        clear_bit(prime_array, i)

    # Loop through numbers from three up to n to check if they are prime.
    # If the number is prime mark all numbers divisible by it as non-prime.
    for i in range(3, n + 1, 2):
        if get_bit(prime_array, i):
            count += 1

            for j in range(i**2, n + 1, i):
                clear_bit(prime_array, j)

    return prime_array, count

if __name__ == "__main__":
    n, q = map(int, input().split(" "))

    prime_array, prime_count = sieve_of_eratosthenes(n)

    print(prime_count)

    for _ in range(q):
        print(get_bit(prime_array, int(input())))