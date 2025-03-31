"""
author: Anton Nilsson
testcase 1:
in:
0 0 10000 1000
0 200 5000 200 7000 200 -1 -1
2000 600 5000 600 10000 600 -1 -1

out:
21

"""

from heapq import heappop, heappush

def dijkstra(adjacent: list[list[tuple[int, float]]]) -> float:
    home = 0
    school = 1

    costs = [float("inf")] * len(adjacent)
    visited = [False] * len(adjacent)

    queue = [(0.0, home)]

    while queue:
        cost, vertex = heappop(queue)

        if visited[vertex]:
            continue

        costs[vertex] = cost
        visited[vertex] = True

        if vertex == school:
            break

        for adjacent_vertex, edge_cost in adjacent[vertex]:
            adjacent_cost = cost + edge_cost
            heappush(queue, (adjacent_cost, adjacent_vertex))

    return costs[school]

def dist(c1, c2):
    x1, y1 = c1
    x2, y2 = c2

    return ((x1-x2)**2 + (y1-y2)**2)**0.5

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()

    # KMH to meters/minute conversion
    FORTY_KMH = 40 * 1000 / 60
    TEN_KMH = 10 * 1000 / 60
    MAX_VERTICES = 202

    home_x, home_y, school_x, school_y = map(int, lines[0].split(" "))

    home = (0, home_x, home_y)
    school = (1, school_x, school_y)

    vertices = [home, school]

    n = 2

    subway_lines = list()

    for line in lines[1:]:
        coords = list(map(int, line.split(" ")))[:-2]
        stops = list(zip(range(n, MAX_VERTICES), coords[::2], coords[1::2]))
        n += len(stops)

        vertices.extend(stops)

        subway_lines.append(stops)

    adjacent = [list() for _ in range(n)]

    for i, x1, y1 in vertices:
        for j, x2, y2 in vertices:
            if i == j:
                continue
            adjacent[i].append((j, dist((x1, y1), (x2, y2)) / TEN_KMH))

    for subway_line in subway_lines:
        for i, j in zip(subway_line, subway_line[1:]):
            u, x1, y1 = i
            v, x2, y2 = j
            cost = dist((x1, y1), (x2, y2)) / FORTY_KMH

            adjacent[u].append((v, cost))
            adjacent[v].append((u, cost))

    print(round(dijkstra(adjacent)))