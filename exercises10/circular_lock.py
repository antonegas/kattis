"""
author: Anton Nilsson
testcase 1:
in:
2
0 11 17 13
5 8 6 11
1 1 3 3
1 0 3 3

out:
Yes
No

"""

from math import gcd

if __name__ == "__main__":
    for _ in range(int(input())):
        devices = list()

        state1, state2, period1, period2 = map(int, input().split(" "))
        state3, state4, period3, period4 = map(int, input().split(" "))

        devices.append((state1, period1))
        devices.append((state2, period2))
        devices.append((state3, period3))
        devices.append((state4, period4))

        if (state1 - state2 - state3 + state4) % gcd(period1, period2, period3, period4):
            print("No")
        else:
            print("Yes")