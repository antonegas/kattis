"""
author: Anton Nilsson
testcase 1:
in:
11
sabcabcfabc

out:
3

testcase 2:
in:
18
trutrutiktiktappop

out:
4

testcase 3:
in:
6
abcdef

out:
0

"""

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

def create_lcp(string: str, suffix_array: list[int]) -> list[int]:
    """
    Given a string and a suffix array for that string creates a longest common prefix array for that string. 

    algorithm: XXX
    time complexity: O(n)
    where:
    - n is the length of the string.
    why:
    - XXX
    reference: https://cp-algorithms.com/string/suffix-array.html#longest-common-prefix-of-two-substrings-without-additional-memory

    parameters:
    - XXX
    returns:
    - XXX
    """
    
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


if __name__ == "__main__":
    string = open(0, "r").read().strip()

    suffix_array = create_suffix_array(string)
    lcp_array = create_lcp(string, suffix_array)

    open(1, "w").write(str(max(lcp_array)))