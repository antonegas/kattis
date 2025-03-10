"""
author: Anton Nilsson
testcase 1:
in:
3 3
0 1 0.9
1 2 0.9
0 2 0.8
2 1
1 0 1
0 0

out:
0.8100
1.0000

"""

from heapq import heappush, heappop

def get_shorty(adjacent: list[list[tuple[int, float]]], source: int, target: int) -> float:
    previous = [-1] * len(adjacent)
    visited = [False] * len(adjacent)

    queue = [(0.0, source, -1)]

    while queue:
        cost, vertex, previous_vertex = heappop(queue)

        if visited[vertex]:
            continue

        if vertex == target:
            return 1 - cost
        
        previous[vertex] = previous_vertex
        visited[vertex] = True

        for adjacent_vertex, edge_cost in adjacent[vertex]:
            adjacent_cost = 1 - (1 - cost) * edge_cost
            heappush(queue, (adjacent_cost, adjacent_vertex, vertex))

    return 0.0

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()[:-1]

    index = 0

    while index < len(lines):
        n, m = map(int, lines[index].split(" "))
        index += 1
        
        adjacent = [list() for _ in range(n)]

        for _ in range(m):
            u, v, factor = map(float, lines[index].split(" "))
            adjacent[int(u)].append((int(v), factor))
            adjacent[int(v)].append((int(u), factor))

            index += 1

        output.append(str(round(get_shorty(adjacent, 0, n - 1), 4)).ljust(6, "0"))

    open(1, "w").write("\n".join(output))