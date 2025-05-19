"""
author: Anton Nilsson
testcase 1:
in:
4
...D
..C.
.B..
A...

out:
4

testcase 2:
in:
5
..T..
A....
.FE.R
....X
S....

out:
3

testcase 3:
in:
10
....AB....
..C....D..
.E......F.
...G..H...
I........J
K........L
...M..N...
.O......P.
..Q....R..
....ST....

out:
0

"""

from collections import defaultdict
from math import comb

def torjke(points):
    count = 0

    for i in range(len(points)):
        px, py = points[i]

        colinear = defaultdict(lambda: 0)
        
        for j in range(i + 1, len(points)):
            qx, qy = points[j]

            key = float("inf")

            if px < qx:
                key = (qy - py) / (qx - px)
            elif px > qx:
                key = (py - qy) / (px - qx)

            colinear[key] += 1

        for l in colinear.values():
            count += comb(l, 2)

    return count

if __name__ == "__main__":
    n = int(input())

    points = list()

    for y in range(n):
        for x, l in enumerate(input()):
            if l != ".":
                points.append((x, y))

    print(torjke(points))