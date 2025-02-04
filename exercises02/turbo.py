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

def algorithm(elements: list[int]) -> list[int]:
    s = sorted([(element, i) for i, element in enumerate(elements)])
    from_front = True
    result = list()

    while len(elements) > 0:
        index = elements.index(min(elements)) if from_front else elements.index(max(elements))
        if from_front:
            result.append(index)
            del elements[index]
        else:
            result.append(len(elements) - 1 - index)
            del elements[index]
        from_front = not from_front

    return result


def solve(elements: list[int]) -> list[int]:
    return algorithm(elements)

if __name__ == "__main__":
    output = ""
    data = open(0, "r").read()
    elements = list(map(int, data.split("\n")[1:-1]))

    output += "\n".join(map(str, solve(elements)))

    open(1, "w").write(output)