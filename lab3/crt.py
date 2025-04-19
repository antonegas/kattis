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

def extended_euclidean(a: int, b: int) -> tuple[int, int, int]:
    """
    The extended Euclidean algorithm to get greatest common divisor and the Bézout coefficients.
    
    time complexity: O(log(min(a,b)))
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
    Given a list of congruences (a_i % m_i) finds a solution which satisfies all the equations.

    algorithm: The algorithm used is the Chinese remainder theorem. It uses the Bézout's identity 
    to iteratively calculate a value x which both satisfies the current resulting congruence and 
    the next congruence.
    time complexity: O(n*logm)
    where:
    - n is the number of congruences.
    - m is the maximum m_i from all congruences.
    why:
    - O(n) from iterating over the congruences.
    - O(logm) from the maximum minimum value in the extended Euclidean algorithm time complexity being m.
    reference: https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Generalization_to_non-coprime_moduli

    parameters:
    - congruences: a list of congruences on the form (a, m).
    returns:
    - If there is a solution: the integer x which satisfies all congruences in modolo the product of 
    all m_i / gcd(all m_i).
    - If there is no solution: the tuple (-1, -1).
    """

    result = congruences[0]

    for b, n in congruences[1:]:
        a, m = result

        # Get the greatest common divisor and the Bézout coefficients for the current iteration.
        g, v, u = extended_euclidean(m, n)

        # If a and b are not equal in modolo of their greatest common divisor there is no solution.
        if a % g != b % g:
            return -1, -1
        
        # Use Bézout's identity to calculate x satisfying both congruences.
        M = m * n // g

        x = ((a * v * n) + (b * u * m)) // g % M

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