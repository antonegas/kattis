"""
author: Anton Nilsson
testcase 1:
in:
10 4
? 1 3
= 1 8
= 3 8
? 1 3

out:
no
yes

testcase 2:
in:
4 5
? 0 0
= 0 1
= 1 2
= 0 2
? 0 3

out:
yes
no

"""

def make_djss(amount: int) -> tuple[list[int], list[int]]:
    """
    Given the number of sets creates the data structures to allow union-find O(logn) time complexity.
    reference: https://en.wikipedia.org/wiki/Disjoint-set_data_structure#Making_new_sets
    """
    parent = list()
    rank = list()

    for i in range(amount + 1):
        parent.append(i)
        rank.append(0)

    return parent, rank

def djs_union(x: int, y: int, parent: list[int], rank: list[int]):
    """
    Given two

    algorithm: XXX
    time complexity: O(XXX)
    space complexity: O(XXX)
    where:
    - n is the XXX
    why:
    - XXX
    reference: https://en.wikipedia.org/wiki/Disjoint-set_data_structure#Union_by_rank

    parameters:
    - x: an element in set X
    - y: an element in set Y
    - parent: a list of parent indices for the trees in the forest of disjoint sets.
    - rank: a list of the rank of each element.
    returns:
    - Nothing but
    """
    
    x_parent = djs_find(x, parent)
    y_parent = djs_find(y, parent)

    if x_parent != y_parent:
        if rank[x_parent] < rank[y_parent]:
            y_parent, x_parent = x_parent, y_parent
        parent[y_parent] = x_parent
        if rank[x_parent] == rank[y_parent]:
            rank[x_parent] += 1

def djs_find(x: int, parent: list[int]) -> int:
    """
    XXX description XXX

    algorithm: XXX
    time complexity: O(XXX)
    space complexity: O(XXX)
    where:
    - n is the XXX
    why:
    - XXX
    reference: https://en.wikipedia.org/wiki/Disjoint-set_data_structure#Finding_set_representatives

    parameters:
    - x: an element in set X
    - y: an element in set Y
    - parent: a list of parent indices for the trees in the forest of disjoint sets.
    returns:
    - XXX
    """
    
    # If the element is the same as it's parent then x is the root of a tree.
    if x == parent[x]:
        return x
    
    # Reparent the element which will make future operations quicker.
    parent[x] = djs_find(parent[x], parent)
    return parent[x]

def djs_same(x: int, y: int, parent: list[int]):
    """
    Checks if two 
    """
    return djs_find(x, parent) == djs_find(y, parent)

if __name__ == "__main__":
    output = list()
    data = open(0, "r").read()
    number_of_elements = int(data.split("\n")[0].split(" ")[0])
    operations = [tuple(operation.split(" ")) for operation in data.split("\n")[1:-1]]

    parent, rank = make_djss(number_of_elements)

    for operation, a, b in operations:
        if operation == "?":
            if djs_same(int(a), int(b), parent):
                output.append("yes\n")
            else:
                output.append("no\n")
        elif operation == "=":
            djs_union(int(a), int(b), parent, rank)

    open(1, "w").write("".join(output))