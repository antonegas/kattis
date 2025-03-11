"""
author: Anton Nilsson
testcase 1:
in:
5
0 1 2
-60 1 3
-60 1 4
20 1 5
0 0
5
0 1 2
20 1 3
-60 1 4
-60 1 5
0 0
5
0 1 2
21 1 3
-60 1 4
-60 1 5
0 0
5
0 1 2
20 2 1 3
-60 1 4
-60 1 5
0 0
-1

out:
hopeless
hopeless
winnable
winnable

testcase 2:
in:
3
0 1 2
-101 1 3
0 0
4
0 1 2
-101 1 3
102 2 2 4
0 0
-1

out:
hopeless
hopeless

"""

from collections import deque

def bfs(adjacent: list[list[int]], costs: list[float], source: int):
    queue = deque()
    queue.append(source)
    costs[source] = float("-inf")

    while len(queue) > 0:
        u = queue.popleft()

        for v, _ in adjacent[u]:
            if costs[v] == float("-inf"):
                continue

            costs[v] = float("-inf")

            queue.append(v)

def xyzzy(adjacent: list[list[int]]) -> bool:
    costs = [float("inf")] * len(adjacent)
    count = [0] * len(adjacent)
    queued = [False] * len(adjacent)
    queue = deque()

    costs[0] = -100.0
    queue.append(0)
    queued[0] = True

    while len(queue) > 0:
        u = queue.popleft()
        queued[u] = False

        for v, edge_cost in adjacent[u]:
            cost = costs[u] + edge_cost

            if cost >= 0:
                continue

            if costs[v] <= cost:
                continue

            if count[v] == len(adjacent):
                break

            costs[v] = cost

            if queued[v]:
                continue

            count[v] += 1

            queue.append(v)
            queued[v] = True

    for u in range(len(adjacent)):
        if count[u] >= len(adjacent) and costs[u] != float("-inf"):
            bfs(adjacent, costs, u)

    return costs[-1] < 0.0

if __name__ == "__main__":
    output = list()
    words = open(0, "r").read().split()[:-1]

    index = 0

    while index < len(words):
        n = int(words[index])
        index += 1

        adjacent = [list() for _ in range(n)]

        for i in range(n):
            energy_value = int(words[index])
            index += 1
            l = int(words[index])
            index += 1

            connected_rooms = list()

            for _ in range(l):
                connected_rooms.append(int(words[index]))
                index += 1

            for connected_room in connected_rooms:
                adjacent[i].append((connected_room - 1, -energy_value))

        if xyzzy(adjacent):
            output.append("winnable")
        else:
            output.append("hopeless")

    open(1, "w").write("\n".join(output))