"""
author: Anton Nilsson
testcase 1:
in:
2
4
fred dinosaur 2 jets jetsons
john rhinocerous 2 jets rockets
mary rhinocerous 2 jetsons rockets
ruth platypus 1 rockets
4
fred dinosaur 2 jets jetsons
john rhinocerous 2 jets rockets
mary rhinocerous 2 jetsons rockets
ruth platypus 1 rockets

out:
fred jetsons
john jets
ruth rockets

fred jetsons
john jets
ruth rockets

testcase 2:
in:
1
1
fred dinosaur 2 jets jetsons

out:
Impossible.

"""

from collections import deque, defaultdict

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
    if capacity == 0:
        return

    if graph[u][v] == 0 and graph[v][u] == 0:
        adjacent[u].append(v)
        adjacent[v].append(u)
    graph[u][v] = capacity

def councilling(residents: dict[str, str], club_members: dict[str, list[str]]) -> list[tuple[str, str]]:
    node_count = 1

    club_nodes = {club: i for i, club in enumerate(club_members, 1)}
    node_count += len(club_nodes)

    resident_nodes = {resident: i for i, resident in enumerate(residents, node_count)}
    node_count += len(resident_nodes)

    party_nodes = {party: i for i, party in enumerate(set(residents.values()), node_count)}
    node_count += len(party_nodes)

    node_count += 1

    graph = [[0] * node_count for _ in range(node_count)]
    adjacent = [list() for _ in range(node_count)]

    source = 0
    sink = node_count - 1

    max_allowed = (len(club_nodes) - 1) // 2

    for club, u in club_nodes.items():
        add_edge(graph, adjacent, source, u, 1)

        for resident in club_members[club]:
            party = residents[resident]

            v = resident_nodes[resident]
            w = party_nodes[party]

            add_edge(graph, adjacent, u, v, 1)
            add_edge(graph, adjacent, v, w, 1)

    for w in party_nodes.values():
        add_edge(graph, adjacent, w, sink, max_allowed)

    flow_graph = dinic(graph, adjacent, source, sink)

    if sum(flow_graph[0]) != len(club_members):
        return list()

    result = list()

    for club in club_members:
        u = club_nodes[club]

        for resident in club_members[club]:
            v = resident_nodes[resident]

            if flow_graph[u][v] == 1:
                result.append((resident, club))

    return result

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())

        residents = dict()
        club_members = defaultdict(lambda: list())

        for i in range(n):
            resident, party, _, *clubs = input().split(" ")

            residents[resident] = party

            for club in clubs:
                club_members[club].append(resident)

        result = councilling(residents, club_members)

        if len(result) == 0:
            print("Impossible.")
        else:
            for resident, club in result:
                print(resident, club)

        print("")