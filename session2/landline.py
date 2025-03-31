"""
author: Anton Nilsson
testcase 1:
in:
4 6 1
1
1 2 1
1 3 1
1 4 1
2 3 2
2 4 4
3 4 3

out:
6

testcase 2:
in:
4 3 2
1 2
1 2 1
2 3 7
3 4 5

out:
impossible

"""

def create_disjoint_sets(amount: int) -> tuple[list[int], list[int]]:
    parent = list()
    rank = list()

    for i in range(amount + 1):
        parent.append(i)
        rank.append(0)

    return parent, rank

def disjoint_set_union(x: int, y: int, parent: list[int], rank: list[int]):
    x_parent = disjoint_set_find(x, parent)
    y_parent = disjoint_set_find(y, parent)

    if x_parent != y_parent:
        if rank[x_parent] < rank[y_parent]:
            y_parent, x_parent = x_parent, y_parent
        parent[y_parent] = x_parent
        if rank[x_parent] == rank[y_parent]:
            rank[x_parent] += 1

def disjoint_set_find(x: int, parent: list[int]) -> int:
    if x == parent[x]:
        return x
    
    parent[x] = disjoint_set_find(parent[x], parent)
    return parent[x]

def disjoint_set_same(x: int, y: int, parent: list[int]):
    return disjoint_set_find(x, parent) == disjoint_set_find(y, parent)

def kruskals(edges: list[tuple[int, int, int]], insecure: list[bool], vertices: int) -> list[tuple[int, int, int]]:
    tree = list()

    parent, rank = create_disjoint_sets(vertices)
    sorted_edges = sorted(edges)

    added = [False for _ in range(vertices)]

    for w, u, v in sorted_edges:
        if insecure[u] and added[u]:
            continue
        if insecure[v] and added[v]:
            continue

        if not disjoint_set_same(u, v, parent):
            tree.append((w, u, v))
            disjoint_set_union(u, v, parent, rank)

            added[u] = True
            added[v] = True

    return tree

if __name__ == "__main__":
    n, m, p = map(int, input().split())
    ps = []
    try:
        if p > 0:
            ps = list(map(int, input().split()))
    except:
        pass

    insecure = [False for _ in range(n)]

    if n != p:
        for p in ps:
            insecure[p - 1] = True

    edges = list()

    for _ in range(m):
        try:
            u, v, c = input().split()
        except:
            u = v = c = "0"

        try:
            u = int(u) - 1
            v = int(v) - 1
        except:
            u = v = 0

        try:
            if not insecure[u] or not insecure[v]:
                edges.append((int(c), u, v))
        except:
            pass
    
    try:
        tree = kruskals(edges, insecure, n)
    except:
        tree = []

    if len(tree) < n - 1:
        print("Impossible")
    else:
        print(sum([c for c, _, _ in tree]))