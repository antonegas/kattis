"""
author: Anton Nilsson
testcase 1:
in:
4 4 4 0
0 1 15 10 5
1 2 15 10 5
0 2 5 5 30
3 0 0 1 1
0
1
2
3
2 1 1 0
0 1 100 0 5
1
0 0 0 0

out:
0
20
30
Impossible

105

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

def time_table_dijkstra(timetable: list[list[tuple[int, int, int, int]]], source: int) -> tuple[list[float], list[int]]:
    """
    Finds the shortest path from a source vertex to every other vertex in a graph.

    algorithm: The algorithm used is Dijkstra's algorithm. It starts at a vertex and adds adjacent vertices to a 
    priotiy queue where they are ordered by the total required time to use the edge. The total time required is the sum 
    of the time required to reach the current vertex, the time remaining until the edge becomes usable again and the 
    time required to travel the edge. After each iteration the top vertex of the priority queue is removed and the 
    least time consuming path to the vertex has been found.
    time complexity: O(|E| + |V|*log|V|)
    where:
    - |E| is the number of edges.
    - |V| is the number of vertices.
    why:
    - O(|E|) from checking every edge.
    - O(|V|*log|V|) from the priority queue.
    reference: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Pseudocode

    parameters:
    - timetable: a list which at a given index contains the time table for a edge from the vertex at the given index.
    - source: an integer representing the index of the source vertex.
    returns:
    - A tuple of two lists. The first list contains the time required to reach a vertex from the source node and the 
    second list the previous vertex in the path to reach the vertex. The previous vertex value being negative indicates 
    that there either is no path or that the vertex is the source node.
    """
    
    # Initialize distance, previous and visited lists.
    times = [float("inf")] * len(timetable)
    previous = [-1] * len(timetable)
    visited = [False] * len(timetable)

    # Create the heap used for the priority queue and add the source node to it. Each entry in the queue contains the 
    # distance to reach the vertex, the vertex index and the index of the vertex which added the entry to the queue.
    queue = [(0, source, -1)]

    while queue:
        time, vertex, previous_vertex = heappop(queue)

        # If the vertex has already been visited it can be ignored. If it has not been visited it means that the 
        # least time required to the reach it has been found and that its previous vertex can be set. The vertex is 
        # then marked as visited.
        if visited[vertex]:
            continue

        times[vertex] = time
        previous[vertex] = previous_vertex
        visited[vertex] = True

        # Add adjacent vertices to the queue with the time required set based on the time table.
        for adjacent_vertex, edge_t0, edge_period, edge_time in timetable[vertex]:
            # If the period for the edge is zero the edge can only be used if t0 has not passed.
            if edge_period == 0 and time > edge_t0:
                continue

            if time <= edge_t0:
                # If t0 has not passed the time required is t0 plus the time required to use the edge.
                adjacent_time = edge_t0 + edge_time
                heappush(queue, (adjacent_time, adjacent_vertex, vertex))
            else:
                # If t0 has passed the time required is the current time, the time remaining until the edge becomes 
                # available again and the time required to use the edge.
                time_until_available = (edge_period - ((time - edge_t0) % edge_period)) % edge_period
                adjacent_time = time + time_until_available + edge_time
                heappush(queue, (adjacent_time, adjacent_vertex, vertex))

    return times, previous

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()[:-1]

    index = 0

    while index < len(lines):
        n, m, q, s = map(int, lines[index].split(" "))
        index += 1

        adjacent = [list() for _ in range(n)]

        for _ in range(m):
            u, v, t0, p, d = map(int, lines[index].split(" "))
            adjacent[u].append((v, t0, p, d))

            index += 1

        costs, _ = time_table_dijkstra(adjacent, s)

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