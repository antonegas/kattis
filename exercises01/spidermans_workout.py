"""
author: Anton Nilsson
time complexity: O(XXX)
space complexity: -
where:
- n is the XXX
why:
- O(XXX) from XXX
testcase XXX:
in:
5
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

out:
UDUD
UUDUDD
IMPOSSIBLE
UD
UUD

"""

def dynamic_programming(distances: list[int]) -> list[list[int]]:
    max_possible = sum(distances) + 1
    max_heights = [[float("inf") for _ in range(max_possible)] for _ in range(len(distances))]
    directions = [[0 for _ in range(max_possible)] for _ in range(len(distances))]

    max_heights[0][distances[0]] = distances[0]
    directions[0][distances[0]] = 1 

    for d, distance in enumerate(distances[1:]):
        for height in range(max_possible):
            max_height = max_heights[d][height]
            
            if max_height == float("inf"):
                continue

            lower_height = height - distance
            higher_height = height + distance

            if lower_height >= 0 and max_heights[d + 1][lower_height] > max_height:
                max_heights[d + 1][lower_height] = max_height
                directions[d + 1][lower_height] = -1
            
            if max_heights[d + 1][higher_height] > max(max_height, higher_height):
                max_heights[d + 1][higher_height] = max(max_height, higher_height)
                directions[d + 1][higher_height] = 1

    return directions
    

def get_path(distances: list[int], directions: list[list[int]]) -> list[str]:
    if directions[-1][0] == float("inf"):
        return ["IMPOSSIBLE"]
    
    result = list()
    current_height = 0

    for i in reversed(range(len(distances))):
        current_distance = distances[i]
        direction = directions[i][current_height]
        if direction == 1:
            current_height -= current_distance
            result.append("U")
        else:
            current_height += current_distance
            result.append("D")

    return list(reversed(result))


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