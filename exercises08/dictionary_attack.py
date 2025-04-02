"""
author: Anton Nilsson
testcase 1:
in:
5
book
apple
secret
December
vertigo
book
b00k
alppe
a1ppe
secret
esrcte
erscte
vreitg0
arithmetic
D3c3m63r
d3c3mb3r
ap1p3

out:
erscte
arithmetic
D3c3m63r
d3c3mb3r

testcase 2:
in:
2
a
bbbb
aaaa
b
aaab

out:
aaaa
b
aaab

testcase 3:
in:
1
abababab
babababa
abbababa

out:
babababa

testcase 4:
in:
1
a
b

out:
b

testcase 5:
in:
2
abc
aac
cba
caa

out:

testcase 6:
in:
1
caa
aac

out:

testcase 7:
in:
1
caaa
aaac

out:

testcase 8:
in:
1
aaac
caaa

out:

testcase 9:
in:
2
aaac
aac
1aaa
1aa

out:
1aaa

testcase 10:
in:
1
aac
1aa

out:

"""

def get_unacceptable(words: list[str]) -> list[set[str]]:
    unacceptable = [set(words)]

    for _ in range(3):
        unaccepatble_words = set()
        for word in unacceptable[-1]:
            for i in range(len(word) - 1):
                unaccepatble_words.add(word[:i] + word[i + 1] + word[i] + word[i + 2:])
        unacceptable.append(unacceptable[-1].union(unaccepatble_words))

    return unacceptable

def is_acceptable(unacceptable_words: list[set], password: str):
    digits = sum(map(lambda x: x.isdigit(), password))

    if digits > 3:
        return True
    
    for word in unacceptable_words[3 - digits]:
        if len(password) != len(word):
            continue
        if sum([symbol1 == symbol2 or symbol2.isdigit() for symbol1, symbol2 in zip(word, password)]) == len(password):
            return False

    return True

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()

    n = int(lines[0])
    index = 1

    words = list()

    for _ in range(n):
        words.append(lines[index])

        index += 1

    unacceptable_words = get_unacceptable(words)

    while index < len(lines):
        password = lines[index]

        if is_acceptable(unacceptable_words, password):
            output.append(password)

        index += 1

    open(1, "w").write("\n".join(output))