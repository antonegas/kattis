"""
author: Anton Nilsson
testcase 1:
in:
6 7
1 3
1 4
3 2
4 2
5 6
6 5
3 4

out:
3

testcase 2:
in:
6 8
1 3
1 4
3 2
4 2
5 6
6 5
3 4
4 3

out:
inf

testcase 3:
in:
31 60
1 3
1 3
3 4
3 4
4 5
4 5
5 6
5 6
6 7
6 7
7 8
7 8
8 9
8 9
9 10
9 10
10 11
10 11
11 12
11 12
12 13
12 13
13 14
13 14
14 15
14 15
15 16
15 16
16 17
16 17
17 18
17 18
18 19
18 19
19 20
19 20
20 21
20 21
21 22
21 22
22 23
22 23
23 24
23 24
24 25
24 25
25 26
25 26
26 27
26 27
27 28
27 28
28 29
28 29
29 30
29 30
30 31
30 31
31 2
31 2

out:
073741824

"""

def dfs(u: int, adjacent: list[list[int]], parent: list[int], visited: list[bool]) -> float:
    visited[u] = True

    for v in adjacent[u]:
        if not visited[v]:
            parent[v] = u
            dfs(v, adjacent, parent, visited)

if __name__ == "__main__":
    n, m = map(int, input())

    adjacent = [list() for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input())

        u = u - 1
        v = v - 1

        adjacent[u].append(v)

    parent = [-1] * n
    parent[0] = 0
    visited = [False] * n

    dfs(0, adjacent, parent, visited)

    visited = [False] * n
    count = [0] * n

    if roads == float("inf"):
        print("inf")
    else:
        print(str(int(roads))[-9:])