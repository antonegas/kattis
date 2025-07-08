"""
author: Anton Nilsson
testcase 1:
in:
5
3 3
9 6 3
5 9 6
3 5 9
1 10
0 1 2 3 4 5 6 7 8 7
2 3
7 6 7
7 6 7
5 5
1 2 3 4 5
2 9 3 9 6
3 3 0 8 7
4 9 8 9 8
5 6 7 8 9
2 13
8 8 8 8 8 8 8 8 8 8 8 8 8
8 8 8 8 8 8 8 8 8 8 8 8 8

out:
Case #1:
a b b
a a b
a a a
Case #2:
a a a a a a a a a b
Case #3:
a a a
b b b
Case #4:
a a a a a
a a b b a
a b b b a
a b b b a
a a a a a
Case #5:
a b c d e f g h i j k l m
n o p q r s t u v w x y z

"""

def get_neighbors(graph: list[list[int]], x: int, y: int) -> list[tuple[int, int]]:
    neighbors = list()

    for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        u = x + dx
        v = y + dy

        if u < 0 or u >= len(graph[0]):
            continue
        if v < 0 or v >= len(graph):
            continue

        neighbors.append((u, v))

    return neighbors

def watershed(land: list[list[int]]) -> list[list[str]]:
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    queue = list()

    for y in range(len(land)):
        for x in range(len(land[y])):
            queue.append((land[y][x], y, x))

    intermediate = [[-1] * len(land[0]) for _ in range(len(land))]

    current = 0

    for level, y, x in sorted(queue):
        if intermediate[y][x] == -1:
            intermediate[y][x] = current
            current += 1

        for u, v in get_neighbors(intermediate, x, y):
            if intermediate[v][u] == -1 and level < land[v][u]:
                intermediate[v][u] = intermediate[y][x]

    regions = [["#"] * len(land[0]) for _ in range(len(land))]
    alphabet_map = [-1] * current

    letter = 0

    for y in range(len(land)):
        for x in range(len(land[0])):
            key = intermediate[y][x]

            if alphabet_map[key] == -1:
                alphabet_map[key] = letter
                letter += 1

            regions[y][x] = ALPHABET[alphabet_map[key]]

    return regions

if __name__ == "__main__":
    t = int(input())

    for i in range(1, t + 1):
        h, w = map(int, input().split(" "))
        land = [[*map(int, input().split(" "))] for _ in range(h)]

        print(f"Case #{i}:")

        for line in watershed(land):
            print(*line)