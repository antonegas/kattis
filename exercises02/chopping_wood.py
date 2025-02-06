"""
author: Anton Nilsson
testcase 1:
in:
6
5
1
1
2
2
7

out:
3
4
5
1
6
2

testcase 2:
in:
2
1
2

out:
Error

"""

from collections import Counter
from heapq import heappop, heappush, heapify

def algorithm(cuts) -> list[int]:
    count = Counter(cuts)
    nodes = set(i for i in range(1, len(cuts) + 2))
    leafs = list(nodes - count.keys())
    heapify(leafs)

    result = list()

    for cut in cuts:
        result.append(heappop(leafs))
        count[cut] -= 1
        if count[cut] == 0:
            heappush(leafs, cut)

    return result

def solve(cuts: list[int]) -> list[str]:
    if len(cuts) + 1 != cuts[-1]:
        return ["Error"]
    else:
        return list(map(str, algorithm(cuts)))

if __name__ == "__main__":
    output = ""
    data = open(0, "r").read()
    cuts = list(map(int, data.split("\n")[1:-1]))
    
    output += "\n".join(solve(cuts))

    open(1, "w").write(output)