"""
author: Anton Nilsson
testcase 1:
in:
1 9 5

out:
1
5

testcase 2:
in:
1 100 10

out:
9
19

testcase 3:
in:
11111 99999 24

out:
5445
11499

"""

def smallest_integer(target: int, start: int, end: int) -> int:
    start_list = [*map(int, str(start).zfill(len(str(end))))]
    result = start_list[:]

    index = len(start_list) - 1
    while target - sum(result) > 0 and index >= 0:
        remaining = target + result[index] - sum(result)

        result[index] = min(remaining, 9)

        index -= 1

    return int("".join(map(str, result)))

def total_digit_sum(target: int, upper: int, digits: int) -> int:
    upper_list = [*map(int, str(upper).zfill(digits))]
    table = [[0] * 136 for _ in range(digits + 1)]

    table[0][0] = 1

    for digit in range(digits):
        for digit_sum in range(target):
            max_possible = sum(upper_list[:digit + 1])
            total = table[digit][digit_sum]
            if digit_sum == max_possible:
                for i in range(upper_list[digit + 1] + 1):
                    table[digit + 1][digit_sum + i] += total
            elif digit_sum < max_possible:
                for i in range(10):
                    table[digit + 1][digit_sum + i] += total

    return table[digits][target]

if __name__ == "__main__":
    output = list()
    data = open(0, "r").read()

    start, end, target = map(int, data.split())

    output.append(str(total_digit_sum(target, end, len(str(end))) - total_digit_sum(target, start, len(str(end)))))
    output.append(str(smallest_integer(target, start, end)))

    # print(smallest_integer(5, 1, 9))
    # print(smallest_integer(10, 1, 100))
    # print(smallest_integer(24, 11111, 99999))

    open(1, "w").write("\n".join(output))