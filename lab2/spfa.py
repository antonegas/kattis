"""
author: Anton Nilsson
testcase 1:
in:
5 4 3 0
0 1 999
1 2 -2
2 1 1
0 3 2
1
3
4
2 1 1 0
0 1 -100
1
0 0 0 0

out:
-Infinity
2
Impossible

-100

"""

from collections import deque

def bfs(adjacent: list[list[tuple[int, int]]], costs: list[float], source: int):
    """
    Propagates -infinity to all vertices reachable from a negative cycle.
    """

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

def spfa(adjacent: list[list[tuple[int, int]]], source: int) -> tuple[list[float], list[int]]:
    """
    Given a graph with edges which may have negative weights, finds the shortest paths from a 
    source node to all other nodes.

    algorithm: The algorithm used is shortest path faster algorithm which is an improvement of 
    Bellman-Ford. Bellman-Ford works by performing relaxations using the edges in the graph. 
    The cost of reaching a node can be improved with an edge (u, v) if the cost of reaching u 
    and the cost of the edge is lower than the current cost of v. The algorithm can also detect 
    negative cycles by seeing if relaxations has been done on a vertex |V| times. The improvement 
    over Bellman-Ford is that only vertices which can relax their neighbors are queued.
    time complexity: O(|V|*|E|)
    where:
    - |V| is the number of vertices.
    - |E| is the number of edges.
    why:
    - O(|V|) from running relaxations at most |V| times.
    - O(|E|) from each phase of relaxations.
    reference: https://cp-algorithms.com/graph/bellman_ford.html#shortest-path-faster-algorithm-spfa

    parameters:
    - adjacent: a list where a given index in the list contains an other list with adjacent vertices 
    and the cost of their connecting edge.
    - source: an integer representing the index of the source vertex.
    returns:
    - A tuple of two lists. The first list contains the cost of reaching a vertex from the source node 
    and the second list the previous vertex in the path to reach the vertex. The previous vertex value 
    being negative indicates that there either is no path or that the vertex is the source node.
    """
    
    # Initialize costs, previous, relaxation count, queued vector and the queue.
    costs = [float("inf")] * len(adjacent)
    previous = [-1] * len(adjacent)
    count = [0] * len(adjacent)
    queued = [False] * len(adjacent)
    queue = deque()

    costs[source] = 0.0
    queue.append(source)
    queued[source] = True

    while len(queue) > 0:
        u = queue.popleft()
        queued[u] = False

        for v, edge_cost in adjacent[u]:
            cost = costs[u] + edge_cost

            # If the edge can not be used for relaxation do not use it. If the edge can be used for 
            # relaxation update the cost to reach the vertex v and set u as the previous vertex for v.
            if costs[v] <= cost:
                continue

            # If a vertex has been relaxed |V| times it is part of a negative cycle.
            if count[v] == len(adjacent):
                break

            costs[v] = cost
            previous[v] = u

            # Queue the vertex v if it is not already in the queue. Update the number of 
            # times that the vertex has been relaxed to detect negative cycles.
            if queued[v]:
                continue

            count[v] += 1

            queue.append(v)
            queued[v] = True

    # Update the costs for all vertices reachable from a negative cycle to be -infinity.
    for u in range(len(adjacent)):
        if count[u] >= len(adjacent) and costs[u] != float("-inf"):
            bfs(adjacent, costs, u)

    return costs, previous

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()[:-1]

    index = 0

    while index < len(lines):
        n, m, q, s = map(int, lines[index].split(" "))
        index += 1

        adjacent = [list() for _ in range(n)]

        for _ in range(m):
            u, v, w = map(int, lines[index].split(" "))
            adjacent[u].append((v, w))

            index += 1

        costs, _ = spfa(adjacent, s)

        for _ in range(q):
            v = int(lines[index])
            cost = costs[v]

            if cost == float("-inf"):
                output.append("-Infinity")
            elif cost == float("inf"):
                output.append("Impossible")
            else:
                output.append(str(int(cost)))

            index += 1

        output.append("")

    open(1, "w").write("\n".join(output))