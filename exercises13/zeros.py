"""
author: Anton Nilsson
testcase 1:
in:
10 11
100 200
0 500
1234567890 2345678901
0 4294967295
-1 -1

out:
1
22
92
987654304
3825876150

"""

from math import log10, floor

def how_many_zeros(m: int, n: int) -> int:
    zeros = 0

    if m == 0:
        zeros += 1

    for k in range(1, floor(log10(n)) + 2):
        kth_digit = (n % 10**k) // 10**(k - 1)

        if k == 1 or kth_digit != 0:
            zeros += 10**(k - 1) * floor(n / 10**k)
        else:
            zeros += 10**(k - 1) * (floor(n / 10**k) - 1) + n + 1 - 10**k * floor(n / 10**k)

    if m - 1 < 1:
        return zeros

    for k in range(1, floor(log10(m - 1)) + 1):
        kth_digit = ((m - 1) % 10**k) // 10**(k - 1)

        if k == 1 or kth_digit != 0:
            zeros -= 10**(k - 1) * floor((m - 1) / 10**k)
        else:
            zeros -= 10**(k - 1) * (floor((m - 1) / 10**k) - 1) + m - 10**k * floor(m / 10**k)

    return zeros

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()[:-1]

    index = 0

    while index < len(lines):
        m, n = map(int, lines[index].split(" "))
        output.append(str(how_many_zeros(m, n)))

        index += 1

    open(1, "w").write("\n".join(output))