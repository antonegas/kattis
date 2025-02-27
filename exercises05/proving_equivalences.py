"""
author: Anton Nilsson
testcase 1:
in:
2
4 0
3 2
1 2
1 3

out:
4
2

testcase 2:
in:
1
8 13
1 2
2 3
2 5
2 6
3 4
3 7
4 3
4 8
5 1
5 6
6 7
7 6
7 8

out:
1

"""

def dfs(vertex: int, adjacent: list[list[int]], visited: list[bool], output: list[int]):
    visited[vertex] = True

    for adjacent_vertex in adjacent[vertex]:
        if visited[adjacent_vertex]:
            continue
        dfs(adjacent_vertex, adjacent, visited, output)
    
    output.append(vertex)

def strongly_connected_components(adjacent: list[list[int]]) -> tuple[list[int], list[list[int]]]:
    visited = [False] * len(adjacent)

    order = list()

    for vertex in range(len(adjacent)):
        if visited[vertex]:
            continue
        auxiliary = list()
        dfs(vertex, adjacent, visited, auxiliary)
        order.extend(auxiliary)

    reversed_adjacent = [list() for _ in range(n)]

    for vertex in range(len(adjacent)):
        for adjacent_vertex in adjacent[vertex]:
            reversed_adjacent[adjacent_vertex].append(vertex)

    visited = [False] * len(reversed_adjacent)
    roots = [0] * len(adjacent)
    components = list()

    for vertex in reversed(order):
        if visited[vertex]:
            continue
        component = list()
        dfs(vertex, reversed_adjacent, visited, component)
        root = min(component)
        components.append(root)
        for component_vertex in component:
            roots[component_vertex] = root

    adjacent_condensation = [list() for _ in range(len(adjacent))]

    for vertex in range(len(adjacent)):
        for adjacent_vertex in adjacent[vertex]:
            if roots[vertex] == roots[adjacent_vertex]:
                continue
            adjacent_condensation[roots[vertex]].append(roots[adjacent_vertex])

    return components, adjacent_condensation

def prove_equivalances(adjacent: list[list[int]]):
    components, adjacent_components = strongly_connected_components(adjacent)

    if len(components) == 1:
        return 0

    has_in = [False] * len(components)
    has_out = [False] * len(components)

    for c, component in enumerate(components):
        if len(adjacent_components[component]):
            has_out[c] = True
        for adjacent_component in adjacent_components[component]:
            has_in[components.index(adjacent_component)] = True

    missing_in = len([0 for yes in has_in if not yes])
    missing_out = len([0 for yes in has_out if not yes])

    return max(missing_in, missing_out)

if __name__ == "__main__":
    # Just needed for this exercise
    import sys
    sys.setrecursionlimit(50000)

    output = list()
    lines = open(0, "r").read().splitlines()[1:]

    index = 0

    while index < len(lines):
        n, m = map(int, lines[index].split(" "))
        index += 1

        proved_graph = [list() for _ in range(n)]

        for _ in range(m):
            s1, s2 = map(int, lines[index].split(" "))
            proved_graph[s1 - 1].append(s2 - 1)
            index += 1

        output.append(str(prove_equivalances(proved_graph)))


    open(1, "w").write("\n".join(output))