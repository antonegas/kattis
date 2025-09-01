"""
author: Anton Nilsson
testcase 1:
in:
2
5 2
1 1
2 2
3 3
6 6
7 8
3 2
3 3
3 6
6 9

out:
Case #1: 2
Case #2: 3

testcase 2:
in:
1
15 4
3709 6011
3543 8617
6478 5882
2173 2205
2301 5039
2302 5952
2097 17
2362 17
4135 8773
4401 2207
2694 7976
1179 2463
3795 8706
769 6063
3579 4557

out:
Case #1: 2891

"""

def dfs(points: list[tuple[int, int]], size: int, remaining: int) -> bool:
    if len(points) == 0:
        return True
    if remaining == 0:
        return False
    
    left_x, first_y = points[0]
    possible_points = list()
    other_points = list()

    for x, y in points:
        if x > left_x + size:
            other_points.append((x, y))
        elif first_y + size >= y >= first_y - size:
            possible_points.append((x, y))
        else:
            other_points.append((x, y))
    
    possible_points.sort(key=lambda x: x[1], reverse=True)

    first = 0
    
    for last in range(len(possible_points)):
        if possible_points[first][1] - size > possible_points[last][1] and \
            dfs(sorted(possible_points[:first] + possible_points[last:]) + other_points, size, remaining - 1):
            return True
            
        while possible_points[first][1] - size > possible_points[last][1]:
            first += 1

    return dfs(sorted(possible_points[:first]) + other_points, size, remaining - 1)

def binary_search(points: list[tuple[int, int]], max_fields: int, max_size: int = 64_000) -> int:
    low = 0
    high = max_size

    while low < high:
        middle = (low + high) // 2

        if not dfs(points, middle, max_fields):
            low = middle + 1
        else:
            high = middle

    return low

def square_fields(points: list[tuple[int, int]], max_fields: int) -> int:
    sorted_points = sorted(points)

    return binary_search(sorted_points, max_fields)

if __name__ == "__main__":
    for i in range(1, int(input()) + 1):
        points = list()

        n, k = map(int, input().split(" "))

        for _ in range(n):
            x, y = map(int, input().split(" "))
            points.append((x, y))

        print(f"Case #{i}:", square_fields(points, k))