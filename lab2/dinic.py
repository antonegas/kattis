"""
author: Anton Nilsson
testcase 1:
in:
4 5 0 3
0 1 10
1 2 1
1 3 1
0 2 1
2 3 10

out:
4 3 5
0 1 2
0 2 1
1 2 1
1 3 1
2 3 2

testcase 2:
in:
2 1 0 1
0 1 100000

out:
2 100000 1
0 1 100000

testcase 3:
in:
2 1 1 0
0 1 100000

out:
2 0 0

testcase 4:
in:
2 1 0 1
0 1 100000000

out:
2 100000000 1
0 1 100000000

testcase 5:
in:
4 4 0 3
0 1 1
1 2 1
2 1 1
2 3 1

out:
4 1 3
0 1 1
1 2 1
2 3 1

testcase 6:
in:
12 17 0 11
0 1 1
0 2 1
0 3 1
1 5 1
1 6 1
1 7 1
2 4 1
2 6 1
3 4 1
3 5 1
4 8 1
5 9 1
6 9 1
7 10 1
8 11 1
9 11 1
10 11 1

out:
12 3 12
0 1 1
0 2 1
0 3 1
2 4 1
3 5 1
1 7 1
4 8 1
5 9 1
7 10 1
8 11 1
9 11 1
10 11 1

testcase 7:
in:
8 9 0 7
0 1 1
0 2 1
1 3 1
2 3 1
3 4 2
4 5 1
4 6 1
5 7 1
6 7 1

out:
8 2 9
0 1 1
0 2 1
1 3 1
2 3 1
3 4 2
4 5 1
4 6 1
5 7 1
6 7 1

"""

from collections import deque

def bfs(source: int, capacity: list[list[int]], flow: list[list[int]], adjacent: list[list[int]]) -> list[int]:
    level = [-1] * len(adjacent)
    level[source] = 0

    queue = deque()
    queue.append(source)

    while len(queue) > 0:
        u = queue.popleft()

        for v in adjacent[u]:
            if capacity[u][v] == flow[u][v] or level[v] != -1:
                continue
            level[v] = level[u] + 1
            queue.append(v)

    return level

def dfs(u: int, pushed: int, sink: int, ptr: list[int], level: list[int], capacity: list[list[int]], flow: list[list[int]]) -> int:
    if u == sink or pushed == 0:
        return pushed

    while ptr[u] < len(flow):
        v = ptr[u]

        if level[u] + 1 == level[v]:
            delta = dfs(v, min(pushed, capacity[u][v] - flow[u][v]), sink, ptr, level, capacity, flow)

            if delta > 0:
                flow[u][v] += delta
                flow[v][u] -= delta
                return delta

        ptr[u] += 1    
    
    return 0

def dinic(graph: list[list[int]], adjacent: list[list[int]], source: int, sink: int) -> list[list[int]]:
    capacity = [u[:] for u in graph]
    flow = [[0] * len(adjacent) for _ in range(len(adjacent))]

    level = bfs(source, capacity, flow, adjacent)

    while level[sink] != -1:
        ptr = [0] * len(adjacent)

        while dfs(source, 10**8, sink, ptr, level, capacity, flow) > 0:
            pass

        level = bfs(source, capacity, flow, adjacent)

    return flow

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()

    n, m, s, t = map(int, lines[0].split(" "))
    index = 1

    graph = [[0] * n for _ in range(n)]
    adjacent = [list() for _ in range(n)]
    edges = list()

    for _ in range(m):
        u, v, c = map(int, lines[index].split(" "))
        if graph[u][v] == 0 and graph[v][u] == 0:
            adjacent[u].append(v)
            adjacent[v].append(u)
        if graph[u][v] == 0:
            edges.append((u, v))
        graph[u][v] += c

        index += 1

    flow_graph = dinic(graph, adjacent, s, t)

    flow = sum(flow_graph[s][i] for i in range(n))
    used_edges = [(u, v, flow_graph[u][v]) for u, v in edges if flow_graph[u][v] > 0]

    output.append(f"{n} {flow} {len(used_edges)}")

    for u, v, edge_flow in used_edges:
        output.append(f"{u} {v} {edge_flow}")

    open(1, "w").write("\n".join(output))