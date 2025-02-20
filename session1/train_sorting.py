"""
author: Anton Nilsson
testcase 1:
in:
3
1
2
3

out:
3

"""

def lis(sequence: list[int]) -> list[int]:
    fixed_sequence = sequence + [float("inf")]
    last_elements = [-1]

    previous = list()
    longest_length = 0

    for i, value in enumerate(fixed_sequence[:-1]):
        low = 0
        high = longest_length + 1
        while low < high:
            middle = (high + low) // 2
            if fixed_sequence[last_elements[middle]] >= value:
                high = middle
            else:
                low = middle + 1

        previous.append(last_elements[low - 1])

        if low > longest_length:
            last_elements.append(i)
            longest_length = low
        else:
            last_elements[low] = i

    longest_sequence = list()
    current_element = last_elements[longest_length]

    for _ in range(longest_length + 1):
        longest_sequence.append(current_element)
        current_element = previous[current_element]

    return list(reversed(longest_sequence))

# def train_sorting(sq: list[int]):

#     up = lis(sq)

#     rsq = [v for i, v in enumerate(sq) if i not in up and v < up[0]]

#     down = lis(sq)

#     return lis([*map(lambda x: -x, sq)])

def train_sorting(sq: list[int]):
    res = 0
    
    for i, c in enumerate(sq):
        lo = c
        hi = c
        l = 1
        for v in sq[i+1:]:
            if lo > v:
                lo = v
                l += 1
            elif hi < v:
                hi = v
                l += 1

        if l > res:
            res = l

    return res

if __name__ == "__main__":
    sq = [*map(int, open(0, "r").read().splitlines()[1:])]

    print(train_sorting(sq))