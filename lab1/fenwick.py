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

def fenwickSum(tree: list[int], index: int):
    """
    XXX description XXX

    algorithm: XXX
    time complexity: O(XXX)
    space complexity: O(XXX)
    where:
    - n is the XXX
    why:
    - XXX
    reference: XXX

    parameters:
    - XXX
    returns:
    - XXX
    """
    
    result = 0

    while index > 0:
        result += tree[index]
        index -= index & -index

    return result

def fenwickAdd(tree: list[int], index: int, delta: int):
    """
    XXX description XXX

    algorithm: XXX
    time complexity: O(XXX)
    space complexity: O(XXX)
    where:
    - n is the XXX
    why:
    - XXX
    reference: XXX

    parameters:
    - XXX
    returns:
    - XXX
    """
    
    index += 1

    while index < len(tree):
        tree[index] += delta
        index += index & -index

def fenwickIndex(tree: list[int], index: int):
    return fenwickSum(tree, index + 1) - fenwickSum(tree, index)

def fenwickCreate(n: int):
    return [0] * (n + 1)

if __name__ == "__main__":
    output = list()
    data = open(0, "r").read()

    n = int(data.split("\n")[0].split(" ")[0])
    tree = fenwickCreate(n)

    for line in data.split("\n")[1:-1]:
        operation = line.split(" ")
        if operation[0] == "+":
            fenwickAdd(tree, int(operation[1]), int(operation[2]))
        else:
            output.append(str(fenwickSum(tree, int(operation[1]))))

    open(1, "w").write("\n".join(output))