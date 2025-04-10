"""
author: Anton Nilsson
testcase 1:
in:
ache
ape
check
peach
#
checkapeache|
animpeachableape|
ape
ape|
#

out:
3
2
2

"""

def get_prefix_function(string: str) -> list[int]:
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
    matches = list()

    prefix_function = get_prefix_function(f"{pattern}{chr(0)}{text}")

    for i in range(len(pattern) + 1, len(pattern) + len(text) + 1):
        if prefix_function[i] == len(pattern):
            matches.append(i - 2 * len(pattern))

    return matches

def messages_from_space(dictionary: list[str], message: str) -> int:
    intervals = list()

    for word in dictionary:
        for start in find_string(word, message):
            intervals.append((start, start + len(word)))

    count = 0
    index = 0

    for start, end in sorted(intervals, key=lambda x:x[1]):
        if start < index:
            continue

        count += 1
        index = end

    return count

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()

    index = 0

    dictionary = list()
    messages = list()


    while lines[index] != "#":
        dictionary.append(lines[index])

        index += 1

    index += 1
    
    message = ""

    while lines[index] != "#":
        line = lines[index]
        message += line

        if "|" in message:
            output.append(str(messages_from_space(dictionary, message[:-1])))
            message = ""

        index += 1

    open(1, "w").write("\n".join(output))