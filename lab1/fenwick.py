"""
author: Anton Nilsson
testcase 1:
in:
10 4
+ 7 23
? 8
+ 3 17
? 8

out:
23
40

testcase 2:
in:
5 4
+ 0 -43
+ 4 1
? 0
? 5

out:
0
-42

"""

def fenwick_sum(tree: list[int], index: int):
    """
    Gives the prefix sum up to but not including an index in a given Fenwick tree.

    algorithm: A given level h of the Fenwick tree contains all indices with h bits set,
    eg 8 = 1000b is level 1 and 13 = 1101 is level 3. The value stored at a given index is
    the sum of a range. The range stored at an index is (index - lsb(index), index]. 
    When making a query given the sum for the range (index - lsb(index), index] can be accessed
    directly. Then remaining ranges can be retreived by decreasing the index by lsb(index) until
    the index is 0.
    time complexity: O(logn)
    where:
    - n is the length of the underlying list.
    why:
    - O(logn) from accessing atmost logn nodes in the tree.
    reference: https://en.wikipedia.org/wiki/Fenwick_tree#Pseudocode

    parameters:
    - tree: the Fenwick tree for which to calculate the prefix sum.
    - index: the first index after the last index included in the prefix sum.
    returns:
    - 
    """
    
    result = 0

    while index > 0:
        result += tree[index]
        index -= index & -index

    return result

def fenwick_add(tree: list[int], index: int, delta: int):
    """
    Adds a delta to a value at an index of a given Fenwick tree.

    algorithm: A given level h of the Fenwick tree contains all indices with h bits set,
    eg 8 = 1000b is level 1 and 13 = 1101 is level 3. The value stored at a given index is
    the sum of a range. The range stored at an index is (index - lsb(index), index]. 
    When a index is increased by delta every range which contains the index also needs to
    be updated. The ranges which contains the index can be found by increasing index by
    lsb(index) until the index is larger than the underlying list.
    time complexity: O(logn)
    where:
    - n is the length of the underlying list.
    why:
    - O(logn) from updating atmost logn nodes in the tree.
    reference: https://en.wikipedia.org/wiki/Fenwick_tree#Pseudocode

    parameters:
    - tree: the Fenwick tree which should be updated.
    - index: the index of the value which delta should be added to.
    - delta: the delta which should be added to the value at the given index.
    """
    
    index += 1 # Wikipedia uses 1 as start index

    while index < len(tree):
        tree[index] += delta
        index += index & -index

def fenwick_index(tree: list[int], index: int):
    """
    Gives the value of an index in a Fenwick tree.

    parameters:
    - tree: the Fenwick tree for which to get the value from.
    - index: the index for which to find the value.
    returns:
    - The value of a given index in the Fenwick tree.
    """
    return fenwick_range(tree, index + 1, index)

def fenwick_range(tree: list[int], start: int, end: int):
    """
    Gives the sum of numbers in a Fenwick tree from start (included) to end (excluded).

    parameters:
    - tree: the Fenwick tree for which to calculate the range sum.
    - start: the index of the start of the range to sum.
    - end: the index of the end of the range to sum.
    returns:
    - The sum of the numbers in the given range.
    """
    return fenwick_sum(tree, end) - fenwick_sum(tree, start)

def fenwick_create(n: int):
    """
    Creates a Fenwick tree of size n with all indices initialized to zero 
    (the index 0 will always be 0).

    paremeters:
    - n: the number of elements which should be in the Fenwick tree.
    returns:
    - A Fenwick tree of size n with all indexes set to zero.
    """
    return [0] * (n + 1)

if __name__ == "__main__":
    output = list()
    data = open(0, "r").read()

    n = int(data.split("\n")[0].split(" ")[0])
    tree = fenwick_create(n)

    for line in data.split("\n")[1:-1]:
        operation = line.split(" ")
        if operation[0] == "+":
            fenwick_add(tree, int(operation[1]), int(operation[2]))
        else:
            output.append(str(fenwick_sum(tree, int(operation[1]))))

    open(1, "w").write("\n".join(output))