"""
author: Anton Nilsson
testcase 1:
in:
popup
5 0 1 2 3 4
Popup
5 0 1 2 3 4
Suffixes are jolly fun, eh old chap?
7 35 3 18 33 26 6 2

out:
1 4 0 2 3
0 1 4 2 3
17 18 19 20 21 22 23

testcase 2:
in:
abcdefghijk
6 0 1 2 3 4 5
kjihgfedcba
6 0 1 2 3 4 5

out:
0 1 2 3 4 5
10 9 8 7 6 5

testcase 3:
in:
dabbb
5 0 1 2 3 4

out:
1 4 3 2 0

testcase 4:
in:
suffixes
8 0 1 2 3 4 5 6 7
algorithms
10 0 1 2 3 4 5 6 7 8 9
ababababa
9 0 1 2 3 4 5 6 7 8

out:
6 2 3 4 7 0 1 5
0 2 7 5 1 8 3 4 9 6

"""

def get_suffix(suffix_array: list[int], i: int) -> int:
    """
    Given a suffix array returns the i:th smallest suffix.
    """
    return suffix_array[i]

def create_suffix_array(string: str) -> list[int]:
    """
    Given a suffix string creates the suffix array for that string.

    algorithm: XXX
    time complexity: O(n*logn)
    where:
    - n is the number of characters in the string.
    why:
    - XXX
    reference: https://cp-algorithms.com/string/suffix-array.html#on-log-n-approach

    parameters:
    - string: 
    returns:
    - The suffix array for the given string.
    """

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

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()

    index = 0

    while index < len(lines):
        string = lines[index].strip()
        
        index += 1

        _, *queries = [*map(int, lines[index].split(" "))]

        index += 1

        suffix_array = create_suffix_array(string)
        output.append(" ".join(map(str, [get_suffix(suffix_array, q) for q in queries])))

    open(1, "w").write("\n".join(output))
