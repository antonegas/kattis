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

    algorithm: To create the suffix array, cyclic shifts of the string + a delimiter, is sorted. 
    The delimiter is chosen such that its value is less than all other values in the string. 
    This choice ensures that the sorting of the cyclic shifts will be equivalent to sorting the 
    suffixes of the string. The sorting of cyclic shift is done by iteratively performing counting 
    sort on substrings of length 2^k based on substrings of length 2^(k-1), which were sorted in 
    the previous iteration.
    time complexity: O(n*logn)
    where:
    - n is the number of characters in the string.
    why:
    - O(n) from running counting sort on substrings of length 2^k.
    - O(logn) from there being logn + 1 iterations of the counting sort.
    reference: https://cp-algorithms.com/string/suffix-array.html#on-log-n-approach

    parameters:
    - string: the string for which to create a suffix array.
    returns:
    - The suffix array for the given string.
    """

    ALPHABET = 256 # The alphabet used is assumed to be ASCII.

    # It is assumed that the string does not contain a NULL character and since
    # NULL has ASCII value 0 it will be smaller than any other character in the string.
    string += chr(0)
    
    # Use counting sort to sort cyclic substrings of length one. The permutation list will be the 
    # start indices of the substrings in sorted order. The equivalance class list will keep track 
    # of the equivalance classes of the substrings. Two substrings has the same equivalance class 
    # if they are equal. If a substring x has a lower value than a substring y, the equivalance 
    # class x belongs to will also be lower than that of y.
    permutation = [0] * len(string)
    equivalance_class = [0] * len(string)
    count = [0] * ALPHABET

    # Count occurences of characters in the string.
    for character in string:
        count[ord(character)] += 1

    # To generate a correct permutation list update the count list such that an index i gives the
    # number of characters with a ASCII value lower or equal to i.
    for i in range(1, ALPHABET):
        count[i] += count[i - 1]

    # Generate the sorted permutation list for the first iteration by using the value of the count 
    # list for the current characters ASCII value. Since the count list was updated to give the 
    # number of characters less than a given ASCII value, it can be used to give a correct index 
    # in the permutation list. This is done by first decreasing the count value for the current 
    # character in the string and then using that as the index in the permutation list.
    for i, character in enumerate(string):
        count[ord(character)] -= 1
        permutation[count[ord(character)]] = i

    # Place the lowest valued substring into equivalence class zero.
    equivalance_class[permutation[0]] = 0
    classes = 1

    # Place all other substrings into equivalence classes by using the sorted permutation list.
    # Since the permutation list is sorted, if two subsesubsequent substrings given by the permutation 
    # list are not equal then the latter one will be in a higher equivalance class.
    for i in range(1, len(string)):
        if string[permutation[i]] != string[permutation[i - 1]]:
            classes += 1
        equivalance_class[permutation[i]] = classes - 1

    # Counting sort can then be used similarly to sort substrings of length 2^k. Two substrings of 
    # length 2^(k-1) can be used to form a substring of length 2^k. Information about the substrings 
    # of length 2^(k-1) can be used to sort the substrings of length 2^k.
    new_permutation = [0] * len(string)
    new_class = [0] * len(string)

    h = 0 # h = k - 1

    while (1 << h) < len(string):
        # Use the permutation list from previous iteration to sort the (a, b) pairs based on b. 
        # In this case a and b are the two substrings of length 2^(k-1) which makes up the 
        # substring of length 2^k.
        for i in range(len(string)):
            # The start index of the 2^k length substring is equal to the b substrings start 
            # index minus 2^(k-1)
            new_permutation[i] = permutation[i] - (1 << h)

            if new_permutation[i] < 0:
                new_permutation[i] += len(string)

        # The new count list will have length equal to the number of equivalance classes.
        count = [0] * classes

        # Count to number of occurences of substrings in each equivalance class.
        for i in range(len(string)):
            count[equivalance_class[new_permutation[i]]] += 1

        # To generate a correct permutation list update the count list such that an index i gives the
        # number of substrings of a lower or equal equivalance class as i.
        for i in range(1, classes):
            count[i] += count[i - 1]

        # By performing a stable sort based on a in (a, b) on the substrings already sorted by b the 
        # entire substring will be correctly sorted. This be done similarly to the substrings of 
        # length one, using counting sort. Since the index retrieved from the count list will have 
        # give higher indices first, the permutation sorted based on b is iterated through backwards, 
        # to ensure that the sort is stable.
        for i in reversed(range(len(string))):
            count[equivalance_class[new_permutation[i]]] -= 1
            permutation[count[equivalance_class[new_permutation[i]]]] = new_permutation[i]

        # Place the lowest valued substring into equivalence class zero.
        new_class[permutation[0]] = 0
        classes = 1

        # Place all other substrings into equivalence classes by using the sorted permutation list.
        # The updated permutation list and equivalance classes for the substrings of length 2^(k-1) 
        # can be used to determine equivalance classes for substrings of length 2^k.
        for i in range(1, len(string)):
            current = [
                equivalance_class[permutation[i]], 
                equivalance_class[(permutation[i] + (1 << h)) % len(string)]
                ]
            previous = [
                equivalance_class[permutation[i - 1]], 
                equivalance_class[(permutation[i - 1] + (1 << h)) % len(string)]
                ]

            # If the equivalance classes of the substrings of length 2^(k-1) making up the current 
            # and previous substrings of length 2^k are different then the substrings of length 2^k 
            # are in different equivalance classes.
            if current != previous:
                classes += 1
            
            new_class[permutation[i]] = classes - 1

        equivalance_class, new_class = new_class, equivalance_class

        h += 1

    # Since the character appended to the end of the string is smaller than all other characters 
    # in the string it can be removed by ignoring the first value of the permutation list.
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
