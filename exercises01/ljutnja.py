"""
author: Anton Nilsson
testcase 1:
in:
5 3
1
3
2

out:
1

testcase 2:
in:
10 4
4
5
2
3

out:
4

testcase 3:
in:
6 3
2
2
2

out:
0

"""

def binary_search(candies: int, requests: list[int]) -> int:
    low = 0
    high = 2_000_000_000
    
    sorted_requests = sorted(requests)

    while low < high:
        middle = (low + high) // 2
        used_candies = sum(map(lambda x: max(0, x - middle), sorted_requests))

        if used_candies > candies:
            low = middle + 1
        else:
            high = middle

    maximum_missing = low
    remaining_candies = candies
    missing_candies = sorted_requests

    for r, request in enumerate(missing_candies):
        missing_candy = min(request, maximum_missing)
        used_candies = request - missing_candy
        
        remaining_candies -= used_candies
        missing_candies[r] = missing_candy

    for r in reversed(range(len(missing_candies))):
        if remaining_candies == 0:
            break
        remaining_candies -= 1
        missing_candies[r] -= 1

    return sum(map(lambda x: x**2, missing_candies))

def solve(candies: int, requests: list[int]) -> int:
    return binary_search(candies, requests)

if __name__ == "__main__":
    output = ""
    data = open(0, "r").read()
    candies = int(data.split("\n")[0].split(" ")[0])
    requests = list(map(int, data.split("\n")[1:-1]))

    output += f"{solve(candies, requests)}\n"

    open(1, "w").write(output)