"""
author: Anton Nilsson
testcase XXX:
in:
1
6 2
1 3 2 6 2 4

out:
12

"""

def algorithm(m, a):
    res = 0

    before = 0
    after = 0

    l = 0
    added_m = False

    for v in a:
        if v < m:
            l = before + after
            before = 0
            after = 0
        after += v
        l = before + after

        if v == m:
            before = after
            after = 0
            added_m = True
            if added_m:
                l -= v

        if l > res:
            res = l

    if before + after > res:
        return before + after

    return res

if __name__ == "__main__":
    data = open(0, "r").read().splitlines()[1:]

    for nm, a in zip(data[::2], data[1::2]):
        m = int(nm.split(" ")[1])
        a = [*map(int, a.split(" "))]
        print(algorithm(m, a))