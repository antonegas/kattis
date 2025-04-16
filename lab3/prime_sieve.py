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
    return int(not bool(array[index >> 3] & (1 << (index % 8))))

def clear_bit(array: bytearray, index: int):
    array[index >> 3] = array[index >> 3] | (1 << (index % 8))

def set_bit(array: bytearray, index: int):
    array[index >> 3] = array[index >> 3] & ~(1 << (index % 8))

def sieve_of_eratosthenes(n: int) -> tuple[bytearray, int]:
    """
    XXX description XXX

    algorithm: XXX
    time complexity: O(XXX)
    space complexity: O(XXX)
    where:
    - n is the XXX
    why:
    - XXX
    reference: XXX

    parameters:
    - XXX
    returns:
    - XXX
    """

    prime_array = bytearray(n // 8 + 1)
    count = 0

    # 0 and 1 are not prime numbers.
    clear_bit(prime_array, 0)
    clear_bit(prime_array, 1)

    for i in range(2, n + 1):
        if get_bit(prime_array, i):
            count += 1

            for j in range(i**2, n + 1, i):
                clear_bit(prime_array, j)

    return prime_array, count

if __name__ == "__main__":
    n, q = map(int, input().split(" "))

    prime_array, count = sieve_of_eratosthenes(n)

    print(count)

    for _ in range(q):
        print(get_bit(prime_array, int(input())))