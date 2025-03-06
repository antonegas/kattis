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
        clubs = set()
        residents = dict()
        parties = defaultdict(lambda: list())

        for _ in range(n):
            resident, club, _, *member_clubs = lines[index].split(" ")
            clubs = clubs.union(set(member_clubs))
            residents[resident] = member_clubs
            parties[club].append(resident)
            
            index += 1

        party_out_capacity = ceil(len(clubs) / 2) - 1
        n = 2 + len(clubs) + len(residents) + len(parties)

        club_nodes = dict()
        resident_nodes = dict()
        party_nodes = dict()

        source = 0
        sink = n - 1
        current_node = 1
        
        graph = [[0] * n for _ in range(n)]
        adjacent = [list() for _ in range(n)]
        person_party_edges = list()

        for club in clubs:
            club_nodes[club] = current_node

            graph[source][current_node] = 1
            adjacent[source].append(current_node)
            adjacent[current_node].append(source)

            current_node += 1

        for resident in residents:
            resident_nodes[resident] = current_node

            for club in residents[resident]:
                club_node = club_nodes[club]

                graph[club_node][current_node] = 1

                person_party_edges.append((club_node, current_node, resident, club))

                adjacent[club_node].append(current_node)
                adjacent[current_node].append(club_node)

            current_node += 1

        for club in parties:
            party_nodes[club] = current_node

            for resident in parties[club]:
                resident_node = resident_nodes[resident]

                graph[resident_node][current_node] = 1

                adjacent[resident_node].append(current_node)
                adjacent[current_node].append(resident_node)

            graph[current_node][sink] = party_out_capacity

            adjacent[current_node].append(sink)
            adjacent[sink].append(current_node)

            current_node += 1

        flow_graph = dinic(graph, adjacent, source, sink)

        flow = sum(flow_graph[source][i] for i in range(n))

        if flow < len(clubs):
            output.append("Impossible.")
            output.append("")
            continue

        for resident_node, party_node, resident, club in person_party_edges:
            if flow_graph[resident_node][party_node] == 1:
                output.append(f"{resident} {club}")

        output.append("")

    open(1, "w").write("\n".join(output))