"""
author: Anton Nilsson
testcase 1:
in:
2
3
0.0 0.0
0.0 1.0
1.0 0.0
10
30.0 38.0
43.0 72.0
47.0 46.0
49.0 69.0
52.0 42.0
58.0 17.0
73.0 7.0
84.0 81.0
86.0 75.0
93.0 50.0

out:
2.000
168.01015709273446

"""

def prims(bridge_points: list[tuple[float, float]]) -> float:
    total = 0.0
    
    x0, y0 = bridge_points[0]
    costs = [((x - x0)**2 + (y - y0)**2)**0.5 for x, y in bridge_points]

    for _ in range(len(bridge_points) - 1):
        best_index = -1
        best_cost = float("inf")

        for cost, index in zip(costs, range(len(costs))):
            if cost == 0.0:
                continue
            if cost > best_cost:
                continue

            best_index = index
            best_cost = cost

        total += best_cost

        xb, yb = bridge_points[best_index]

        for i, bridge_point in enumerate(bridge_points):
            x, y = bridge_point
            cost = ((x - xb)**2 + (y - yb)**2)**0.5

            if cost < costs[i]:
                costs[i] = cost

    return total

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()[1:]

    index = 0

    while index < len(lines):
        m = int(lines[index])
        index += 1

        bridge_points = list()

        for _ in range(m):
            bridge_points.append(tuple(map(float, lines[index].split(" "))))
            index += 1

        output.append(str(prims(bridge_points)))

    open(1, "w").write("\n".join(output))