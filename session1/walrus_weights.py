def walrus_weights(ws):
    mc = 1000
    v, ws = ws, ws

    max_values = [[0] * (mc + 1) for _ in range((len(ws) + 1))]
    
    for weight, value, item in zip(ws, v, range(1, len(ws) + 1)):
        for capacity in range(1, mc + 1):
            if weight > capacity:
                max_values[item][capacity] = max_values[item - 1][capacity]
            else:
                alternative1 = max_values[item - 1][capacity]
                alternative2 = max_values[item - 1][capacity - weight] + value
                max_values[item][capacity] = max(alternative1, alternative2)

    indices = list()

    capacity = mc

    for item in reversed(range(1, len(ws) + 1)):
        
        if max_values[item][capacity] > max_values[item - 1][capacity]:
            indices.append(item - 1)
            capacity -= ws[item - 1]

    inc = [ws[i] for i in indices]

    res = sum(inc)

    diff = (1000 - res) * 2

    for i, w in enumerate(ws):
        if i in indices:
            continue
        if w == diff:
            return res + w

    return res

if __name__ == "__main__":
    ws = [*map(int, open(0, "r").read().splitlines()[1:])]

    print(walrus_weights(ws))