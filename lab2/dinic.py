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
    """
    Finds the level for every vertex in the graph. Where the level of a vertex being the minimum number of edges with 
    available capacity needed to reach the vertex.
    """

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

def dfs(u: int, pushed: int, sink: int, edge_pointers: list[int], level: list[int], capacity: list[list[int]], flow: list[list[int]]) -> int:
    """
    Finds a blocking flow for a vertex, if the vertex isn't already blocked. A flow is blocking if 
    it blocks atleast one of the following edges in the level graph. A edge is blocked if its flow is 
    maximal for the level graph. A vertex is blocked all its outgoing edges in the level graph is blocked.
    """

    # Terminate if the sink vertex has been reached or if this is a blocking path.
    if u == sink or pushed == 0:
        return pushed

    while edge_pointers[u] < len(flow):
        v = edge_pointers[u]

        # The only valid edges are edges which are one level above the current one.
        if level[u] + 1 == level[v]:
            delta = dfs(v, min(pushed, capacity[u][v] - flow[u][v]), sink, edge_pointers, level, capacity, flow)

            # If delta for the edge is not zero the edge wasn't already blocked.
            if delta > 0:
                flow[u][v] += delta
                flow[v][u] -= delta
                return delta

        # If there wasn't an edge between u and v or if the edge already had a blocking flow check 
        # the next vertex. 
        edge_pointers[u] += 1
    
    return 0

def dinic(graph: list[list[int]], adjacent: list[list[int]], source: int, sink: int) -> list[list[int]]:
    """
    Given a graph of capacities, a source and a sink vertex, finds the flow graph which gives the maximum 
    flow in the graph.

    algorithm: The algorithm used is Dinitz. It works by constructing a directed acyclic graph called a 
    level graph using breadth first search. It then finds blocking flows through this level graph. 
    These two steps are then repeated until there is no path in the level graph from the source vertex 
    to the sink vertex and a maximum flow has been found.
    time complexity: O(|V|^2*|E|)
    where:
    - |V| is the number of vertices.
    - |E| is the number of edges.
    why:
    - O(|V|) from there being at most |V| phases of the algorithm.
    - O(|E|) from the breadth first search.
    - O(|V|*|E|) from the depth first search.
    - O(|E|) from updating the flow each edge.
    - O(|V|*(|E|+|V|*|E|+|E|)) = O(|V|^2*|E|)
    reference: https://cp-algorithms.com/graph/dinic.html#implementation

    parameters:
    - graph: a matrix of vertices in the graph where graph[u][v] gives the capacity of the edge from u to v.
    - adjacent: a list of lists where adjacent[u] gives the list of all edges from u, if adjacent[u] contains 
    v then adjacent[v] should contain u.
    - source: the index of the source vertex in the graph.
    - sink: the index of the sink vertex in the graph.
    returns:
    - A graph with the maximum flows through every edge in the graph.
    """

    capacity = [u[:] for u in graph]
    flow = [[0] * len(adjacent) for _ in range(len(adjacent))]

    # Find a level graph for the graph.
    level = bfs(source, capacity, flow, adjacent)

    # Keep looking for blocking flows as long as there is a non-blocked path to the sink vertex.
    while level[sink] != -1:
        edge_pointers = [0] * len(adjacent)

        # Start from the source vertex assuming that the maximum possible flow can be pushed into it.
        # Repeat this until there no longer is a blocking flow for the level graph.
        while dfs(source, 10**8, sink, edge_pointers, level, capacity, flow) > 0:
            pass

        # Find a new level graph in the graph based on the updated edge flows.
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

    flow = sum(flow_graph[s])
    used_edges = [(u, v, flow_graph[u][v]) for u, v in edges if flow_graph[u][v] > 0]

    output.append(f"{n} {flow} {len(used_edges)}")

    for u, v, edge_flow in used_edges:
        output.append(f"{u} {v} {edge_flow}")

    open(1, "w").write("\n".join(output))