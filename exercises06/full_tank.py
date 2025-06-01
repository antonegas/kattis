"""
author: Anton Nilsson
testcase 1:
in:
5 5
10 10 20 12 13
0 1 9
0 2 8
1 2 1
1 3 11
2 3 7
2
10 0 3
20 1 4

out:
170
impossible

"""

from heapq import heappop, heappush

def full_tank(adjacent: list[list[tuple[int, int]]], prices: list[int], start: int, end: int, fuel_capacity: int) -> float:
    costs = [[float("inf")] * len(adjacent) for _ in range(fuel_capacity + 1)]
    visited = [[False] * len(adjacent) for _ in range(fuel_capacity + 1)]

    queue = [(0, 0, start)]

    while queue:
        cost, tank, u = heappop(queue)

        if u == end:
            return cost

        if visited[tank][u]:
            continue

        costs[tank][u] = cost
        visited[tank][u] = True

        if tank < fuel_capacity:
            heappush(queue, (cost + prices[u], tank + 1, u))

        for v, distance in adjacent[u]:
            if distance <= tank and not visited[tank - distance][v]:
                heappush(queue, (cost, tank - distance, v))

    return float("inf")

if __name__ == "__main__":
    n, m = map(int, input().split(" "))

    prices = [*map(int, input().split(" "))]
    adjacent = [list() for _ in range(n)]

    for _ in range(m):
        u, v, d = map(int, input().split(" "))

        adjacent[u].append((v, d))
        adjacent[v].append((u, d))

    q = int(input())

    for _ in range(q):
        capacity, start, end = map(int, input().split(" "))

        cheapest_trip = full_tank(adjacent, prices, start, end, capacity)
        
        if cheapest_trip != float("inf"):
            print(int(cheapest_trip))
        else:
            print("impossible")