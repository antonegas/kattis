"""
author: Anton Nilsson
testcase 1:
in:
5

out:
12

testcase 2:
in:
14

out:
912

testcase 3:
in:
19

out:
832

testcase 4:
in:
20

out:
664

"""

def three_digits(number: int) -> str:
    result = 1

    for i in range(2, number + 1):
        result = result * i
        while result % 10 == 0:
            result = result // 10

        result = result % 1_000_000_000_000

    return str(result)[-3:]

if __name__ == "__main__":
    output = list()
    data = open(0, "r").read()

    output.append(three_digits(int(data.split("\n")[0])))

    open(1, "w").write("\n".join(output))