"""
author: Anton Nilsson
testcase 1:
in:
5
Ron
George
Bill
Fred
Jenny
3
Fred Jenny
Bill Ron
George Jenny
2
Alice
Bob
1
Alice Bob

out:
Bill Fred George Ron Jenny
You all need therapy.

"""

def class_picture(names: list[str], can_stand: dict[str, set], possible: set[str], remaining: set[str]) -> list[str]:
    if len(remaining) == 0:
        return list()
    if len(possible) == 1:
        return list()

    for name in names:
        if name not in possible:
            continue
        if name not in remaining:
            continue

        remaining.remove(name)

        order = class_picture(names, can_stand, can_stand[name], remaining)

        if len(order) == len(remaining):
            remaining.add(name)
            return [name] + order

        remaining.add(name)

    return list()

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()

    index = 0

    while index < len(lines):
        n = int(lines[index])

        index += 1

        names = list()

        for _ in range(n):
            name = lines[index]
            index += 1

            names.append(name)

        names = sorted(names)

        can_stand = {name: set(names) for name in names}

        m = int(lines[index])

        index += 1

        for _ in range(m):
            name1, name2 = lines[index].split()
            index += 1

            can_stand[name1].remove(name2)
            can_stand[name2].remove(name1)

        order = class_picture(names, can_stand, set(names), set(names))

        if not order:
            print("You all need therapy.")
        else:
            print(" ".join(order))