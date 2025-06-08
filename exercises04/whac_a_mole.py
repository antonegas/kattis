"""
author: Anton Nilsson
testcase 1:
in:
4 2 6
0 0 1
3 1 3
0 1 2
0 2 2
1 0 2
2 0 2
5 4 3
0 0 1
1 2 1
2 4 1
0 0 0

out:
4
2

"""

from math import gcd, ceil, sqrt

def get_reachable(max_reach: int) -> list[list[list[tuple[int, int]]]]:
    reachable = [list() for _ in range(max_reach + 1)]

    for dx in range(-max_reach, max_reach + 1):
        for dy in range(-max_reach, max_reach + 1):
            distance = ceil(sqrt(dx**2 + dy**2))

            if distance > max_reach:
                continue

            divisor = distance

            if dx != 0 and dy != 0:
                divisor = gcd(dx, dy)

            holes = [(0, 0)]

            for scalar in range(1, divisor + 1):
                holes.append((dx * scalar // divisor, dy * scalar // divisor))

            reachable[distance].append(holes)

    return reachable

def whac_a_mole(size: int, reachable: list[list[tuple[int, int]]], duration: int, moles: list[tuple[int, int, int]]) -> int:
    points = [[[0] * size for _ in range(size)] for _ in range(duration + 1)]
    mole_positions = [[[0] * size for _ in range(size)] for _ in range(duration)]

    for x, y, t in moles:
        points[t][y][x] = -1
        mole_positions[t][y][x] = 1

    max_points = 0

    for t in range(duration):
        for x in range(size):
            for y in range(size):
                if points[t][y][x] == 0:
                    continue

                if points[t][y][x] == -1:
                    points[t][y][x] = 0

                for ds in reachable:
                    last_dx, last_dy = ds[-1]
                    last_x = x + last_dx
                    last_y = y + last_dy

                    if last_x < 0 or last_x >= size:
                        continue
                    if last_y < 0 or last_y >= size:
                        continue

                    received_points = sum([mole_positions[t][y + dy][x + dx] for dx, dy in ds]) + points[t][y][x]

                    points[t + 1][last_y][last_x] = max(points[t + 1][last_y][last_x], received_points)

                    max_points = max(max_points, points[t + 1][last_y][last_x])

    return max_points

if __name__ == "__main__":
    reachable = get_reachable(5)
    n, d, m = map(int, input().split(" "))

    while n != 0 and d != 0 and m != 0:
        moles = list()
        duration = 0
        
        for _ in range(m):
            x, y, t = map(int, input().split(" "))
            moles.append((x + d, y + d, t - 1))
            duration = max(duration, t)

        current_reachable = [x for xs in reachable[:d + 1] for x in xs]

        print(whac_a_mole(n + d * 2, current_reachable, duration, moles))

        n, d, m = map(int, input().split(" "))