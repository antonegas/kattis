"""
author: Anton Nilsson
testcase 1:
in:
2
10
4 4
OOGO
XXOO
XOOX
XXOO
XXOO
OOFO
2
2 2
OG
XX
OO
FO

out:
The minimum number of turns is 9.
The problem has no solution.

"""

from collections import deque

def contains_car(motorway, x, y, t):
    direction = (len(motorway) - 1 - y) % 2 * 2 - 1
    return motorway[y][(x - direction * t) % len(motorway[0])] == "X"

def frogger(max_time: int, n: int, m: int, motorway: list[str]):
    visited = [[[False] * m for _ in range(m)] for _ in range(n + 2)]
    queue = deque()

    fx = motorway[-1].find("F")
    start = (fx, n + 1, 0)
    visited[n + 1][fx][0]

    queue.append(start)

    while queue:
        x, y, t = queue.popleft()

        if t > max_time:
            continue

        if motorway[y][x] == "G":
            return t
        
        neighbors = [(x + dx, y + dy, t + 1) for dx, dy in [(0, 0), (1, 0), (0, -1), (-1, 0), (0, 1)]]

        for nx, ny, nt in neighbors:
            if nx < 0 or nx >= m or ny < 0 or ny >= n + 2:
                continue

            if contains_car(motorway, nx, ny, nt):
                continue

            if visited[ny][nx][nt % m]:
                continue

            visited[ny][nx][nt % m] = True
            queue.append((nx, ny, nt))

    return -1

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()[1:]

    x = 0
    n = 0
    m = 0
    index = 0

    while index < len(lines):
        x = int(lines[index])
        n, m = map(int, lines[index + 1].split(" "))
        motorway = lines[index + 2:index + n + 4]

        t = frogger(x, n, m, motorway)

        if t < 0:
            print("The problem has no solution.")
        else:
            print(f"The minimum number of turns is {t}.")

        index += n + 4

    open(1, "w").write("\n".join(output))