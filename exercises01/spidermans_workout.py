"""
author: Anton Nilsson
testcase 1:
in:
6
4
20 20 20 20
6
3 2 5 3 1 2
7
3 4 2 1 6 4 5
2
1 1
3
1 1 2
3
2 2 2

out:
UDUD
UUDUDD
IMPOSSIBLE
UD
UUD
IMPOSSIBLE

"""

def dynamic_programming(distances: list[int]) -> list[list[int]]:
    MAX_POSSIBLE = sum(distances) + 1
    highest = [[float("inf")] * MAX_POSSIBLE for _ in distances]
    directions = [[0] * MAX_POSSIBLE for _ in distances]

    highest[0][distances[0]] = distances[0]
    directions[0][distances[0]] = 1

    for d, distance in enumerate(distances[1:], 1):
        for height, max_height in enumerate(highest[d - 1]):
            if max_height == float("inf"):
                continue

            lower = height - distance
            higher = height + distance

            if lower >= 0 and highest[d][lower] > max_height:
                highest[d][lower] = max_height
                directions[d][lower] = -1

            if highest[d][higher] > max(higher, max_height):
                highest[d][higher] = max(higher, max_height)
                directions[d][higher] = 1

    return directions

def get_path(distances: list[int], directions: list[list[int]]) -> list[str]:
    if directions[-1][0] == 0:
        return ["IMPOSSIBLE"]
    
    height = 0
    result = ["X" for _ in distances]

    for d, distance in reversed(list(enumerate(distances))):
        direction = directions[d][height]
        height -= distance * direction
        if direction == -1:
            result[d] = "D"
        elif direction == 1:
            result[d] = "U"

    return result

def solve(distances: list[int]) -> list[str]:
    if sum(distances) % 2:
        return ["IMPOSSIBLE"]

    directions = dynamic_programming(distances)

    return get_path(distances, directions)

if __name__ == "__main__":
    result = ""
    data = open(0, "r").read()
    all_distances = [list(map(int, x.split(" "))) for x in data.split("\n")[2::2]]

    for distances in all_distances:
        result += "".join(solve(distances)) + "\n"

    open(1, "w").write(result)