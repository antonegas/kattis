"""
author: Anton Nilsson
testcase 1:
in:
1
2
3
4
5
6
8
98

out:
1
2
5
9
8
6
11
002

"""

def base7(number: int) -> list[int]:
    if number == 0:
        return [0]
    
    result = list()

    while number != 0:
        result.append(number % 7)
        number = number // 7

    return result
    
def ignore_garbage(number: int) -> list[int]:
    valid_digits = [0, 1, 2, 5, 9, 8, 6]
    return [*map(lambda i: valid_digits[i], base7(number))]

if __name__ == "__main__":
    output = list()
    data = open(0, "r").read()
    numbers = map(int, data.split("\n")[:-1])

    for number in numbers:
        output.append("".join(map(str, ignore_garbage(number))))

    open(1, "w").write("\n".join(output))