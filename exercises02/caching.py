"""
author: Anton Nilsson
testcase 1:
in:
1 2 3
0
0
1

out:
2

testcase 2:
in:
3 4 8
0
1
2
3
3
2
1
0

out:
5

"""

from heapq import heappop, heappush

def caching(size: int, count: int, accesses: list[int]) -> int:
    next_access = [[float("-inf")] for _ in range(count)]

    for time, access in reversed([*enumerate(accesses)]):
        next_access[access].append(-time)

    cached = [False] * count
    queue = list()
    misses = 0

    for time, access in enumerate(accesses):
        next_access[access].pop()

        if cached[access]:
            heappush(queue, (next_access[access][-1], access))
            continue

        misses += 1
        cached[access] = True

        if misses <= size:
            heappush(queue, (next_access[access][-1], access))
            continue

        _, removed_cache = heappop(queue)
        cached[removed_cache] = False

        heappush(queue, (next_access[access][-1], access))

    return misses

if __name__ == "__main__":
    c, n, a = map(int, input().split(" "))
    
    accesses = [int(input()) for _ in range(a)]

    print(caching(c, n, accesses))