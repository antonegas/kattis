"""
author: Anton Nilsson
testcase 1:
in:
3
abcdefg
bcdefgh
cdefghi
3
xxx
yyy
zzz
0

out:
bcdefg
cdefgh

?

"""

from bisect import bisect

def create_suffix_array(string: str) -> list[int]:
    ALPHABET = 256

    string += chr(0)
    
    permutation = [0] * len(string)
    equivalance_class = [0] * len(string)
    count = [0] * ALPHABET

    for character in string:
        count[ord(character)] += 1

    for i in range(1, ALPHABET):
        count[i] += count[i - 1]

    for i, character in enumerate(string):
        count[ord(character)] -= 1
        permutation[count[ord(character)]] = i

    equivalance_class[permutation[0]] = 0
    classes = 1

    for i in range(1, len(string)):
        if string[permutation[i]] != string[permutation[i - 1]]:
            classes += 1
        equivalance_class[permutation[i]] = classes - 1

    new_permutation = [0] * len(string)
    new_class = [0] * len(string)

    h = 0

    while (1 << h) < len(string):
        for i in range(len(string)):
            new_permutation[i] = permutation[i] - (1 << h)
            if new_permutation[i] < 0:
                new_permutation[i] += len(string)

        count = [0] * classes

        for i in range(len(string)):
            count[equivalance_class[new_permutation[i]]] += 1

        for i in range(1, classes):
            count[i] += count[i - 1]

        for i in reversed(range(len(string))):
            count[equivalance_class[new_permutation[i]]] -= 1
            permutation[count[equivalance_class[new_permutation[i]]]] = new_permutation[i]

        new_class[permutation[0]] = 0
        classes = 1

        for i in range(1, len(string)):
            current = [
                equivalance_class[permutation[i]], 
                equivalance_class[(permutation[i] + (1 << h)) % len(string)]
                ]
            previous = [
                equivalance_class[permutation[i - 1]], 
                equivalance_class[(permutation[i - 1] + (1 << h)) % len(string)]
                ]

            if current != previous:
                classes += 1
            
            new_class[permutation[i]] = classes - 1

        equivalance_class, new_class = new_class, equivalance_class

        h += 1

    return permutation[1:]

def create_lcp_array(string: str, suffix_array: list[int]) -> list[int]:
    rank = [0] * len(string)

    for i in range(len(string)):
        rank[suffix_array[i]] = i

    k = 0
    lcp = [0] * (len(string) - 1)

    for i in range(len(string)):
        if rank[i] == len(string) - 1:
            k = 0
            continue

        j = suffix_array[rank[i] + 1]

        while i + k < len(string) and j + k < len(string) and string[i + k] == string[j + k]:
            k += 1

        lcp[rank[i]] = k

        if k > 0:
            k -= 1

    return lcp

def string_index(start_indices: list[int], index: int):
    return bisect(start_indices, index) - 1

def life_forms(dna_sequences: list[str]) -> list[str]:
    if len(dna_sequences) == 1:
        return dna_sequences

    concatenated = "".join(dna_sequences)
    half = len(dna_sequences) // 2 + 1
    start_indices = [0]

    for dna_sequence in dna_sequences[1:]:
        start_indices.append(start_indices[-1] + len(dna_sequence))
    
    suffix_array = create_suffix_array(concatenated)
    lcp_array = create_lcp_array(concatenated, suffix_array)

    sequence_count = [0] * len(dna_sequences)
    sequence_count[string_index(start_indices, suffix_array[0])] = 1
    count = 1

    longest = 1
    longest_indices = []

    lower = 0

    for upper in range(1, len(concatenated)):
        upper_index = string_index(start_indices, suffix_array[upper])

        if sequence_count[upper_index] == 0:
            count += 1

        sequence_count[upper_index] += 1

        while count == half:
            value = min(lcp_array[lower:upper], default=0)

            if value == longest:
                longest_indices.append(suffix_array[lower])
            elif value > longest:
                longest = value
                longest_indices = [suffix_array[lower]]

            lower_index = string_index(start_indices, suffix_array[lower])

            sequence_count[lower_index] -= 1

            if sequence_count[lower_index] == 0:
                count -= 1

            lower += 1

    result = set()

    for i in longest_indices:
        result.add(concatenated[i:i + longest])

    return sorted(result)

if __name__ == "__main__":
    from sys import stdin
    input=stdin.readline

    output = list()

    n = int(input())

    while n:
        dna_sequences = [input().strip() for _ in range(n)]

        result = life_forms(dna_sequences)

        if len(result) == 0:
            output.append("?")
        else:
            output.extend(result)

        output.append("")

        n = int(input())

    open(1, "w").write("\n".join(output))