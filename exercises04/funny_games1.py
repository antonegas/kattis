"""
author: Anton Nilsson
testcase 1:
in:
4
6 2 0.25 0.5
10 2 0.25 0.5
29.29 4 0.3 0.7 0.43 0.54
29.30 4 0.3 0.7 0.43 0.54

out:
Mikael
Nils
Nils
Mikael

"""

from math import log, ceil
from functools import reduce

def get_winner(x: float, factor_weapons: list[float]) -> bool:
    sorted_weapons = sorted(factor_weapons)
    nils = [0] * len(factor_weapons)
    mikeal = [0] * len(factor_weapons)
    combined = [0] * len(factor_weapons)

    turns = ceil(log(1 / x) / log(sorted_weapons[0]))

    nils[0] = (turns + 1) // 2
    mikeal[0] = turns // 2
    combined[0] = turns
    players = [nils, mikeal]

    while nils[-1] != (turns + 1) // 2 and mikeal[-1] != turns // 2:
        losing = turns % 2
        player = players[losing]

        for i, n in enumerate(player):
            if n != 0:
                player[i] -= 1
                player[i + 1] += 1
                combined[i] -= 1
                combined[i + 1] += 1
                break

        size = x * reduce(lambda a, b: a * b, [f**n for n, f in zip(combined, sorted_weapons)])

        if size > 1:
            player[0] += 1
            combined[0] += 1
            turns += 1

    print(nils)
    print(mikeal)
    print(x * reduce(lambda a, b: a * b, [f**n for n, f in zip(combined, sorted_weapons)]))

    return turns % 2 == 1

if __name__ == "__main__":
    output = list()
    data = open(0, "r").read()
    
    for x, _, *factor_weapons in [map(float, x.split(" ")) for x in data.split("\n")[1:-1]]:
        print("Nils" if get_winner(x, factor_weapons) else "Mikael")
        # output.append("Nils" if get_winner(x, factor_weapons) else "Mikael")

    open(1, "w").write("\n".join(output))