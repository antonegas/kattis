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
from math import ceil

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

def dfs(u: int, pushed: int, sink: int, ptr: list[int], level: list[int], capacity: list[list[int]], flow: list[list[int]]) -> int:
    if u == sink or pushed == 0:
        return pushed

    while ptr[u] < len(flow):
        v = ptr[u]

        if level[u] + 1 == level[v]:
            delta = dfs(v, min(pushed, capacity[u][v] - flow[u][v]), sink, ptr, level, capacity, flow)

            if delta > 0:
                flow[u][v] += delta
                flow[v][u] -= delta
                return delta

        ptr[u] += 1    
    
    return 0

def dinic(graph: list[list[int]], adjacent: list[list[int]], source: int, sink: int) -> list[list[int]]:
    capacity = [u[:] for u in graph]
    flow = [[0] * len(adjacent) for _ in range(len(adjacent))]

    level = bfs(source, capacity, flow, adjacent)

    while level[sink] != -1:
        ptr = [0] * len(adjacent)

        while dfs(source, 10**8, sink, ptr, level, capacity, flow) > 0:
            pass

        level = bfs(source, capacity, flow, adjacent)

    return flow

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()[1:]

    index = 0

    while len(lines) > index:
        n = int(lines[index])
        index += 1

        club_nodes = dict()
        resident_nodes = dict()
        party_nodes = dict()

        edges = list()
        club_resident_edges = list()

        source = 0
        sink = 1
        total_nodes = 2

        for _ in range(n):
            resident, party, _, *clubs = lines[index].split(" ")

            if resident not in resident_nodes:
                resident_nodes[resident] = total_nodes
                total_nodes += 1

            if party not in party_nodes:
                party_nodes[party] = total_nodes
                total_nodes += 1

            resident_party_edge = (resident_nodes[resident], party_nodes[party], 1)
            edges.append(resident_party_edge)

            for club in clubs:
                if club not in club_nodes:
                    club_nodes[club] = total_nodes
                    total_nodes += 1
                
                club_resident_edge = (club_nodes[club], resident_nodes[resident])
                edges.append(club_resident_edge + (1,))
                club_resident_edges.append(club_resident_edge + (club, resident,))

            index += 1

        party_limit = (len(club_nodes) - 1) // 2

        for party_node in party_nodes.values():
            party_sink_edge = (party_node, sink, party_limit)
            edges.append(party_sink_edge)

        for club_node in club_nodes.values():
            source_club_edge = (source, club_node, 1)
            edges.append(source_club_edge)

        graph = [[0] * total_nodes for _ in range(total_nodes)]
        adjacent = [list() for _ in range(total_nodes)]

        for u, v, capacity in edges:
            if graph[u][v] == 0 and graph[v][u] == 0:
                adjacent[u].append(v)
                adjacent[v].append(u)
            graph[u][v] += capacity

        flow_graph = dinic(graph, adjacent, source, sink)

        flow = sum(flow_graph[source])

        if flow != len(club_nodes):
            output.append("Impossible.")
            output.append("")
            continue

        for u, v, club, resident in club_resident_edges:
            if flow_graph[u][v] > 0:
                output.append(f"{resident} {club}")

        output.append("")

    open(1, "w").write("\n".join(output))