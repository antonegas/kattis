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

from math import ceil, log
from functools import cache

@cache
def get_winner(x: float, factor_weapons: tuple[float], depth: int) -> int:
    player = depth % 2
    
    if x <= 1:
        return not player
    
    for factor_weapon in factor_weapons:
        winner = get_winner(x * factor_weapon, factor_weapons, depth + 1)
        if winner == player:
            return player
        
    return (player + 1) % 2

if __name__ == "__main__":
    output = list()
    data = open(0, "r").read()
    
    for x, _, *factor_weapons in [map(float, x.split(" ")) for x in data.split("\n")[1:-1]]:
        print(["Nils", "Mikael"][get_winner(x, tuple(factor_weapons), 0)])

    open(1, "w").write("\n".join(output))