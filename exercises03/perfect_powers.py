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
-25
8
-8
0

out:
31
3
1
3
3

"""

def pth_power(number: int) -> int:
    for b in range(2, int(abs(number)**0.5) + 1):
        x = abs(number)
        p = 0
        while x % b == 0:
            x = x // b
            p += 1
        if x != 1:
            continue
        if number > 0:
            return p
        if p % 2 == 1:
            return p

    return 1

if __name__ == "__main__":
    output = list()
    data = open(0, "r").read()
    numbers = map(int, data.split("\n")[:-2])

    for number in numbers:
        output.append(str(pth_power(number)))

    open(1, "w").write("\n".join(output))