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
2
1
0


testcase 2:
in:
2 1 0 1
0 1 100000

out:
1
0


testcase 3:
in:
2 1 1 0
0 1 100000

out:
1
1


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

def minimum_cut(graph: list[list[int]], adjacent: list[list[int]], source: int, target: int) -> list[int]:
    """
    Gives the vertex set U containing s for a s-t-minimum-cut problem.

    algorithm: The flow graph for the graph is found using Dinic's algorithm. The vertex 
    set U is then all the vertices which can be reached from the source vertex using edges 
    with residual capacity.
    time complexity: O(|V|^2*|E|)
    where:
    - |V| is the number of vertices.
    - |E| is the number of edges.
    why:
    - O(|V|^2*|E|) from running Dinic's algorithm.
    - O(|V|+|E|) from running depth first search.
    - O(|V|^2*|E|+|V|+|E|)=O(|V|^2*|E|).
    reference: https://cp-algorithms.com/graph/edmonds_karp.html#max-flow-min-cut-theorem

    parameters:
    - graph: the weight graph where graph[u][v] gives the weight of the edge from u to v.
    - adjacent: a list of lists where adjacent[u] gives the list of all edges from u. If 
    adjacent[u] contains v then adjacent[v] should contain u.
    - source: the index of the source vertex in the graph.
    - target: the index of the target vertex in the graph.
    returns:
    - The vertex set U containing s for the given s-t-minimum-cut problem.
    """

    # Find the flow graph using Dinic's algorithm.
    flow_graph = dinic(graph, adjacent, source, target)

    # Use depth first search to find vertices reachable from the source vertex 
    # in the residual graph.
    stack = list()
    visited = [False] * len(adjacent)
    U = list()

    stack.append(source)
    visited[source] = True
    U.append(source)

    while len(stack) > 0:
        u = stack.pop()

        for v in adjacent[u]:
            if visited[v]:
                continue
            
            # The residual capacity is equal to the capacity of the edge minus 
            # the flow through that edge.
            if graph[u][v] - flow_graph[u][v] <= 0:
                continue

            visited[v] = True
            stack.append(v)
            U.append(v)

    return U

def add_edge(graph: list[list[int]], adjacent: list[list[int]], u: int, v: int, capacity: int):
    """
    Adds an edge to the capacity graph with the given capacity.
    """
    if graph[u][v] == 0 and graph[v][u] == 0:
        adjacent[u].append(v)
        adjacent[v].append(u)
    graph[u][v] += capacity

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()

    n, m, s, t = map(int, lines[0].split(" "))
    index = 1

    graph = [[0] * n for _ in range(n)]
    adjacent = [list() for _ in range(n)]

    for _ in range(m):
        u, v, w = map(int, lines[index].split(" "))
        add_edge(graph, adjacent, u, v, w)

        index += 1

    U = minimum_cut(graph, adjacent, s, t)

    output.append(str(len(U)))
    output.extend(map(str, U))

    open(1, "w").write("\n".join(output))