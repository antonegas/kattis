"""
author: Anton Nilsson
testcase 1:
in:
5
2
1 2
2 3
2
2 3
2 3
5
1 2 3 4 5
2 5
10
1 2 2 2 2 2 2 2 2 2
3 6
10
1 2 2 2 2 2 2 2 2 2
0 0

out:
Game 1 -- 1 : 0
Game 2 -- 0 : 1
Game 3 -- 2 : 8
Game 4 -- 84 : 36
Game 5 -- 1 : 0

"""

from math import comb
from itertools import combinations
from collections import Counter

def count_wins(tiles: list[int], draws: int, target: int) -> int:
    outcomes1 = Counter()
    outcomes2 = Counter()

    tiles1 = tiles[:len(tiles)//2]
    tiles2 = tiles[len(tiles)//2:]

    for i in range(min(draws, len(tiles1)) + 1):
        for combination in combinations(tiles1, i):
            outcomes1[(i, sum(combination))] += 1

    for i in range(min(draws, len(tiles2)) + 1):
        for combination in combinations(tiles2, i):
            outcomes2[(i, sum(combination))] += 1

    return sum([outcomes1[(draw, value)] * outcomes2[(draws - draw, target - value)] for draw, value in outcomes1])

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()[1:]

    index = 0

    while index < len(lines):
        m = int(lines[index])
        index += 1

        tiles = list(map(int, lines[index].split(" ")))

        index += 1

        n, t = map(int, lines[index].split(" "))

        index += 1

        wins = count_wins(tiles, n, t)
        loses = comb(m, n) - wins

        output.append(f"Game {index // 3} -- {wins} : {loses}")

    open(1, "w").write("\n".join(output))