"""
author: Anton Nilsson
testcase 1:
in:
3
mamad
asflkj
aabb

out:
3
Impossible
2

testcase 2:
in:
1
vvuetetun

out:
11

"""

def evil_straw(word: str):
    start = 0
    end = len(word) - 1
    checked = [False] * len(word)

    result = 0

    while start < end:
        from_start = start
        from_end = end
        start_ignore = 0
        end_ignore = 0

        while from_start < end:
            if word[from_start] == word[end] and not checked[from_start]:
                break
            if checked[from_start]:
                start_ignore += 1
            from_start += 1

        while from_end > start:
            if word[from_end] == word[start] and not checked[from_end]:
                break
            if checked[from_end]:
                end_ignore += 1
            from_end -= 1

        if from_start >= end and from_end <= start:
            return -1
        
        edit_distance_start = from_start - start - start_ignore
        edit_distance_end = end - from_end - end_ignore
        
        if edit_distance_start < edit_distance_end:
            checked[from_start] = True
            checked[end] = True
            result += edit_distance_start
        else:
            checked[from_end] = True
            checked[start] = True
            result += edit_distance_end

        while start < len(word) and checked[start]:
            start += 1
        while 0 < end and checked[end]:
            end -= 1

    return result

if __name__ == "__main__":
    output = list()
    words = open(0, "r").read().splitlines()[1:]

    for word in words:
        result = evil_straw(word)

        if result < 0:
            output.append("Impossible")
        else:
            output.append(str(result))

    open(1, "w").write("\n".join(output))