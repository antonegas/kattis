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

def create_lcp_array(string: str, suffix_array: list[int]) -> list[int]:
    """
    Given a string and a suffix array for that string creates a longest common prefix array for that string. 

    algorithm: The algorithm used is Kasai's algorithm. Assume that there are two adjacent suffixes in the 
    suffix array with a longest common prefix of k. If the first character of these suffixes is removed the 
    longest common prefix for the resulting suffixes will be at least k - 1. This is true for every suffix 
    except for the last suffix in the suffix array.
    time complexity: O(n)
    where:
    - n is the length of the string.
    why:
    - O(n) from increasing k atmost k times.
    - O(n) from looping over the suffixes of the string.
    reference: https://cp-algorithms.com/string/suffix-array.html#longest-common-prefix-of-two-substrings-without-additional-memory

    parameters:
    - string: the string to get the longest common prefix array for.
    - suffix_array: the suffix array for the given string.
    returns:
    - A longest common prefix array for the given string, where lcp[i] gives the longest common prefix between 
    the suffixes suffix_array[i] and suffix_array[i + 1].
    """
    
    rank = [0] * len(string)

    # Create a reverse lookup array for suffixes starting at an index of the string to their index in 
    # the suffix array.
    for i in range(len(string)):
        rank[suffix_array[i]] = i

    k = 0
    lcp = [0] * (len(string) - 1)

    for i in range(len(string)):
        # If the current i is the last item in the suffix array there is no next value so there is no 
        # longest common prefix.
        if rank[i] == len(string) - 1:
            k = 0
            continue

        # Check the prefix using the suffix following the suffix starting at i.
        j = suffix_array[rank[i] + 1]

        # As long as the two suffixes share characters at offset k the length of the longest common prefix 
        # between them can be increased. This can be repeated until the offset reaches the end of the string 
        # for one of the suffixes.
        while i + k < len(string) and j + k < len(string) and string[i + k] == string[j + k]:
            k += 1

        # The longest common prefix between i and j is the found k.
        lcp[rank[i]] = k

        # The length of the longest common prefix for i + 1 is at most one less than the current i.
        if k > 0:
            k -= 1

    return lcp

if __name__ == "__main__":
    string = open(0, "r").readlines()[1].strip()

    suffix_array = create_suffix_array(string)
    lcp_array = create_lcp_array(string, suffix_array)

    open(1, "w").write(str(max(lcp_array)))