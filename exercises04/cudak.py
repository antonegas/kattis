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

def cudak_smallest(target: int, start: int, end: int) -> int:
    result = [*map(int, str(start).zfill(len(str(end))))]
    index = len(result) - 1
    while target - sum(result) > 0 and index >= 0:
        remaining = target + result[index] - sum(result)

        result[index] = min(remaining, 9)

        index -= 1

    return int("".join(map(str, result)))

def cudak_total(target: int, upper: int) -> int:
    bounds = [*map(int, str(upper))]
    total = [[0] * (target + 1) for _ in range(len(bounds))]

    for j in range(min(bounds[0], target + 1)):
        total[0][j] = 1

    bound_sum = bounds[0]

    for i, bound in enumerate(bounds[1:]):
        for j in range(target + 1):
            if total[i][j] == 0 and j != bound_sum:
                continue
            
            for digit in range(min(10, target - j + 1)):
                total[i + 1][j + digit] += total[i][j]
                if digit < bound and j == bound_sum:
                    total[i + 1][j + digit] += 1

        bound_sum += bound

    if bound_sum == target:
        total[-1][-1] += 1
    return total[-1][-1]

if __name__ == "__main__":
    start, end, target = map(int, input().split(" "))

    print(cudak_total(target, end) - cudak_total(target, start - 1))
    print(cudak_smallest(target, start, end))