"""
author: Anton Nilsson
testcase 1:
in:
0.142857 6

out:
1/7

testcase 2:
in:
1.6 1

out:
5/3

testcase 3:
in:
123.456 2

out:
61111/495

"""

from math import gcd

def rational_ratio(ni: str, r: int) -> str:
    w, d = str(ni).split(".")

    ns = "0" + w + d

    nu = int(ns) - int(ns[:-r])
    de = 10**(len(str(d))) - 10**(len(str(d)) - r)

    cd = gcd(nu, de)
    
    return f"{nu//cd}/{de//cd}"

if __name__ == "__main__":
    n, r = input().split(" ")
    print(rational_ratio(n, int(r)))