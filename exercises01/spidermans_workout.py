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
    # The max possible height that spiderman can reach is the sum of all distances.
    MAX_POSSIBLE = sum(distances) + 1
    highest = [[float("inf")] * MAX_POSSIBLE for _ in distances]
    directions = [[0] * MAX_POSSIBLE for _ in distances]

    # For the first distance the only allowed action is to climb up.
    highest[0][distances[0]] = distances[0]
    directions[0][distances[0]] = 1

    for d, distance in enumerate(distances[1:], 1):
        for height, max_height in enumerate(highest[d - 1]):
            # If max height is infinite it is not possible to reach the height using
            # the previous distances.
            if max_height == float("inf"):
                continue

            lower = height - distance
            higher = height + distance

            # Make that the lower height is not below street level. The minimum needed
            # height never increases after spiderman climbs down.
            if lower >= 0 and highest[d][lower] > max_height:
                highest[d][lower] = max_height
                directions[d][lower] = -1

            # Climbing up may increase the minimum needed max height.
            if highest[d][higher] > max(higher, max_height):
                highest[d][higher] = max(higher, max_height)
                directions[d][higher] = 1

    return directions

def get_path(distances: list[int], directions: list[list[int]]) -> list[str]:
    # If the direction is 0 at any (d, height) in the directions table it means the height is not
    # possible to reach using the previous distances. If this is the case for the ground level after
    # using all distances it is impossible to reach the street level after climbing.
    if directions[-1][0] == 0:
        return ["IMPOSSIBLE"]
    
    height = 0
    result = ["X" for _ in distances]

    # Backtrack through the distances to get the path with a minimal needed max height.
    for d, distance in reversed(list(enumerate(distances))):
        # The direction and distance decides the next height
        direction = directions[d][height]
        height -= distance * direction

        if direction == -1:
            result[d] = "D"
        elif direction == 1:
            result[d] = "U"

    return result

def solve(distances: list[int]) -> list[str]:
    # The sum of the distances needs to be even for spiderman to be able to reach the street again.
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