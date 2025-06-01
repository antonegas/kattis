"""
author: Anton Nilsson
testcase 1:
in:
4 3 4 0
0 1 2
1 2 2
3 0 2
0
1
2
3
2 1 1 0
0 1 100
1
0 0 0 0

out:
0
2
4
Impossible

100

"""

from heapq import heappop, heappush

def get_path(previous: list[int], target: int) -> list[int]:
    """
    Given a previous list and a target, gives a shortest path from the source to the target.
    """
    path = [target]

    while previous[path[-1]] != -1:
        path.append(previous[path[-1]])

    return [*reversed(path)]

def dijkstra(adjacent: list[list[tuple[int, int]]], source: int) -> tuple[list[float], list[int]]:
    """
    Finds the shortest path from a source vertex to every other vertex in a graph.

    algorithm: The algorithm used is Dijkstra's algorithm. It starts at a vertex and adds adjacent 
    vertices to a priotiy queue where they are ordered by the cost of the connecting edge and the 
    cost of reaching the vertex. After each iteration the top vertex of the priority queue is removed 
    and the cheapest path to the vertex has been found.
    time complexity: O(|E|*log|E|)
    where:
    - |E| is the number of edges.
    - |V| is the number of vertices.
    why:
    - O(|E|) from checking every edge.
    - O(|V|) from checking every vertex.
    - O(log|E|) from the priority queue.
    - O((|V|+|E|)*log|E|) = O(|E|*log|E|)
    reference: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Pseudocode

    parameters:
    - adjacent: a list where a given index in the list contains an other list with adjacent vertices and the cost of 
    their connecting edge.
    - source: an integer representing the index of the source vertex.
    returns:
    - A tuple of two lists. The first list contains the cost of reaching a vertex from the source node and the second 
    list the previous vertex in the path to reach the vertex. The previous vertex value being negative indicates that 
    there either is no path or that the vertex is the source node.
    """
    
    # Initialize distance, previous and visited lists.
    costs = [float("inf")] * len(adjacent)
    previous = [-1] * len(adjacent)
    visited = [False] * len(adjacent)

    # Create the heap used for the priority queue and add the source node to it. Each entry in the queue contains the 
    # distance to reach the vertex, the vertex index and the index of the vertex which added the entry to the queue.
    queue = [(0, source, -1)]

    while queue:
        cost, u, previous_vertex = heappop(queue)

        # If the vertex has already been visited it can be ignored. If it has not been visited it means that the 
        # shortest distance to the reach it has been found and that its previous vertex can be set. The vertex is then 
        # marked as visited.
        if visited[u]:
            continue

        costs[u] = cost
        previous[u] = previous_vertex
        visited[u] = True

        # Add adjacent vertices to the queue with the cost set to the cost of reaching the the current vertex plus 
        # the cost of the connecting edge and the previous vertex set to the current vertex.
        for v, edge_cost in adjacent[u]:
            if not visited[v]:
                adjacent_cost = cost + edge_cost
                heappush(queue, (adjacent_cost, v, u))

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

        costs, _ = dijkstra(adjacent, s)

        for _ in range(q):
            query = int(lines[index])
            query_result = costs[query]

            if query_result == float("inf"):
                output.append("Impossible")
            else:
                output.append(str(query_result))

            index += 1

        output.append("")

    open(1, "w").write("\n".join(output))