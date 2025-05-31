"""
author: Anton Nilsson
testcase 1:
in:
5 8
2 1 0 0 1
1 2
3 4
2 3
4 5
3 1
2 4
1 4
3 5

5 4
4 4 1 0 3
1 3
2 3
3 4
4 5

-1

out:
2 0 2 2 2 1 2 2
NO

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
    graph[u][v] += capacity

def unfair_play(standings: list[int], matches: list[tuple[int, int]]):
    node_count = len(standings) + len(matches) + 2
    team_nodes = [0] + [len(matches) + team + 1 for team in range(len(standings))]
    graph = [[0] * node_count for _ in range(node_count)]
    adjacent = [list() for _ in range(node_count)]
    match_edges = list()

    source = 0
    sink = node_count - 1
    our_team = len(standings)

    max_allowed = standings[-1] - 1

    for i in range(1, len(matches) + 1):
        team1, team2 = matches[i - 1]

        match_edges.append((i, team_nodes[team2]))

        # Add edge with capacity 2 from source to match.
        add_edge(graph, adjacent, source, i, 2)

        if team1 == our_team or team2 == our_team:
            # If either team is ours add an edge from the match to our team.
            max_allowed += 2

            add_edge(graph, adjacent, i, team_nodes[our_team], 2)
        else:
            # If neither team is ours add edges from the match to each team.
            add_edge(graph, adjacent, i, team_nodes[team1], 2)
            add_edge(graph, adjacent, i, team_nodes[team2], 2)

    for team in range(len(standings)):
        if standings[team] > max_allowed:
            return list()
        
        # Add edge with maximum allowed points as capacity between team and sink.
        add_edge(graph, adjacent, team_nodes[team + 1], sink, max_allowed - standings[team])

    # Our team is allowed to score one more point than the other teams.
    graph[team_nodes[our_team]][sink] += 1

    flow_graph = dinic(graph, adjacent, source, sink)

    # Only possible if every match edge is at full capacity.
    if sum(flow_graph[0]) == len(matches) * 2:
        return [flow_graph[match][team] for match, team in match_edges]
    
    return list()

if __name__ == "__main__":
    block = input()

    while block != "-1":
        n, m = map(int, block.split(" "))
        standings = list(map(int, input().split(" ")))
        matches = list()

        for _ in range(m):
            team1, team2 = map(int, input().split(" "))
            matches.append((team1, team2))

        possible = unfair_play(standings, matches)

        if possible:
            print(*possible)
        else:
            print("NO")

        input()
        block = input()