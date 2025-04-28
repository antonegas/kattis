"""
author: Anton Nilsson
testcase 1:
in:
5 2

out:
3

testcase 2:
in:
2 4

out:
1

testcase 3:
in:
8 3

out:
5

testcase 4:
in:
4 2

out:
3

testcase 5:
in:
5 1

out:
2

"""

if __name__ == "__main__":
    n, k = map(int, input().split())

    first = k
    last = ((n - 1) // k) * k

    print(min(n - 1, first - last + n))

    # if k != 1:

        # print("===", first, last)
        
    # else:
    #     print(2)