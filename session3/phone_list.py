"""
author: Anton Nilsson
testcase 1:
in:
2
3
911
97625999
91125426
5
113
12340
123440
12345
98346

out:
NO
YES

"""

from itertools import combinations

def get_prefix_function(string: str) -> list[int]:
    pi = [0] * len(string)

    for i in range(1, len(string)):
        j = pi[i - 1]
        while j > 0 and string[i] != string[j]:
            j = pi[j - 1]
        if string[i] == string[j]:
            j += 1
        pi[i] = j

    return pi

if __name__ == "__main__":
    for _ in range(int(input())):
        numbers = [input() for _ in range(int(input()))]

        yes = True

        for number1, number2 in combinations(numbers, 2):
            if len(number2) >= len(number1):
                prefix_function = get_prefix_function(f"{number1}{chr(0)}{number2}")
                if prefix_function[len(number1) * 2] == len(number1):
                    yes = False
                    break
            if len(number1) >= len(number2):
                prefix_function = get_prefix_function(f"{number2}{chr(0)}{number1}")
                if prefix_function[len(number2) * 2] == len(number2):
                    yes = False
                    break

        if yes:
            print("YES")
        else:
            print("NO")