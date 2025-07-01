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

from heapq import heappop, heappush

def funny_games(size: float, weapons: list[float]) -> bool:
    if min(weapons) * size <= 1:
        return True

    weapons.sort()
    queue = []
    wins = [[1.0, 1 / min(weapons)]]

    while wins[-1][1] <= size:
        if len(queue) == 0:
            for weapon in weapons:
                heappush(queue, (wins[-1][1] / weapon, wins[-1][1] / weapons[-1] / weapon))

        first, second = heappop(queue)

        if first <= wins[-1][1]:
            wins[-1][1] = max(wins[-1][1], second)
            continue

        for weapon in weapons:
            heappush(queue, (wins[-1][1] / weapon, min(first, wins[-1][1] / weapons[-1]) / weapon))

        if queue[0][0] < first:
            heappush(queue, (first, second))
            first, second = heappop(queue)
        elif queue[0][0] == first and queue[0][1] < second:
            heappush(queue, (first, second))
            first, second = heappop(queue)
            
        wins.append([first, second])

    for first, second in wins:
        if first < size and size <= second:
            return True

    return False

if __name__ == "__main__":
    for _ in range(int(input())):
        size, _, *weapons = map(float, input().split(" "))
        
        winning = funny_games(size, weapons)

        if winning:
            print("Nils")
        else:
            print("Mikael")

