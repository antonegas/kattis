"""
author: Anton Nilsson
testcase 1 (relative prime):
in:
2
1 2 2 3
151 783 57 278

out:
5 6
31471 217674

testcase 2 (general):
in:
3
10000 23000 9000 23000
10000 23000 10000 23000
1234 2000 746 2002

out:
no solution
10000 23000
489234 2002000

"""

def modular_inverse(a: int, b: int) -> int:
    """
    Calculates the modular inverse of a for the divisor n. Gives -1 if there is no modular inverse.
    Reference: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
    """
    old_r = a
    r = b
    old_s = 1
    s = 0
    old_t = 0
    t = 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    if old_r != 1:
        return -1

    return old_s % b

def modular_add(a: int, b: int, n: int) -> int:
    """
    Calculates the sum of two numbers modolo n.
    """
    return (a + b) % n

def modular_subtract(a: int, b: int, n: int) -> int:
    """
    Calculates the difference between two numbers modolo n.
    """
    return (a - b) % n

def modular_multiply(a: int, b: int, n: int) -> int:
    return (a * b) % n

def modular_divide(a: int, b: int, n: int) -> int:
    b_inverse = modular_inverse(b, n)

    if b_inverse == -1:
        return -1
    
    return (a * b_inverse) % n

def extended_euclidean(a: int, b: int) -> tuple[int, int, int]:
    """
    The extended Euclidean algorithm to get greatest common divisor and the Bézout coefficients.
    Reference: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
    """
    old_r = a
    r = b
    old_s = 1
    s = 0
    old_t = 0
    t = 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_t, old_s

def crt(congruences: list[tuple[int, int]]) -> tuple[int, int]:
    """
    Given a list of congruences (a_i % n_i), where all n_i are relative primes, finds a 
    solution which satisfies all the equations.

    algorithm: The algorithm used is the Chinese remainder theorem. XXX
    time complexity: O(XXX)
    where:
    - n is the XXX
    why:
    - XXX
    reference: https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Generalization_to_non-coprime_moduli

    parameters:
    - congruences: a list of congruences one the form (a, n).
    returns:
    - The integer a which satisfies all congruences and the product of all n_i / gcd(all n_i).
    """

    result = congruences[0]

    for b, n in congruences[1:]:
        a, m = result

        g, v, u = extended_euclidean(m, n)

        if a % g != b % g:
            return -1, -1
        
        M = m * n // g

        x = (((a * v * n) + (b * u * m)) // g) % M

        result = (x, M)

    return result

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()[1:]

    index = 0

    while index < len(lines):
        a0, n0, a1, n1 = map(int, lines[index].split(" "))

        x, K = crt([(a0, n0), (a1, n1)])

        if x == -1:
            output.append("no solution")
        else:
            output.append(f"{x} {K}")

        index += 1

    open(1, "w").write("\n".join(output))