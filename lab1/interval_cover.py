"""
author: Anton Nilsson
testcases:
in:
-0.5 1
3
-0.9 -0.1
-0.2 2
-0.7 1
0 1
3
0 0.25
0.25 0.75
0.75 0.999
0 1
3
0 0.25
0.25 0.75
0.75 1
1 1
1
1 1
0 1
3
0 1
1 3
3 4
1 1
2
1 1
1 1
1 1
2
1 1
2 2
1 1
2
2 2
1 1

out:
1
2
impossible
3
0 1 2
1
0
1
0
1
1
1
0
1
1

"""

def cover(interval: tuple[float, float], intervals: list[tuple[float, float]]) -> list[int]:
    """
    Given an interval will find if it possible fully cover it given a set of intervals.
    If it is possible to fully cover the interval it will give a list of 

    algorithm: Chosing an interval which covers the most of the remaining interval, 
    including the left most element, results in the minimum number of intervals being used. 
    A proof is left as an exercise for the reader (TDDD20, lecture 2).
    time complexity: O(n*logn)
    where:
    - n is the number of intervals
    why:
    - O(n*logn) from sorting the intervals (python uses powersort/mergesort)
    - O(n) from looping over the sorted intervals
    - O(1) for popping the last element of a list
    - O(1) for appending an element to a list
    - O(n*logn+n*(1+1)) = O(nlogn)

    parameters:
    - interval: the interval for which to find a minimal amount of intervals which covers it.
    - intervals: the intervals from which the algorithm choses when searching for a solution.
    returns:
    - If a solution exists: a list of indices which creates a minimum covering of the interval.
    - If a solution doesn't exist: an empty list
    """
    # Intervals are sorted in order to only have to loop through the intervals once.
    # The indices of each interval in the original list is appended to be able to return
    # them later.
    indexed_intervals = [iv + (i,) for i, iv in enumerate(intervals)]
    sorted_intervals = sorted(indexed_intervals)

    low, high = interval
    current_index = 0
    result = list()

    # Loop until the interval is covered. The number of intervals which covers the interval 
    # needs to be atleast one.
    while low < high or len(result) == 0:
        # Start the search for, the next interval, from the current low
        new_low = low
        best_index = None

        # Check intervals not already checked until the left most value in the
        # remaining intervals is greater than the current low.
        for left_most, right_most, index in sorted_intervals[current_index:]:
            # Does the current interval still cover low.
            if left_most > low:
                break

            # If the right most is greater than or equal to the currently best known
            # interval update the new low and the best index.

            # Greater than or equal, to is used to make it easier to find a solution in
            # the case that the lowest value and the highest value in the interval is equal.
            if right_most >= new_low:
                new_low = right_most
                best_index = index
            
            current_index += 1

        # If a new best index was not found, the interval can't be covered.
        if best_index is None:
            return list()
        
        # If a new low was found update low and append the used interval index.
        low = new_low
        result.append(best_index)
    
    return result

def solve(interval: tuple[float, float], intervals: list[tuple[float, float]]) -> list[int]:
    return cover(interval, intervals)

if __name__ == "__main__":
    output = ""
    data = open(0, "r").read()
    info = [tuple(map(float, x.split(" "))) for x in data.split("\n")[:-1]]

    i = 0
    while i < len(info):
        intervals = list()
        interval = info[i]
        i += 1

        n = int(info[i][0])
        i += 1

        for _ in range(n):
            intervals.append(info[i])
            i += 1

        result = solve(interval, intervals)

        if len(result) == 0:
            output += "impossible\n"
        else:
            output += f"{len(result)}\n"
            output += " ".join(map(str, result)) + "\n"

    open(1, "w").write(output)