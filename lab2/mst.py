"""
author: Anton Nilsson
testcase 1:
in:
4 4
0 1 1
1 2 2
1 3 3
2 3 0
2 1
0 1 100
3 0
0 0

out:
3
0 1
1 2
2 3
100
0 1
Impossible

"""

def create_disjoint_sets(amount: int) -> tuple[list[int], list[int]]:
    """
    Given the number of sets creates the data structures to allow union-find O(logn) time complexity.
    """
    parent = list()
    rank = list()

    for i in range(amount + 1):
        parent.append(i)
        rank.append(0)

    return parent, rank

def disjoint_set_union(x: int, y: int, parent: list[int], rank: list[int]):
    """
    Given two elements performs the union operation on the sets which contains the 
    two elements by updating the parent and rank lists.
    """
    
    x_parent = disjoint_set_find(x, parent)
    y_parent = disjoint_set_find(y, parent)

    if x_parent != y_parent:
        if rank[x_parent] < rank[y_parent]:
            y_parent, x_parent = x_parent, y_parent
        parent[y_parent] = x_parent
        if rank[x_parent] == rank[y_parent]:
            rank[x_parent] += 1

def disjoint_set_find(x: int, parent: list[int]) -> int:
    """
    Given an element finds the root node of the tree which identifies the disjoint set.
    """
    
    if x == parent[x]:
        return x
    
    parent[x] = disjoint_set_find(parent[x], parent)
    return parent[x]

def disjoint_set_same(x: int, y: int, parent: list[int]):
    """
    Checks if two elements are in the same set.
    """
    return disjoint_set_find(x, parent) == disjoint_set_find(y, parent)

def kruskals_algorithm(edges: list[tuple[int, int, int]], vertices: int) -> list[tuple[int, int, int]]:
    """
    Finds a mimimum spanning tree using Kruskal's algorithm.

    algorithm: Put each node into a disjoint set data structure. Sort each edge by their weight. 
    Add new edges to the tree as long as they don't result in a cycle. Since the edges are sorted 
    based on weight the resulting tree will be a minimum spanning tree.
    time complexity: O(|E|*log|E|)
    where:
    - |V| is the number of vertices.
    - |E| is the number of edges.
    why:
    - O(|E|*log|E|) from sorting the edges by weight (python uses powersort/mergesort).
    - O(|V|) from creating the disjoint set from the vertices.
    - O(|V|*a(|V|)) from doing find and union on every vertex.
    - O(|E|*log(|E|)+|V|*a(|V|))=O(|E|*log|E|)
    reference: https://en.wikipedia.org/wiki/Kruskal%27s_algorithm#Pseudocode

    parameters:
    - edges: a list of tuples (weight, vertex 1, vertex 2) representing edges.
    - vertices: the number of vertices.
    returns:
    - A list of edges which are included in the minimum spanning tree.
    """
    
    tree = list()

    # Set up disjoint set data structure and sort edges based on weight.
    parent, rank = create_disjoint_sets(vertices)
    sorted_edges = sorted(edges)

    # Go over all sorted edges, add an edge to the minimum spanning tree if it 
    # doesn't result in a cycle.
    for w, u, v in sorted_edges:
        if not disjoint_set_same(u, v, parent):
            tree.append((w, u, v))
            disjoint_set_union(u, v, parent, rank)

    return tree

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()[:-1]

    index = 0

    while index < len(lines):
        n, m = map(int, lines[index].split(" "))
        index += 1
        edges = list()

        for _ in range(m):
            u, v, w = map(int, lines[index].split(" "))
            edges.append((w, u, v))
            index += 1

        tree = kruskals_algorithm(edges, n)

        if len(tree) < n - 1:
            output.append("Impossible")
            continue

        output.append(str(sum([w for w, _, _ in tree])))
        
        tree_edges = [(u, v) if u < v else (v, u) for _, u, v in tree]
        for u, v in sorted(tree_edges):
            output.append(f"{u} {v}")

    open(1, "w").write("\n".join(output))