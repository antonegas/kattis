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
    for tree, left_tree, l in zip(sorted_trees, left_spots, range(1, len(left_spots) + 1)):
        minimum_distances[l][0] = minimum_distances[l - 1][0] + distance(tree, left_tree)
    for tree, right_tree, r in zip(sorted_trees, right_spots, range(1, len(right_spots) + 1)):
        minimum_distances[0][r] = minimum_distances[0][r - 1] + distance(tree, right_tree)

    # The optimal way to place the first tree is on the left side. The optimal way
    # to place the second tree is either on the left side or the right side depending
    # on which leads to the smallest total amount of distance trees are moved. 
    # Because of this both options are stored. The number of options increases by one 
    # for each following tree, until half the trees has been considered. After half the 
    # trees has been considered one of these options can be eliminated at a time, until 
    # all trees has been considered. 
    for l, left_tree in enumerate(left_spots):
        for r, right_tree in enumerate(right_spots):
            tree = sorted_trees[l + r + 1]
            left_distance = distance(left_tree, tree)
            right_distance = distance(right_tree, tree)

            left_alternative = minimum_distances[l][r + 1]
            right_alternative = minimum_distances[l + 1][r]

            left_minimum = left_distance + left_alternative
            right_minimum = right_distance + right_alternative

            minimum_distances[l + 1][r + 1] = min(left_minimum, right_minimum)

    return minimum_distances[-1][-1]

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