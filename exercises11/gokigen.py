r"""
author: Anton Nilsson
testcase 1:
in:
3
1.1.
...0
.3..
..2.

out:
\//
\\\
/\/

testcase 2:
in:
5
.21...
..33.0
......
..33..
0..33.
....11

out:
/\\//
//\\\
\\\//
\/\\/
///\\

testcase 3:
in:
6
.0...1.
......2
22..33.
..1.3..
.3....1
.213...
....21.

out:
\//\\\
//\\//
\\\//\
\\//\\
/\\\\\
/\/\//

testcase 4:
in:
6
.2.....
2.1.31.
..3.3..
.1...1.
2.3....
1...31.
...0.1.

out:
/\\\/\
\\////
/\\/\\
///\\/
\/\\/\
\//\\\

"""

from collections import deque

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

def get_intersection_index(x: int, y: int, size: int) -> int:
    return x + y * size

def test_slash(x: int, y: int, size: int, intersections: list[list[int]], parent: list[int], rank: list[int], solution: list[list[str]]) -> bool:
    top_right = (x + 1, y)
    bottom_left = (x, y + 1)

    top_right_index = get_intersection_index(*top_right, size)
    bottom_left_index = get_intersection_index(*bottom_left, size)

    parent_copy = parent[:]
    rank_copy = rank[:]

    if not disjoint_set_same(top_right_index, bottom_left_index, parent):
        disjoint_set_union(top_right_index, bottom_left_index, parent_copy, rank_copy)

        solution[y][x] = "/"

        x1, y1 = top_right
        x2, y2 = bottom_left

        intersections[y1][x1] -= 1
        intersections[y2][x2] -= 1
        
        if dfs(x + 1, y, size, intersections, parent_copy, rank_copy, solution):
            return True
        
        solution[y][x] = ""
        
        intersections[y1][x1] += 1
        intersections[y2][x2] += 1

    return False

def test_backslash(x: int, y: int, size: int, intersections: list[list[int]], parent: list[int], rank: list[int], solution: list[list[str]]) -> bool:
    top_left = (x, y)
    bottom_right = (x + 1, y + 1)

    top_left_index = get_intersection_index(*top_left, size)
    bottom_right_index = get_intersection_index(*bottom_right, size)

    parent_copy = parent[:]
    rank_copy = rank[:]

    if not disjoint_set_same(top_left_index, bottom_right_index, parent):
        disjoint_set_union(top_left_index, bottom_right_index, parent_copy, rank_copy)

        solution[y][x] = "\\"
        
        x1, y1 = top_left
        x2, y2 = bottom_right

        intersections[y1][x1] -= 1
        intersections[y2][x2] -= 1
        
        if dfs(x + 1, y, size, intersections, parent_copy, rank_copy, solution):
            return True
        
        solution[y][x] = ""

        intersections[y1][x1] += 1
        intersections[y2][x2] += 1

    return False

def dfs(x: int, y: int, size: int, intersections: list[list[int]], parent: list[int], rank: list[int], solution: list[list[str]]):
    # NOTE: This could maybe be faster if a bfs is run in each step to eliminate forced lines.
    if x == size - 1:
        x = 0
        y += 1
    if y == size - 1:
        return True

    right_extra = 0
    bottom_extra = 0

    if x == size - 2:
        right_extra = 1
    if y == size - 2:
        bottom_extra = 2

    if intersections[y][x] == 0 and intersections[y][x + 1] == 0:
        return False
    if intersections[y][x + 1] == 0 and intersections[y + 1][x + 1] == 0:
        return False
    if intersections[y + 1][x] == 0 and intersections[y][x] == 0:
        return False
    if intersections[y + 1][x + 1] == 0 and intersections[y + 1][x] == 0:
        return False
    
    if intersections[y][x] == 1 and intersections[y + 1][x + 1] == 0:
        return False
    if intersections[y][x + 1] + right_extra == 2 and intersections[y + 1][x] == 0:
        return False
    if intersections[y + 1][x] + bottom_extra == 3 and intersections[y][x + 1] == 0:
        return False
    if intersections[y + 1][x + 1] + right_extra + bottom_extra == 4 and intersections[y][x] == 0:
        return False
    
    if intersections[y][x] == 1 and intersections[y][x + 1] + right_extra == 2:
        return False
    if intersections[y][x + 1] + right_extra == 2 and intersections[y + 1][x + 1] + right_extra + bottom_extra == 4:
        return False
    if intersections[y + 1][x] + bottom_extra == 3 and intersections[y][x] == 1:
        return False
    if intersections[y + 1][x + 1] + right_extra + bottom_extra == 4 and intersections[y + 1][x] + bottom_extra == 3:
        return False
    
    if intersections[y][x] > 1:
        return False
    if intersections[y][x + 1] + right_extra > 2:
        return False
    if intersections[y + 1][x] + bottom_extra > 3:
        return False
    if intersections[y + 1][x + 1] + right_extra + bottom_extra > 4:
        return False

    if intersections[y][x] == 0:
        return test_slash(x, y, size, intersections, parent, rank, solution)
    if intersections[y][x + 1] == 0:
        return test_backslash(x, y, size, intersections, parent, rank, solution)
    if intersections[y + 1][x] == 0:
        return test_backslash(x, y, size, intersections, parent, rank, solution)
    if intersections[y + 1][x + 1] == 0:
        return test_slash(x, y, size, intersections, parent, rank, solution)

    if intersections[y][x] == 1:
        return test_backslash(x, y, size, intersections, parent, rank, solution)
    if intersections[y][x + 1] + right_extra == 2:
        return test_slash(x, y, size, intersections, parent, rank, solution)
    if intersections[y + 1][x] + bottom_extra == 3:
        return test_slash(x, y, size, intersections, parent, rank, solution)
    if intersections[y + 1][x + 1] + right_extra + bottom_extra == 4:
        return test_backslash(x, y, size, intersections, parent, rank, solution)

    if test_slash(x, y, size, intersections, parent, rank, solution):
        return True

    if test_backslash(x, y, size, intersections, parent, rank, solution):
        return True

    return False

def gokigen(intersections: list[list[int]]) -> list[list[str]]:
    size = len(intersections)
    parent, rank = create_disjoint_sets(size ** 2)
    solution = [[""] * (size - 1) for _ in range(size - 1)]

    dfs(0, 0, size, intersections, parent, rank, solution)

    return solution

if __name__ == "__main__":
    n = int(input())

    intersections = [[-1] * (n + 1) for _ in range(n + 1)]

    for y in range(n + 1):
        line = input()

        for x in range(n + 1):
            if line[x] == ".":
                continue

            intersections[y][x] = int(line[x])

    for line in gokigen(intersections):
        print("".join(line))