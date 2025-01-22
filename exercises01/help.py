"""
author: Anton Nilsson
time complexity: O(n + d * (p + q + min(p, q)))
where: 
- n is the number of words.
- d is the number of direct placeholder-word mappings.
- p, q is the number of placeholders (counting <a> twice on a line as two) on each line.
why:
- O(n) from looping over each item on both lines in the pair to generate the graph.
- O(d) from looping over each direct mapping to run dfs.
- O(p + q + min(p, q)) from dfs which has time complexity O()
assumptions:
- dictionary and set, access and insertion is O(1)
- list append, pop and access is O(1)
- zip([1,...,n]) is O(n)
testcase 1:
in:
10
how now brown <animal>
<foo> now <color> cow
who are you
<a> <b> <a>
<a> b
c <a>
to be or not to be
<foo> be <bar> not <foo> <baf>
<a>
<a>
<a> <a> b
<b> <c> <c>
<a> <a> <b>
<a> <a> c
<a> <a> i j
<b> <c> <b> <c>
a a a
a a
a
b
out:
how now brown cow
-
c b
to be or not to be
any
b b b
any any c
-
-
-
"""

from collections import defaultdict

def is_placeholder(word: str) -> bool:
    return word[0] == "<" and word[-1] == ">"

def get_numbered_placeholder(placeholder: str, number: int) -> str:
    return f"<{placeholder[1:-1]}{number}>"

def dfs(start: str, graph: dict[str, list[str]], mappings: dict[str, str]) -> bool:
    """
    Finds and adds [mappings] to the spaning tree using depth first search starting in 
    the placeholder [start] in the [graph].

    Return True if the spanning tree doesn't have any conflicts,
    False otherwise.
    """
    starting_word = mappings[start]
    stack: list[str] = list()
    visited: set[str] = set()
    stack.append(start)

    while stack:
        placeholder = stack.pop()
        if placeholder not in visited:
            visited.add(placeholder)
            for connected_placeholder in graph[placeholder]:
                # There is a conflict if there already is a mapping to different word
                connected_word = mappings[connected_placeholder]
                if connected_word != "" and connected_word != starting_word:
                    return False
                
                if connected_placeholder not in visited:
                    mappings[connected_placeholder] = starting_word
                    stack.append(connected_placeholder)

    return True

def solve(line1: list[str], line2: list[str]) -> list[str]:
    # If the patterns are different length, they can't have a matching phrase.
    if len(line1) != len(line2): 
        return ["-"]

    pairs = zip(line1, line2)
    partial_mappings: dict[str, str] = defaultdict(lambda: "")
    graph: dict[str, list[str]] = defaultdict(lambda: list())

    # There is 3 possible cases:
    # 1. Both items in a pair are placeholder.
    # 2. One item is a placeholder and the other is a word.
    # 3. Both items are words.

    # Case 1: both placeholders needs to be replaced by a word but we don't know which yet.
    # Case 2: if a pair contains a placeholder and a word. The placeholder has to be mapped to that word.
    # Case 3: words has to be the same.
    for item1, item2 in pairs:
        placeholder1 = get_numbered_placeholder(item1, 1)
        placeholder2 = get_numbered_placeholder(item2, 2)
        if is_placeholder(item1) and is_placeholder(item2): # Case 1
            graph[placeholder1].append(placeholder2)
            graph[placeholder2].append(placeholder1) 
        elif is_placeholder(item1): # Case 2
            current_mapping = partial_mappings[placeholder1]
            if current_mapping != "" and current_mapping != item2:
                return ["-"]
            partial_mappings[placeholder1] = item2
        elif is_placeholder(item2): # Case 2
            current_mapping = partial_mappings[placeholder2]
            if current_mapping != "" and current_mapping != item1:
                return ["-"]
            partial_mappings[placeholder2] = item1
        elif item1 != item2: # Case 3 failed
            return ["-"]
        
    # 

    # Idea:
    # - DFS is used to find spanning subtrees of the graph.
    # - The starting point of each search is a placeholder which was mapped to a word in the previous part.
    # - Any other placeholder in the subtree also has to be mapped to the same word as the starting point.
    # - If a placeholder has already been mapped to another word there is no match.
    # - If after this there is a placeholder without a mapping it can be mapped to any valid word (eg. "any").
    mappings = defaultdict(lambda: "", partial_mappings)

    for placeholder in partial_mappings:
        if not dfs(placeholder, graph, mappings):
            return ["-"]
        
    phrase: list[str] = list()

    # Generate a possible phrase using:
    # - The word for any word.
    # - A mapping for a mapped placeholder.
    # - The word "any" for any unmapped placeholder.
    for item in line1:
        if not is_placeholder(item):
            phrase.append(item)
        elif get_numbered_placeholder(item, 1) in mappings:
            phrase.append(mappings[get_numbered_placeholder(item, 1)])
        else:
            phrase.append("any")
    
    return phrase

if __name__ == "__main__":
    data = open(0, "r").read()
    lines = [list(line.split(" ")) for line in data.split("\n")[1:]]
    line_pairs = zip(lines[::2], lines[1::2])

    result = ""

    for line1, line2 in line_pairs:
        result += " ".join(solve(line1, line2)) + "\n"

    open(1, "w").write(result)
