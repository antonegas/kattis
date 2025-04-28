"""
author: Anton Nilsson
testcase 1:
in:
5
10 5
10 7
1337 23
123454321 42
999999937 142857133

out:
IMPOSSIBLE
3
872
14696943
166666655

"""

def extended_euclidean(a: int, b: int) -> tuple[int, int, int]:
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
    result = congruences[0]

    for b, n in congruences[1:]:
        a, m = result

        g, v, u = extended_euclidean(m, n)

        if a % g != b % g:
            return -1, -1
        
        M = m * n // g

        x = ((a * v * n) + (b * u * m)) // g % M

        result = (x, M)

    return result

if __name__ == "__main__":
    for _ in range(int(input())):
        K, C = map(int, input().split())

        if C == 1:
            print(K + 1)
            continue
        if K == 1:
            print(1)
            continue

        x, _ = crt([(1, K), (0, C)])
        result = x // C

        if x == -1 or result > 1000000000:
            print("IMPOSSIBLE")
        else:
            print(result)