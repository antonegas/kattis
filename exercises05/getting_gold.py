"""
author: Anton Nilsson
testcase 1:
in:
7 4
#######
#P.GTG#
#..TGG#
#######

out:
1

testcase 2:
in:
8 6
########
#...GTG#
#..PG.G#
#...G#G#
#..TG.G#
########

out:
4

"""

from collections import deque

def getting_gold(width: int, height: int, grid: list[str]) -> int:
    visited = [[False] * width for _ in range(height)]
    queue = deque()

    for x in range(width):
        for y in range(height):
            if grid[y][x] == "P":
                start = (x, y)
                visited[y][x] = True
                queue.append(start)
                break

        if len(queue) == 1:
            break

    gold = 0

    while queue:
        x, y = queue.popleft()

        if grid[y][x] == "G":
            gold += 1

        neighbors = [(x + dx, y + dy) for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]]
        symbols = [grid[y][x] for x, y in neighbors]

        if "T" in symbols:
            continue

        for coord, symbol in zip(neighbors, symbols):
            if symbol == "#":
                continue

            nx, ny = coord

            if visited[ny][nx]:
                continue

            visited[ny][nx] = True

            queue.append(coord)

    return gold

if __name__ == "__main__":
    data = open(0, "r").read().splitlines()

    width, height = map(int, data[0].split(" "))
    grid = data[1:]

    print(getting_gold(width, height, grid))