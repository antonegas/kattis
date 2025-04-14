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

def crt(congruences: list[tuple[int, int]]) -> tuple[int, int]:
    """
    Given a list of congruences (a_i % n_i) finds a solution a, which satisfies all congruences if one such exists.

    algorithm: The algorithm used is the Chinese remainder theorem. XXX
    time complexity: O(XXX)
    where:
    - n is the 
    why:
    - XXX
    reference: https://cp-algorithms.com/algebra/chinese-remainder-theorem.html#implementation

    parameters:
    - congruences: a list of congruences one the form (a, n)
    returns:
    - If there is a solution: the integer a which satisfies all congruences and the product of all n_i.
    - If there is no solution: negative one and zero.
    """
    
    N = 1

    for _, n in congruences:
        N = N * n

    solution = 0

    for a, n in congruences:
        solution = (solution + a * N // n % N * modular_inverse(N // n, n)) % N

    return solution, N

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()[1:]

    index = 0

    while index < len(lines):
        a0, n0, a1, n1 = map(int, lines[index].split(" "))

        x, K = crt([(a0, n0), (a1, n1)])

        output.append(f"{x} {K}")

        index += 1

    open(1, "w").write("\n".join(output))