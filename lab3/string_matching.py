"""
author: Anton Nilsson
testcase 1:
in:
p
Popup
helo
Hello there!
peek a boo
you speek a bootiful language
anas
bananananaspaj

out:
2 4

5
7

"""

def get_prefix_function(string: str) -> list[int]:
    """
    Given a string calculates the prefix function for the string.
    """

    pi = [0] * len(string)

    for i in range(1, len(string)):
        j = pi[i - 1]
        while j > 0 and string[i] != string[j]:
            j = pi[j - 1]
        if string[i] == string[j]:
            j += 1
        pi[i] = j

    return pi

def find_string(pattern: str, text: str):
    """
    Given a pattern and a text finds all the occurences of the pattern in the text.

    algorithm: The algorithm used is Knuth-Morris-Pratt. It generates a prefix function pi 
    for a given string. Indexing pi[i] gives how much of the string prefix is found again 
    going back from that position. This is done efficiently by using the fact that 
    pi[i] + 1 >= pi[i + 1]. If string[i + 1] != string[pi[i]] then pi[i] + 1 > pi[i + 1] 
    and shorter prefixes has to be checked. Using the value of pi[pi[i]] the total number 
    of backtracking that needs to be checked is at most n for the entire string. 
    
    To find all occurences of a pattern in a text the prefix function is generated for the string: 
    pattern + special character + text. This special character shouldn't appear in either the 
    pattern or text string, this will cause pattern to be the longest prefix. All occurences of 
    the pattern in the text will then have p[i] equal to the length of the pattern.
    time complexity: O(n+m)
    where:
    - n is the length of the pattern.
    - m is the length of the text.
    why:
    - O(n+m) from generating the prefix function.
    - O(m) from looping over the pattern part of the generated prefix function.
    - O(n+m+m) = O(n+m)
    reference: https://cp-algorithms.com/string/prefix-function.html#implementation

    parameters:
    - pattern: the pattern string to find in the text string.
    - text: the text string to find the pattern in.
    returns:
    - The index in the text string where the occurence of the pattern starts.
    """

    matches = list()

    prefix_function = get_prefix_function(f"{pattern}{chr(0)}{text}")

    for i in range(len(pattern) + 1, len(pattern) + len(text) + 1):
        if prefix_function[i] == len(pattern):
            matches.append(i - 2 * len(pattern))

    return matches

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()

    for pattern, text in zip(lines[::2], lines[1::2]):
        output.append(" ".join(map(str, find_string(pattern, text))))

    open(1, "w").write("\n".join(output))