"""
author: Anton Nilsson
testcase XXX:
in:
2
9
PUSH
DUP
ADD
PUSH
ADD
DUP
ADD
DUP
UNION
5
PUSH
PUSH
ADD
PUSH
INTERSECT

out:
0
0
1
0
1
1
2
2
2
***
0
0
1
0
0
***

"""

def push(stack):
    stack.append(set())

def dup(stack):
    stack.append(stack[-1])

def union(stack):
    s1 = stack.pop()
    s2 = stack.pop()
    stack.append(s1 | s2)

def intersect(stack):
    s1 = stack.pop()
    s2 = stack.pop()
    stack.append(s1 & s2)

def add(stack):
    s1 = stack.pop()
    s2 = stack.pop()
    s2.add(tuple(s1))
    stack.append(s2)

def setstack(operations):
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
    
    ops = {
        "PUSH": push,
        "DUP": dup,
        "UNION": union,
        "INTERSECT": intersect,
        "ADD": add
    }

    result = list()
    stack = list()

    for operation in operations:
        ops[operation](stack)
        result.append(len(stack[-1]))

    return result

def solve(operations):
    return setstack(operations)

if __name__ == "__main__":
    output = ""
    data = open(0, "r").read()
    operations = list(data.split("\n")[1:-1])

    i = 0
    while i < len(operations):
        n = int(operations[i])
        i += 1
        output += "\n".join(map(str, solve(operations[i:i+n]))) + "\n***\n"
        i += n

    open(1, "w").write(output)