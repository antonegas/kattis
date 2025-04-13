"""
author: Anton Nilsson
testcase 1:
in:
2
6 6
6 a
5 aa
4 a*a
3 aaaa
2 aaaaa
1 aaaaaa
6 6
6 b
5 aa
4 a*a
3 aaaa
2 aaaaa
1 aaaaaa

out:
aaaaaa
IMPOSSIBLE

testcase 2:
in:
2
6 6
6 a
5 *a
4 *a
3 *a
2 *a
1 aaaaaa
6 2
2 bbbbb
1 a*
6 2
2 bbbbb
1 *a

out:
aaaaaa
abbbbb
IMPOSSIBLE

testcase 3:
in:
1
4 4
4 *
3 *
2 *aa
1 aaaa

out:
aaaa

"""

def reconstruction(suffixes: list[tuple[str, int]], target: int):
    reconstructed_string = ["*"] * target

    for suffix, position in suffixes:
        offset = position

        for i in range(len(suffix)):
            if suffix[i] == "*":
                offset += target - position - len(suffix)
                continue

            if reconstructed_string[i + offset] == "*":
                reconstructed_string[i + offset] = suffix[i]
            elif reconstructed_string[i + offset] != suffix[i]:
                return "IMPOSSIBLE"
            
    if "*" in reconstructed_string:
        return "IMPOSSIBLE"
            
    return "".join(reconstructed_string)

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()[1:]

    index = 0

    while index < len(lines):
        l, s = map(int, lines[index].split(" "))

        index += 1

        suffixes = list()

        for _ in range(s):
            i, suffix = lines[index].split(" ")

            suffixes.append((suffix, int(i) - 1))

            index += 1

        output.append(reconstruction(suffixes, l))

    open(1, "w").write("\n".join(output))