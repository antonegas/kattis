"""
author: Anton Nilsson
testcase 1:
in:
2
3
1 1 0
NYN
YNY
NYN
7
7 3 3 2 0 0 5
NYNNNNN
YNYYNNN
NYNYYNN
NYYNYNN
NNYYNNN
NNNNNNY
NNNNNYN

out:
1
4

testcase 2:
in:
1
2
10 0
NY
YN

out:
10

"""

from collections import deque

def bfs(source: int, capacity: list[list[int]], flow: list[list[int]], adjacent: list[list[int]]) -> list[int]:
    level = [-1] * len(adjacent)
    level[source] = 0

    queue = deque()
    queue.append(source)

    while len(queue) > 0:
        u = queue.popleft()

        for v in adjacent[u]:
            if capacity[u][v] == flow[u][v] or level[v] != -1:
                continue
            level[v] = level[u] + 1
            queue.append(v)

    return level

def dfs(u: int, pushed: int, sink: int, edge_pointers: list[int], level: list[int], capacity: list[list[int]], flow: list[list[int]]) -> int:
    if u == sink or pushed == 0:
        return pushed

    while edge_pointers[u] < len(flow):
        v = edge_pointers[u]

        if level[u] + 1 == level[v] and capacity[u][v] - flow[u][v] > 0:
            delta = dfs(v, min(pushed, capacity[u][v] - flow[u][v]), sink, edge_pointers, level, capacity, flow)

            if delta > 0:
                flow[u][v] += delta
                flow[v][u] -= delta
                return delta

        edge_pointers[u] += 1
    
    return 0

def dinic(capacity: list[list[int]], adjacent: list[list[int]], source: int, sink: int) -> list[list[int]]:
    flow = [[0] * len(adjacent) for _ in range(len(adjacent))]

    level = bfs(source, capacity, flow, adjacent)

    while level[sink] != -1:
        edge_pointers = [0] * len(adjacent)

        while dfs(source, 10**8, sink, edge_pointers, level, capacity, flow) > 0:
            pass

        level = bfs(source, capacity, flow, adjacent)

    return flow

def add_edge(graph: list[list[int]], adjacent: list[list[int]], u: int, v: int, capacity: int):
    if graph[u][v] == 0 and graph[v][u] == 0:
        adjacent[u].append(v)
        adjacent[v].append(u)
    graph[u][v] = capacity

def risk(bordering: list[list[int]], armies: list[int]) -> int:
    node_count = len(armies) * 2 + 2
    graph = [[0] * node_count for _ in range(node_count)]
    adjacent = [list() for _ in range(node_count)]

    first_layer = [*range(1, len(armies) + 1)]
    second_layer = [u + len(armies) for u in first_layer]

    source = 0
    sink = node_count - 1

    bordering_nodes = [-1]

    for u in range(len(armies)):
        if armies[u] == 0:
            continue

        add_edge(graph, adjacent, source, first_layer[u], armies[u])
        add_edge(graph, adjacent, second_layer[u], sink, 1)

        for v in bordering[u]:
            if armies[v] > 0:
                add_edge(graph, adjacent, first_layer[u], second_layer[v], armies[u])
            elif bordering_nodes[-1] != second_layer[u]:
                bordering_nodes.append(second_layer[u])

    bordering_nodes = bordering_nodes[1:]
    
    bordering_count = len(bordering_nodes)
    total_armies = sum(armies)

    high = total_armies // bordering_count
    low = 1

    while low < high:
        middle = (high + low) // 2

        for u in bordering_nodes:
            graph[u][sink] = middle

        flow_graph = dinic(graph, adjacent, source, sink)
        possible = not any([graph[u][sink] - flow_graph[u][sink] for u in second_layer])

        if possible:
            low = middle + 1
        else:
            high = middle

    for u in bordering_nodes:
        graph[u][sink] = low

    flow_graph = dinic(graph, adjacent, source, sink)
    possible = not any([graph[u][sink] - flow_graph[u][sink] for u in second_layer])

    if possible:
        return low
    return low - 1

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())

        armies = [*map(int, input().split(" "))]
        bordering = [list() for _ in range(n)]

        for u in range(n):
            line = input()

            bordering[u].append(u)

            for v in range(n):
                if line[v] == "Y":
                    bordering[u].append(v)
        
        print(risk(bordering, armies))