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

def min_max(x: float, factor_weapons: list[float], depth: int, memo: dict[float, int]) -> int:
    if x in memo:
        return memo[x]
    
    if x <= 1:
        return depth % 2
    
    best = -1

    for factor_weapon in factor_weapons:
        winner = min_max(x * factor_weapon, factor_weapons, depth + 1, memo)
        if best < 0 or winner == depth % 2:
            best = winner

    memo[x] = best

    return best

if __name__ == "__main__":
    output = list()
    data = open(0, "r").read()
    
    for x, _, *factor_weapons in [map(float, x.split(" ")) for x in data.split("\n")[1:-1]]:
        print(["Mikael", "Nils"][min_max(x, factor_weapons, 0, dict())])

    open(1, "w").write("\n".join(output))