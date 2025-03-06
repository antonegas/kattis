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

def bfs(capacities: list[list[int]], flow: list[list[int]], adjacent: list[list[int]], source: int, target: int) -> list[int]:
    """
    Gives a shortest augmented path from source to target.
    """
    queue = deque()
    queue.append(source)
    parent = [-1] * len(adjacent)
    visited = [False] * len(adjacent)
    visited[source] = True

    if source == target:
        return parent
    
    while len(queue) > 0:
        u = queue.popleft()
        for v in adjacent[u]:
            if capacities[u][v] - flow[u][v] > 0 and not visited[v]:
                parent[v] = u
                visited[v] = True
                if v == target:
                    return parent
                queue.append(v)

    return []

def edmonds_karp(graph: list[list[int]], adjacent: list[list[int]], source: int, sink: int) -> list[list[int]]:
    """
    Given a capacity graph, a source and a sink, gives the flow graph.

    algorithm: The algorithm used Edmonds-Karp. The algorithm works by running 
    breadth first search to find the shortest augmented path from the source to 
    the sink. The flow of this path is the minimum capacity of the edges along 
    this path. For every edge along this path the capacity of the edge is decreased 
    by the flow and the capacity of the back-edge is increased by the flow. 
    This is repeated until there no longer exists such a path.
    time complexity: O(|V||E|^2)
    where:
    - |V| is the number of vertices.
    - |E| is the number of edges.
    why:
    - O(|V|) from the maximum length of an augmented path.
    - O(|E|) from finding the augmented path.
    - O(|E|) from there being atleast one edge with becomes saturated.
    reference: https://cp-algorithms.com/graph/edmonds_karp.html#implementation

    parameters:
    - adjacent: a list of containing all directed edges away from a vertex and 
    their capacities.
    - source: the source vertex of the max-flow problem.
    - sink: the sink vertex of the max-flow problem
    returns:
    - The flow graph of the max-flow problem.
    """
    capacity_graph = [u[:] for u in graph]
    flow_graph = [[0] * len(adjacent) for _ in range(len(adjacent))]

    parent = bfs(capacity_graph, flow_graph, adjacent, source, sink)

    while parent != []:
        path = list()
        current = sink
        flow = float("inf")

        while current != source:
            previous = parent[current]
            flow = min(flow, capacity_graph[previous][current] - flow_graph[previous][current])
            path.append((previous, current))
            current = previous

        for u, v in path:
            flow_graph[u][v] += flow
            flow_graph[v][u] -= flow
        
        parent = bfs(capacity_graph, flow_graph, adjacent, source, sink)

    return flow_graph

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

    flow_graph = edmonds_karp(graph, adjacent, s, t)

    flow = sum(flow_graph[s][i] for i in range(n))
    used_edges = [(u, v, flow_graph[u][v]) for u, v in edges if flow_graph[u][v] > 0]

    output.append(f"{n} {flow} {len(used_edges)}")

    for u, v, edge_flow in used_edges:
        output.append(f"{u} {v} {edge_flow}")

    open(1, "w").write("\n".join(output))