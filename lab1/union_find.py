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

def create_disjoint_sets(amount: int) -> tuple[list[int], list[int]]:
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

def disjoint_set_union(x: int, y: int, parent: list[int], rank: list[int]):
    """
    Given two elements performs the union operation on the sets which contains the 
    two elements by updating the parent and rank lists.

    algorithm: After having performed the union operation both elements should be in the 
    same tree, in other words they should have the same root node. If the elements already 
    share root node nothing needs to be done. Otherwise the parent with the highest rank 
    becomes the root node of the union and the other parent becomes a child node. 
    This results in a lower depth of the resulting union.
    time complexity: O(a(n))
    where:
    - n is the total number of elements in all of the sets.
    - a is the inverse Ackermann function which grows extraordinarily slowly.
    why:
    - a(n) from the depth of the tree.
    reference: https://en.wikipedia.org/wiki/Disjoint-set_data_structure#Union_by_rank

    parameters:
    - x: an element in set X
    - y: an element in set Y
    - parent: a list of parent indices for the trees in the forest of disjoint sets.
    - rank: a list of the rank of each element.
    returns:
    - Nothing but will update both the parent and rank lists.
    """
    
    x_parent = disjoint_set_find(x, parent)
    y_parent = disjoint_set_find(y, parent)

    if x_parent != y_parent:
        if rank[x_parent] < rank[y_parent]:
            y_parent, x_parent = x_parent, y_parent
        parent[y_parent] = x_parent
        if rank[x_parent] == rank[y_parent]:
            rank[x_parent] += 1

def disjoint_set_find(x: int, parent: list[int]) -> int:
    """
    Given an element finds the root node of the tree which identifies the disjoint set.

    algorithm: The root a tree identifies a set. An element which has it self as its parent is a
    root node. If the current element is not the root of the tree go up the tree. Nodes which are
    not direct children to the root node are moved up in the tree by changing their parent to their
    parents parent. This will drastically decrease the speed at which the depth of the tree increases.
    time complexity: O(a(n))
    where:
    - n is the total number of elements in all of the sets.
    - a is the inverse Ackermann function which grows extraordinarily slowly.
    why:
    - a(n) from the depth of the tree.
    reference: https://en.wikipedia.org/wiki/Disjoint-set_data_structure#Finding_set_representatives

    parameters:
    - x: an element in set X.
    - parent: a list of parent indices for the trees in the forest of disjoint sets.
    returns:
    - The root node of the tree representing the disjoint set containing x.
    """
    
    # If the element is the same as it's parent then x is the root of a tree.
    if x == parent[x]:
        return x
    
    # Reparent the element which will make future operations quicker.
    parent[x] = disjoint_set_find(parent[x], parent)
    return parent[x]

def disjoint_set_same(x: int, y: int, parent: list[int]):
    """
    Checks if two elements are in the same set.
    """
    return disjoint_set_find(x, parent) == disjoint_set_find(y, parent)

if __name__ == "__main__":
    output = list()
    data = open(0, "r").read()
    number_of_elements = int(data.split("\n")[0].split(" ")[0])

    parent, rank = create_disjoint_sets(number_of_elements)

    for line in data.split("\n")[1:-1]:
        operation, a, b = line.split(" ")
        if operation == "?":
            if disjoint_set_same(int(a), int(b), parent):
                output.append("yes")
            else:
                output.append("no")
        elif operation == "=":
            disjoint_set_union(int(a), int(b), parent, rank)

    open(1, "w").write("\n".join(output))