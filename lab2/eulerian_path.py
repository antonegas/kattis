"""
author: Anton Nilsson
testcase 1:
in:
4 4
0 1
1 2
1 3
2 3
2 2
0 1
1 0
2 1
0 1
0 0

out:
Impossible
0 1 0
0 1

"""

def eulerian_path(adjacent: list[list[int]]) -> list[tuple[int, int]]:
    """
    Given a graph gives an Eularian path in the graph if one exists

    algorithm: Checks if there exists an Eulerian path by checking the in- and out degrees of every 
    vertex. If every vertex has an in degree equal to its out degree there exists an Eulerian path. 
    There also exists an Eulerian path if there is one vertex with an in degree equal to its out 
    degree minus one and one vertex with an in degree equal to its out degree plus one. The algorithm 
    for finding the first case is to find a simple cycle an then inserting other simple cycles in the 
    graph into this cycle. For the second case the algorithm is the same just that one out edge is 
    added to the start of the path and one in edge to the end of the path, from the vertices where 
    the in- and out degree wasn't equal.
    time complexity: O(|V|+|E|)
    where:
    - |V| is the number of vertices.
    - |E| is the number of edges.
    why:
    - O(|E|) from searching every edge.
    - O(|V|) from searching every vertex.
    reference: https://www.topcoder.com/thrive/articles/eulerian-path-and-circuit-in-graphs

    parameters:
    - adjacent: a list of lists where adjacent[u] gives the list of all edges from u.
    returns:
    - An empty list if there doesn't exist an Eulerian path in the graph.
    - A list of edges in the Eulerian path if there is one in the graph.
    """
    
    # Calculate the in- and out degree of every vertex.
    in_degree = [0 for _ in range(len(adjacent))]
    out_degree = [0 for _ in range(len(adjacent))]
    edges = 0

    for u in range(len(adjacent)):
        for v in adjacent[u]:
            out_degree[u] += 1
            in_degree[v] += 1
            edges += 1
    
    # Check for the existence of an Eulerian path. If there is an Eulerian path will also find first and 
    # last vertex in the path if those need to be specific vertices. If they don't need to be specific 
    # vertices will find a possible vertex to start the search from
    first = -1
    last = -1
    start = 0

    for vertex in range(len(adjacent)):

        # Verify that all vertices have equal in- and out degrees or that at most one vertex has one more 
        # out degree than in and one has one more in degree than out.
        if start < 0 and out_degree[vertex] > 0:
            start = vertex
        if in_degree[vertex] == out_degree[vertex]:
            continue
        if abs(in_degree[vertex] - out_degree[vertex]) > 1:
            return []
        if out_degree[vertex] - in_degree[vertex] == 1 and first >= 0:
            return []
        if in_degree[vertex] - out_degree[vertex] == 1 and last >= 0:
            return []
        
        # Set first and last vertex if they need to be specified.
        if out_degree[vertex] - in_degree[vertex] == 1:
            first = vertex
        elif in_degree[vertex] - out_degree[vertex] == 1:
            last = vertex

    # If there are no edges there is no Eulerian path.
    if edges == 0:
        return []
    
    # If a first in the path was found start the search from it.
    if first >= 0:
        start = first

    # Search through the modified graph to find Eularian circuits.
    adjacent_offset = [0 for _ in range(len(adjacent))]
    stack = [start]
    vertex_path = list()

    while stack:
        u = stack[-1]

        if adjacent_offset[u] == len(adjacent[u]):
            vertex_path.append(u)
            stack.pop()
        else:
            v = adjacent[u][adjacent_offset[u]]
            adjacent_offset[u] += 1
            stack.append(v)

    # If the path doesn't include all edges it isn't Eularian.
    if len(vertex_path) != edges + 1:
        return []
    
    # Fix the path to be a list of edges.
    vertex_path = list(reversed(vertex_path))
    path = list(zip(vertex_path, vertex_path[1:]))
            
    return path

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()[:-1]

    index = 0

    while index < len(lines):
        n, m = map(int, lines[index].split(" "))
        index += 1

        adjacent = [list() for _ in range(n)]

        for _ in range(m):
            u, v = map(int, lines[index].split(" "))

            adjacent[u].append(v)
            
            index += 1

        path = eulerian_path(adjacent)

        if path:
            output.append(" ".join(map(str, [edge[0] for edge in path] + [path[-1][1]])))
        else:
            output.append("Impossible")

    open(1, "w").write("\n".join(output))