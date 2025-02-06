"""
author: Anton Nilsson
testcase 1:
in:
3
2
1
3

out:
1
0
0

testcase 2:
in:
5
5
4
3
2
1

out:
4
3
2
1
0

testcase 3:
in:
7
5
4
3
7
1
2
6

out:
4
2
3
0
2
1
0

"""

def fenwick_sum(tree: list[int], index: int):
    result = 0

    while index > 0:
        result += tree[index]
        index -= index & -index

    return result

def fenwick_add(tree: list[int], index: int, delta: int):
    index += 1 # Wikipedia uses 1 as start index

    while index < len(tree):
        tree[index] += delta
        index += index & -index

def fenwick_index(tree: list[int], index: int):
    return fenwick_range(tree, index + 1, index)

def fenwick_range(tree: list[int], start: int, end: int):
    return  fenwick_sum(tree, end) - fenwick_sum(tree, start)

def fenwick_create(n: int):
    return [0] * (n + 1)

def algorithm(elements: list[int]) -> list[int]:
    tree = fenwick_create(len(elements))

    for i in range(len(elements)):
        fenwick_add(tree, i, 1)

    sorted_elements = sorted([(element, i) for i, element in enumerate(elements)])

    front = 0
    back = len(elements) - 1
    result = list()

    for i in range(len(sorted_elements)):
        if i % 2 == 0:
            _, index = sorted_elements[front]
            fenwick_add(tree, index, -1)
            result.append(fenwick_range(tree, 0, index + 1))
            front += 1
        else:
            _, index = sorted_elements[back]
            fenwick_add(tree, index, -1)
            result.append(fenwick_range(tree, index, len(sorted_elements)))
            back -= 1

    return result

def solve(elements: list[int]) -> list[int]:
    return algorithm(elements)

if __name__ == "__main__":
    output = ""
    data = open(0, "r").read()
    elements = list(map(int, data.split("\n")[1:-1]))

    output += "\n".join(map(str, solve(elements)))

    open(1, "w").write(output)