"""
author: Anton Nilsson
testcase 1:
in:
10
1 2 3 4 5 6 7 8 9 10
10
1 1 1 1 1 1 1 1 1 1
10
5 19 5 81 50 28 29 1 83 23
10
-99 1 2 3 4 5 6 7 8 9
10
99 1 2 3 4 5 6 7 8 9
5
5 4 3 2 1
7
5 4 3 2 1 2 3

out:
10
0 1 2 3 4 5 6 7 8 9
1
9
5
0 1 5 6 8
10
0 1 2 3 4 5 6 7 8 9
9
1 2 3 4 5 6 7 8 9
1
4
3
4 5 6

"""

def lis(sequence: list[int]) -> list[int]:
    """
    Given a sequence of numbers finds the longest subsequence of increasing numbers.

    algorithm: Keeps track of possible ways of creating increasing subsequences using the numbers
    up to an index in the given sequence. This means there will be increasing subsequences of 
    length 0, 1, ..., L, where L is the length of the longest increasing subsequence using the
    numbers up to the index. The kept subsequences are such that the last element in a sequence
    is the smallest it can be when creating a subsequence of that length. This means that 
    binary search can be used to efficiently find which subsequence to append a new number to
    when the index.
    time complexity: O(n*logn)
    where:
    - n is the the number of numbers in the given sequence.
    why:
    - O(n) from looping over all the elements once.
    - O(logn) from doing binary search to find which subsequence to append the current element to.
    reference: https://en.wikipedia.org/wiki/Longest_increasing_subsequence#Efficient_algorithms

    parameters:
    - sequence: a list of integers.
    returns:
    - A list containing the indices of the integers in the longest increasing subsequence.
    """
    
    # Python indexing fix for when checking the sequence of length zero.
    fixed_sequence = sequence + [float("inf")]
    last_elements = [-1]

    previous = list()
    longest_length = 0

    for i, value in enumerate(fixed_sequence[:-1]):
        # Binary search to find the longest sequence to which the current value can be appended to.
        # The value can be appended to any sequence 
        low = 0
        high = longest_length + 1
        while low < high:
            middle = (high + low) // 2
            if fixed_sequence[last_elements[middle]] >= value:
                high = middle
            else:
                low = middle + 1

        previous.append(last_elements[low - 1])

        # Check if a new longest sequence has been found. If a longest sequence has been found set it 
        # as the longest sequence. If not the binary search will have guaranteed that it is safe to 
        # replace the best sequence of length low with the sequence of length low - 1 with value 
        # appended to it. 
        if low > longest_length:
            last_elements.append(i)
            longest_length = low
        else:
            last_elements[low] = i

    # To find the indices of the elements in the longest list backtracking is started from the last
    # element in the longest sequence. Then the saved previous elements is followed until a longest
    # increasing subsequence has been reconstructed.
    longest_sequence = list()
    current_element = last_elements[longest_length]

    for _ in range(longest_length + 1):
        longest_sequence.append(current_element)
        current_element = previous[current_element]

    return list(reversed(longest_sequence))

def solve(sequence: list[int]) -> list[int]:
    return lis(sequence)

if __name__ == "__main__":
    output = ""
    data = open(0, "r").read()
    t = list(data.split("\n")[1:-1:2])
    sequences = [list(map(int, x.split(" "))) for x in data.split("\n")[1:-1:2]]

    for sequence in sequences:
        result = solve(sequence)
        output += f"{len(result)}\n"
        output += " ".join(map(str, result)) + "\n"

    open(1, "w").write(output)