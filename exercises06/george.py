"""
author: Anton Nilsson
testcase 1:
in:
6 5
1 6 20 4
5 3 2 4
1 2 2
2 3 8
2 4 3
3 6 10
3 5 15

out:
21

testcase 2:
in:
8 9
1 5 5 5
1 2 3 4 5
1 2 8
2 7 4
2 3 10
6 7 40
3 6 5
6 8 3
4 8 4
4 5 5
3 4 23

out:
40

"""

from heapq import heappop, heappush

def blocked_dijkstra(timetable: list[list[tuple[int, int, int]]], source: int) -> tuple[list[float], list[int]]:
    times = [float("inf")] * len(timetable)
    previous = [-1] * len(timetable)
    visited = [False] * len(timetable)

    queue = [(0, source, -1)]

    while queue:
        time, vertex, previous_vertex = heappop(queue)

        if visited[vertex]:
            continue

        times[vertex] = time
        previous[vertex] = previous_vertex
        visited[vertex] = True

        for adjacent_vertex, edge_time, blocked in timetable[vertex]:
            if time < blocked or time >= blocked + edge_time:
                adjacent_time = time + edge_time
                heappush(queue, (adjacent_time, adjacent_vertex, vertex))
            else:
                adjacent_time = blocked + 2 * edge_time
                heappush(queue, (adjacent_time, adjacent_vertex, vertex))

    return times, previous

def george(start: int, end: int, offset: int, route: list[int], graph: list[list[int]]) -> int:
    adjacent = [list() for _ in range(len(graph))]

    for a, b in zip(route, route[1:]):
        l = graph[a][b]
        graph[a][b] = -1
        graph[b][a] = -1

        adjacent[a].append((b, l, offset))
        adjacent[b].append((a, l, offset))

        offset += l

    for a in range(len(graph)):
        for b in range(len(graph)):
            if graph[a][b] != -1:
                l = graph[a][b]
                adjacent[a].append((b, l, float("inf")))

    return int(blocked_dijkstra(adjacent, start)[0][end])

if __name__ == "__main__":
    n, m = map(int, input().split(" "))
    start, end, offset, _ = map(int, input().split(" "))

    route = [u - 1 for u in map(int, input().split(" "))]
    graph = [[-1] * n for _ in range(n)]

    for _ in range(m):
        a, b, l = map(int, input().split(" "))
        graph[a - 1][b - 1] = l
        graph[b - 1][a - 1] = l

    print(george(start - 1, end - 1, -offset, route, graph))