"""
author: Anton Nilsson
testcase 1:
in:
4
10 1
1
0
10
10

out:
2.4142135624

testcase 2:
in:
6
10 1
0
9
3
5
5
6

out:
9.2853832858

testcase 3:
in:
4
2 1
0
1
1
2

out:
2.828427124746

testcase 4:
in:
4
2 1
0
1
1
1

out:
3.8284271247462
"""

def get_spots(number_of_trees: int, length: float, width: float) -> tuple[list[tuple[float, float]], list[tuple[float, float]]]:
    # Half the trees are placed on the left side and half on the right side.
    # On each side of the avenue the trees are placed evenly.
    number_half_trees = number_of_trees // 2
    distance = length / (number_half_trees - 1)
    left = list()
    right = list()

    for i in range(number_half_trees):
        # At each multiple (n/2>=i>=0) of the distence there is a tree on the left side
        # and on the right side.
        left.append((distance * i, 0))
        right.append((distance * i, width))

    return left, right

def distance(tree1: tuple[float, float], tree2: tuple[float, float]):
    x1, y1 = tree1
    x2, y2 = tree2
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def dynamic_programming(trees: list[tuple[float, float]], left_spots: list[tuple[float, float]], right_spots: list[tuple[float, float]]) -> float:
    # The spots where trees should be placed on the left and right side of the road is
    # order based on their distance from the start of the road. The dropped trees should
    # also be order this way too. 
    sorted_trees = sorted(trees)
    minimum_distances = [[float("inf")] * (len(right_spots) + 1) for _ in range(len(left_spots) + 1)]

    # The distance the trees have been moved at the start is 0.
    minimum_distances[0][0] = 0

    # The dropped trees can either be placed at left or right side of the avenue at 
    # the closest unoccupied spot. If only one side of the avenue and the first half 
    # of the trees was regarded, the optimal way to move the trees to the correct 
    # spots would be in the order they appear in. The first column is initialized as
    # if only the left side was regarded and the top row is initialized as if only
    # the right side was regarded.
    for tree, left_spot, l in zip(sorted_trees, left_spots, range(1, len(left_spots) + 1)):
        minimum_distances[l][0] = minimum_distances[l - 1][0] + distance(tree, left_spot)
    for tree, right_spot, r in zip(sorted_trees, right_spots, range(1, len(right_spots) + 1)):
        minimum_distances[0][r] = minimum_distances[0][r - 1] + distance(tree, right_spot)

    # The value in the cell at row l and column r is a minimum distance to move the 
    # first l + r trees. It represents the minimum distance to move the trees in the
    # specific case that l trees has been placed on the left side of the avenue and
    # r trees on the right side.
    for l, left_spot in enumerate(left_spots, 1):
        for r, right_spot in enumerate(right_spots, 1):
            # Given that we chose to place the (l + r):th tree on the left or right
            # side of the avenue the distance it has to be moved is the distance
            # between the dropped tree position to the l:th or r:th spot on the side
            # of the avenue.
            tree = sorted_trees[l + r - 1]
            left_distance = distance(left_spot, tree)
            right_distance = distance(right_spot, tree)

            # To determine if the (l + r):th tree should be placed on the left or
            # right side of the avenue either the best way to place r trees on
            # the right side or l trees on the left side of the avenue has to be
            # considered

            # If the (l + r):th tree is placed on the left side of the avenue the
            # minimum total distance to place l - 1 trees on the left side of the
            # avenue and r trees on the right side has to be considered and vice versa.
            left_alternative = minimum_distances[l - 1][r]
            right_alternative = minimum_distances[l][r - 1]
            left_total = left_distance + left_alternative
            right_total = right_distance + right_alternative
            minimum_distances[l][r] = min(left_total, right_total)

    return minimum_distances[len(left_spots)][len(right_spots)]

def solve(length: int, width: int, trees: list[tuple[float, float]]) -> float:
    left, right = get_spots(len(trees), length, width)

    return dynamic_programming(trees, left, right)

if __name__ == "__main__":
    output = ""
    data = open(0, "r").read()
    length, width = map(int, data.split("\n")[1].split(" "))
    trees = [(float(x), 0.0) for x in data.split("\n")[2:-1]]

    output += f"{solve(length, width, trees)}" + "\n"

    open(1, "w").write(output)