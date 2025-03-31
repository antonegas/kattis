"""
author: Anton Nilsson
testcase 1:
in:
2
CZK EUR
2
CZK EUR 25:1
EUR CZK 1:25
2
GBP USD
2
USD GBP 8:5
GBP USD 5:9
3
BON DEM CZK
3
DEM BON 1:6
BON CZK 1:5
DEM CZK 1:20
3
CZK EUR GBP
3
CZK EUR 24:1
EUR GBP 5:4
GBP CZK 1:30
3
CZK USD GBP
4
CZK USD 28:1
CZK GBP 31:1
GBP CZK 1:31
USD GBP 1:1
0

out:
Ok
Arbitrage
Ok
Ok
Arbitrage

"""

import re

def floyd_warshall(graph: list[list[float]]) -> list[list[float]]:
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                graph[i][j] = max(graph[i][j], graph[i][k] * graph[k][j])

    return graph

if __name__ == "__main__":
    while True:
        C = int(input())

        if C == 0:
            break

        codes = list(input().split(" "))
        code_identifiers = {code: i for i, code in enumerate(codes)}

        R = int(input())

        exchanges = [[0.0] * C for _ in range(C)]

        for u in range(C):
            exchanges[u][u] = 1.0

        for _ in range(R):
            code1, code2, value1, value2 = re.split(" |:", input())
            u = code_identifiers[code1]
            v = code_identifiers[code2]
            exchanges[u][v] = int(value2) / int(value1)

        new_exchanges = floyd_warshall(exchanges)

        ok = True

        for u in range(C):
            if new_exchanges[u][u] > 1:
                ok = False
                break

        if ok:
            print("Ok")
        else:
            print("Arbitrage")