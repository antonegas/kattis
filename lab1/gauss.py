"""
author: Anton Nilsson
testcase 1:
in:
2
1 1
0 1
23 42
1
5
1
3
1 -2 0
2 -4 0
1 -2 1
3 6 4
3
1 1 0
3 3 0
0 1 2
1 4 8
0

out (non partial):
-19 42
0.2
multiple
inconsistent

out (partial):
-19 42
0.20
? ? 1.00
inconsistent

"""

def gauss_jordan(matrix: list[list[float]], rhs: list[float]) -> list[float]:
    """
    Given a linear equation uses Gauss-Jordan elimination to solve to system.

    algorithm: XXX
    time complexity: O(n^3)
    where:
    - n is the number of equations (the width or height of the matrix).
    why:
    - O(n) from chosing a pivot.
    - O(n^2) from going over each element in the matrix after chosing a pivot.
    reference: https://cp-algorithms.com/linear_algebra/linear-system-gauss.html#implementation

    parameters:
    - matrix: a n*n matrix of linear equations, one for each row in the matrix.
    - rhs: a list of the right hand sides of the equations.
    returns:
    - If there is one solution: a list with the solution to the equation system.
    - If there is multiple solutions: a list with the solution to the equation system where inf indicates value which may take multiple values.
    - If there is no solution: an empty list.
    """

    EPSILON = 1e-9

    # The algorithm as described should have the right hand side vector appended to the matrix.
    a = [matrix[i] + [rhs[i]] for i in range(len(rhs))]
    n = len(rhs)
    
    where = [-1] * n
    row = 0

    for column in range(n):
        pivot = row

        # Select the row with the largest absolute value as the pivot.
        for i in range(row, n):
            if abs(a[i][column]) > abs(a[pivot][column]):
                pivot = i

        # If the absolute value at the pivot is close to zero no valid pivot exists.
        if abs(a[pivot][column]) < EPSILON:
            continue

        for i in range(column, n + 1):
            a[pivot][i], a[row][i] = a[row][i], a[pivot][i]

        where[column] = row

        for i in range(n):
            if i == row:
                continue

            c = a[i][column] / a[row][column]

            for j in range(column, n + 1):
                a[i][j] -= a[row][j] * c

        row += 1

    result = [0.0] * n

    for i in range(n):
        if where[i] != -1:
            result[i] = a[where[i]][n] / a[where[i]][i]

    # Check if the equation system is inconsistent by seeing if the calculated value 
    # is different from the right hand side.
    for i in range(n):
        s = sum([result[j] * a[i][j] for j in range(n)])

        if abs(s - a[i][n]) > EPSILON:
            return []
    
    # Check if the equation system contains variables which may take multiple values.
    # A variable can take multiple values if no pivot was found or if it depends on
    # a variable which may take multiple values.
    for i in range(n):
        if where[i] != -1:
            continue
        result[i] = float("inf")
        for j in range(n):
            if abs(a[j][i]) < EPSILON:
                continue
            result[where.index(j)] = float("inf")

    return result

if __name__ == "__main__":
    PARTIAL = True

    output = list()
    data = open(0, "r").read()
    lines = [[*map(float, x.split(" "))] for x in data.split("\n")[:-1]]

    n = 0
    matrix = list()

    for l in lines:
        if n == 0:
            matrix = list()
            n = int(l[0]) + 1
            continue
        if n == 1:
            t = gauss_jordan(matrix, l)
            if len(t) == 0:
                output.append("inconsistent")
            elif float("inf") in t and not PARTIAL:
                output.append("multiple")
            else:
                output.append(" ".join(list(map(str, map(lambda x: x, t)))).replace("inf", "?"))
        else:
            matrix.append(l)
        n -= 1

    open(1, "w").write("\n".join(output))