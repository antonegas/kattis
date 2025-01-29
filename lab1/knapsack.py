"""
author: Anton Nilsson
testcase 1:
in:
5 3
1 5
10 5
100 5
6 4
5 4
4 3
3 2
2 1

out:
1
2
3
1 2 3

"""

def knapsack(max_capacity: int, items: list[tuple[int, int]]) -> list[int]:
    """
    Given knapsack with limited capacity and a set of items with a weight and values, 
    gives the indices of items which maximizes the value of the items packed in the knapsack.

    algorithm: The algorithm used is dynamic programming. The table consists of the capacity
    as columns and the items as rows. It loops through the rows and columns to determine 
    given a capacity (column) and a subset of items (row) the maximum value of items packed
    from the subset of items without exceeding the capacity.
    time complexity: O(n*c)
    space complexity: O(n*c)
    where:
    - n is the number of values/weigths.
    - c is the maximum capacity of the knapsack.
    why:
    - O(n) from looping over the items.
    - O(c) from looping over the capacities.
    - O(1) for random accesses in a list.
    - The indices of items packed needs to be stored in n*c matrix hence the space complexity.
    reference: https://en.wikipedia.org/wiki/Knapsack_problem#0-1_knapsack_problem

    parameters:
    - capacity: the limited capacity of the knapsack.
    - weights: a list of the weights of each item.
    - values: a list of the value of each item.
    returns:
    - The maximum possible utilization of the limited capacity of the knapsack when packing 
    the items.
    """

    # Extract values and weights from items.
    values, weights = zip(*items)

    # Initialize the max possible value for all capacities and weights to be zero.
    max_values = [[0] * (max_capacity + 1) for _ in range((len(weights) + 1))]
    
    # Iterate through max values and update based on previously calculated capacities and items.
    for weight, value, item in zip(weights, values, range(1, len(weights) + 1)):
        for capacity in range(1, max_capacity + 1):
            if weight > capacity:
                max_values[item][capacity] = max_values[item - 1][capacity]
            else:
                alternative1 = max_values[item - 1][capacity]
                alternative2 = max_values[item - 1][capacity - weight] + value
                max_values[item][capacity] = max(alternative1, alternative2)

    # To get the indices of the included items the max values table is backtracked through.
    # The backtracking starts at the max capacity and the last item. The backtracking then
    # continues until the first item its reached.
    indices = list()

    capacity = max_capacity

    for item in reversed(range(1, len(weights) + 1)):
        # An item was packed in the knapsack if going back one item the value was lower at 
        # the current capacity.
        if max_values[item][capacity] > max_values[item - 1][capacity]:
            indices.append(item - 1)

            # Decrease the capacity to check with the weight of an item if it was packed.
            capacity -= weights[item - 1]

    return indices

def solve(max_capacity: int, items: list[tuple[int, int]]) -> list[int]:
    return knapsack(max_capacity, items)

if __name__ == "__main__":
    output = ""
    data = open(0, "r").read()
    pairs: list[tuple[int, int]] = [tuple(map(int, line.split(" "))) for line in data.split("\n")[:-1]]
    
    i = 0
    while i < len(pairs):
        max_capacity, number_of_items = pairs[i]
        i += 1

        items = pairs[i:i + number_of_items]
        optimal_packing = solve(max_capacity, items)
        i += number_of_items

        output += f"{len(optimal_packing)}\n"
        output += " ".join(map(str, optimal_packing)) + "\n"

    open(1, "w").write(output)