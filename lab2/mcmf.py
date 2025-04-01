"""
author: Anton Nilsson
testcase 1:
in:
4 4 0 3
0 1 4 10
1 2 2 10
0 2 4 30
2 3 4 10

out:
4 140

testcase 2:
in:
2 1 0 1
0 1 1000 100

out:
1000 100000

testcase 3:
in:
2 1 1 0
0 1 1000 100

out:
0 0

"""

from collections import deque
from heapq import heappop, heappush

def spfa_bfs(adjacent: list[list[int]], costs: list[float], source: int):
    queue = deque()
    queue.append(source)
    costs[source] = float("-inf")

    while len(queue) > 0:
        u = queue.popleft()

        for v in adjacent[u]:
            if costs[v] == float("-inf"):
                continue

            costs[v] = float("-inf")

            queue.append(v)

def spfa(adjacent: list[list[int]], edge_costs: list[list[float]], source: int) -> list[float]:
    costs = [float("inf")] * len(adjacent)
    count = [0] * len(adjacent)
    queued = [False] * len(adjacent)
    queue = deque()

    costs[source] = 0.0
    queue.append(source)
    queued[source] = True

    while len(queue) > 0:
        u = queue.popleft()
        queued[u] = False

        for v in adjacent[u]:
            edge_cost = edge_costs[u][v]
            cost = costs[u] + edge_cost

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
            spfa_bfs(adjacent, costs, u)

    return costs

def dijkstra(adjacent: list[list[int]], capacity: list[list[int]], flow: list[list[int]], edge_costs: list[list[float]], source: int) -> list[float]:
    costs = [float("inf")] * len(adjacent)
    visited = [False] * len(adjacent)

    queue = [(0.0, source)]

    while queue:
        cost, u = heappop(queue)

        if visited[u]:
            continue

        costs[u] = cost
        visited[u] = True

        for v in adjacent[u]:
            if capacity[u][v] - flow[u][v] <= 0:
                continue

            edge_cost = edge_costs[u][v]
            adjacent_cost = cost + edge_cost
            heappush(queue, (adjacent_cost, v))

    return costs

def dinic_bfs(source: int, capacity: list[list[int]], flow: list[list[int]], cost: list[list[float]], adjacent: list[list[int]]) -> list[int]:
    level = [-1] * len(adjacent)
    level[source] = 0

    queue = deque()
    queue.append(source)

    while len(queue) > 0:
        u = queue.popleft()

        for v in adjacent[u]:
            if capacity[u][v] == flow[u][v] or level[v] != -1 or cost[u][v] != 0:
                continue
            level[v] = level[u] + 1
            queue.append(v)

    return level

def dinic_dfs(u: int, pushed: int, sink: int, edge_pointers: list[int], level: list[int], capacity: list[list[int]], flow: list[list[int]], cost: list[list[float]]) -> int:
    if u == sink or pushed == 0:
        return pushed

    while edge_pointers[u] < len(flow):
        v = edge_pointers[u]

        if level[u] + 1 == level[v] and cost[u][v] == 0 and capacity[u][v] - flow[u][v] > 0:
            delta = dinic_dfs(v, min(pushed, capacity[u][v] - flow[u][v]), sink, edge_pointers, level, capacity, flow, cost)

            if delta > 0:
                flow[u][v] += delta
                flow[v][u] -= delta
                return delta

        edge_pointers[u] += 1
    
    return 0

def dinic(capacity: list[list[int]], cost: list[list[float]], flow: list[list[int]], adjacent: list[list[int]], source: int, sink: int) -> list[list[int]]:
    # flow = [[0] * len(adjacent) for _ in range(len(adjacent))]

    level = dinic_bfs(source, capacity, flow, cost, adjacent)

    while level[sink] != -1:
        edge_pointers = [0] * len(adjacent)

        while dinic_dfs(source, 10**8, sink, edge_pointers, level, capacity, flow, cost) > 0:
            pass

        level = dinic_bfs(source, capacity, flow, cost, adjacent)

    return flow

def recalculate_edge_costs(adjacent: list[list[int]], path_costs: list[float], cost: list[list[float]]):
    """
    Updates the cost matrix based on the shortest paths to reach vertices.
    """

    for u in range(len(adjacent)):
        if path_costs[u] == float("inf"):
            continue

        for v in adjacent[u]:
            if path_costs[v] == float("inf"):
                continue

            cost[u][v] += path_costs[u] - path_costs[v]

def primal_dual(capacity: list[list[int]], graph_cost: list[list[float]], adjacent: list[list[int]], source: int, sink: int):
    """
    Given a graph of capacities, a source and a sink vertex, finds the flow graph which gives the maximum 
    flow for the minimum cost in the graph.

    algorithm: The algorithm used is Primal-Dual, which is a version of succesive shortest path with some 
    improvement to the time complexity of the algorithm.
    time complexity: O(min(F,|V|*C)*|V|^2*|E|)
    where:
    - |V| is the number of vertices.
    - |E| is the number of edges.
    - F is the maximum flow in the graph.
    - C is the maximum cost of the edges.
    why:
    - O(|V|*|E|) from running the Bellman-Ford algorithm.
    - O(min(F,|V|*C)) from there being at most min(F,|V|*C) iterations.
    - O(|E|+|V|*log|V|) from running Dijkstra's algorithm.
    - O(|V|^2*|E|) from running Dinitz's algorithm to find a maximum flow.
    - O(|V|*|E|+min(F,|V|*C)*(|E|+|V|*log|V|+|V|^2*|E|)) = O(min(F,|V|*C)*|V|^2*|E|)
    reference: https://codeforces.com/blog/entry/105658

    parameters:
    - XXX
    returns:
    - XXX
    """

    cost = [c[:] for c in graph_cost]
    flow = [[0] * len(adjacent) for _ in range(len(adjacent))]

    path_costs = spfa(adjacent, cost, source)
    recalculate_edge_costs(adjacent, path_costs, cost)

    path_costs = dijkstra(adjacent, capacity, flow, cost, source) # TODO: Check if this needs to be here or if bellman is enough
    recalculate_edge_costs(adjacent, path_costs, cost)
    
    while path_costs[sink] != float("inf"):
        dinic(capacity, cost, flow, adjacent, source, sink)

        path_costs = dijkstra(adjacent, capacity, flow, cost, source)
        recalculate_edge_costs(adjacent, path_costs, cost)
    
    return flow

if __name__ == "__main__":
    lines = open(0, "r").read().splitlines()

    n, m, s, t = map(int, lines[0].split(" "))
    index = 1

    capacity_graph = [[0] * n for _ in range(n)]
    cost_graph = [[float("inf")] * n for _ in range(n)]
    adjacent = [list() for _ in range(n)]
    edges = list()

    for _ in range(m):
        u, v, c, w = map(int, lines[index].split(" "))
        if capacity_graph[u][v] == 0 and capacity_graph[v][u] == 0:
            adjacent[u].append(v)
            adjacent[v].append(u)
        if capacity_graph[u][v] == 0:
            edges.append((u, v))
        capacity_graph[u][v] += c
        cost_graph[u][v] = w
        cost_graph[u][v] = w

        index += 1

    flow_graph = primal_dual(capacity_graph, cost_graph, adjacent, s, t)
    flow = sum(flow_graph[s])

    cost = sum([cost_graph[u][v] * flow_graph[u][v] for u, v in edges if flow_graph[u][v] > 0])

    open(1, "w").write(f"{flow} {cost}")