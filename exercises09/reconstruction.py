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

def pad_suffix(suffix: str, length: int, target: int):
    padded_suffix = suffix

    if "*" in suffix:
        part1, part2 = suffix.split("*")
        padded_suffix = part1 + "*" * (length + 1 - len(suffix)) + part2
    
    return padded_suffix.rjust(target, "*")

def reconstruction(suffixes: list[tuple[str, int]], target: int):
    padded_suffixes = list()

    for suffix, length in suffixes:
        padded_suffix = pad_suffix(suffix, length, target)
        padded_suffixes.append(padded_suffix)

    reconstructed_string = ["*"] * target

    for padded_suffix in padded_suffixes:
        for i in range(target):
            if padded_suffix[i] == "*":
                continue

            if reconstructed_string[i] == "*":
                reconstructed_string[i] = padded_suffix[i]
            elif reconstructed_string[i] != padded_suffix[i]:
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

            suffixes.append((suffix, l + 1 - int(i)))

            index += 1

        output.append(reconstruction(suffixes, l))

    open(1, "w").write("\n".join(output))