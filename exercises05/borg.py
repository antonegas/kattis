"""
author: Anton Nilsson
testcase 1:
in:
2
6 5
##### 
#A#A##
# # A#
#S  ##
##### 
7 7
#####  
#AAA###
#    A#
# S ###
#     #
#AAA###
#####  

out:
8
11 

testcase 2:
in:
1
14 3
##############
#S          A#
##############

out:
11

"""

from collections import deque

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
    """
    
    tree = list()

    parent, rank = create_disjoint_sets(vertices)
    sorted_edges = sorted(edges)

    for w, u, v in sorted_edges:
        if not disjoint_set_same(u, v, parent):
            tree.append((w, u, v))
            disjoint_set_union(u, v, parent, rank)

    return tree

def bfs(maze: list[str], positions: list[list[int]], start: tuple[int, int, int]) -> list[tuple[int, int, int]]:
    visited = [[False] * len(maze[0]) for _ in range(len(maze))]
    q = deque()

    index, x, y = start
    visited[y][x] = True
    q.append((0, x, y))

    edges = list()

    while q:
        w, x, y = q.popleft()
        position_index = positions[y][x]

        if position_index > index:
            edges.append((w, index, position_index))

        neighbors = [(w + 1, x + dx, y + dy) for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]]

        for w, x, y in neighbors:
            if maze[y][x] == "#":
                continue

            if visited[y][x]:
                continue

            visited[y][x] = True

            q.append((w, x, y))

    return edges

def borg(maze: list[str]) -> int:
    positions = list()
    maze_positions = [[-1] * len(maze[0]) for _ in range(len(maze))]

    for y, line in enumerate(maze):
        for x, character in enumerate(line):
            if character in "AS":
                index = len(positions)
                maze_positions[y][x] = index
                positions.append((index, x, y))

    edges = list()

    for position in positions:
        edges.extend(bfs(maze, maze_positions, position))

    return sum(w for w, _, _ in kruskals_algorithm(edges, len(positions)))


if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()[1:]

    index = 0

    while index < len(lines):
        _, height = map(int, lines[index].split(" "))
        index += 1

        maze = list()

        for _ in range(height):
            maze.append(lines[index])
            index += 1

        output.append(str(borg(maze)))

    open(1, "w").write("\n".join(output))