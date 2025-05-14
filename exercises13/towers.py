"""
author: Anton Nilsson
testcase 1:
in:
4
2^2^2
3^4
15
9^2

out:
Case 1:
15
2^2^2
3^4
9^2

testcase 2:
in:
7
2^2^2
2^2^1^2^2
1^1^1^1
1^2^1^1
3^4
15
9^2

out:
Case 1:
1^1^1^1
1^2^1^1
2^2^1^2^2
15
2^2^2
3^4
9^2

testcase 3:
in:
2
100^100
2^2^9

out:
Case 1:
2^2^9
100^100

"""

from functools import cmp_to_key
from math import log2

def n_exponantiations(tower: list[int]) -> tuple[list[int], int, float]:
    LIMIT = 1024

    current = 1

    for i, exponent in reversed(list(enumerate(tower))):
        if current * log2(exponent) > LIMIT:

            if i == 0:
                return [], 1, current * log2(exponent)
            else:
                return tower[:i], i + 1, current * log2(exponent) + log2(log2(tower[i - 1]))
            
        current = exponent ** current

    return [], 0, current

def compare(a: tuple[list[int], int, float], b: tuple[list[int], int, float]) -> int:
    a1, a2, a3 = a
    b1, b2, b3 = b
    
    if a2 > b2:
        return 1
    elif b2 > a2:
        return -1

    if a3 > b3:
        return 1
    elif b3 > a3:
        return -1
    
    for a4, b4 in reversed(list(zip(a1, b1))):
        if a4 > b4:
            return 1
        elif b4 > a4:
            return -1

    return 0

def sort_towers(towers: list[list[int]]):
    values = list()

    for tower in towers:
        if 1 in tower:
            tower = tower[:tower.index(1)]
        
        values.append(n_exponantiations(tower))

    return sorted(range(len(towers)), key=cmp_to_key(lambda a, b: compare(values[a], values[b])))

if __name__ == "__main__":
    output = list()
    tower_strings = open(0, "r").read().splitlines()[1:]

    towers = [list(map(int, string.split("^"))) for string in tower_strings]

    sorted_towers = sort_towers(towers)

    output.append("Case 1:")

    for index in sorted_towers:
        output.append(tower_strings[index])

    open(1, "w").write("\n".join(output))
