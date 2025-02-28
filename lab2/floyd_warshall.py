"""
author: Anton Nilsson
testcase 1:
in:
4 3 4
0 1 2
1 2 2
3 3 1
0 2
1 2
3 0
3 3
2 1 2
0 1 100
0 1
1 0
0 0 0

out:
4
2
Impossible
0

100
Impossible

"""

def floyd_warshall(original: list[list[float]]) -> list[list[float]]:
    """
    Given a graph finds the shortest path from one node to another.

    algorithm: The implemented algorithm is Floyd-Warshall. It works by going through every pair 
    of nodes and seeing if there exists a shorter path between them which goes through another node.
    Negative cycles are detected by running the algorithm again and seeing if it results in even 
    shorter paths.
    time complexity: O(|V|^3)
    where:
    - |V| is the the number of vertices.
    why:
    - O(|V|^3) from looping through every pair of vertices and check if going through the vertex k is shorter.
    reference: https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm#Pseudocode

    parameters:
    - original: a matrix with orignal[from][to] giving the weight of going from a node to another.
    returns:
    - A graph with the shortest paths from and to each pair of vertices.
    """

    graph = [destination[:] for destination in original] # Copy original graph.

    # Find the shortest paths from each node to every other node.
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                # Update the shortest path from i to j if going through k results in a lower weight.
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # Detect if there exists negative cycles by running the algorithm again and seeing if it 
    # results in shorter paths.
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                # If going through k results in a shorter distance there is a negative cycle.
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = float("-inf")

    return graph

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()[:-1]

    index = 0

    while index < len(lines):
        n, m, q = map(int, lines[index].split(" "))
        index += 1

        graph = [[float("inf")] * n for _ in range(n)]

        for u in range(n):
            graph[u][u] = 0

        for _ in range(m):
            u, v, w = map(int, lines[index].split(" "))
            graph[u][v] = min(graph[u][v], w)
            index += 1

        shortest_paths = floyd_warshall(graph)

        for _ in range(q):
            u, v = map(int, lines[index].split(" "))
            query_result = shortest_paths[u][v]

            if query_result == float("inf"):
                output.append("Impossible")
            elif query_result == float("-inf"):
                output.append("-Infinity")
            else:
                output.append(str(query_result))
            
            index += 1

        output.append("")

    open(1, "w").write("\n".join(output))