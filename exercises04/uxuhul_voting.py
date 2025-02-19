"""
author: Anton Nilsson
testcase 1:
in:
2
4
8 7 6 5 4 3 2 1
8 6 3 1 2 4 5 7
8 3 6 5 1 2 7 4
1 2 3 4 5 6 7 8
1
1 2 3 4 5 6 7 8

out:
NYY
NNY

"""

def vote(preferences: list[list[int]]) -> int:
    options = [1, 2, 4]
    last_preference = preferences[-1]
    initial_votes = list()

    for previous in range(8):
        initial_votes.append(min([previous ^ option for option in options], key=lambda i: last_preference[i]))

    result = [initial_votes]

    for preference in reversed(preferences[:-1]):
        future_votes = result[-1]
        optimal_votes = list()

        for previous in range(8):
            optimal_votes.append(min([future_votes[previous ^ option] for option in options], key=lambda i: preference[i]))

        result.append(optimal_votes)

    return result[-1][0]

if __name__ == "__main__":
    output = list()
    data = open(0, "r").read()

    ORDER = ["NNN", "NNY", "NYN", "NYY", "YNN", "YNY", "YYN", "YYY"]

    preferences = list()
    for line in data.split("\n")[2:-1]:
        preference = list(map(int, line.split(" ")))
        if len(preference) == 1:
            output.append(ORDER[vote(preferences)])
            preferences = list()
        else:
            preferences.append(preference)
    output.append(ORDER[vote(preferences)])

    open(1, "w").write("\n".join(output))