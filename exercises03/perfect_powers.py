"""
author: Anton Nilsson
testcase 1:
in:
17
1073741824
25
0

out:
1
30
2

testcase 2:
in:
2147483648
-27
8
0

out:
31
3
3

"""

from math import isclose, pow

def pth_power(number: int) -> int:
    jumps = 1
    if number < 0:
        jumps = 2
    
    for power in reversed(range(1, 32, jumps)):
        root = pow(abs(number), 1/power)
        if not isclose(root, 1) and isclose(root, round(root)):
            return power
    
    return 1

if __name__ == "__main__":
    output = list()
    data = open(0, "r").read()
    numbers = map(int, data.split("\n")[:-2])

    for number in numbers:
        output.append(str(pth_power(number)))

    open(1, "w").write("\n".join(output))