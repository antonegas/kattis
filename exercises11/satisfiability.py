"""
author: Anton Nilsson
testcase 1:
in:
2
3 3
X1 v X2
~X1
~X2 v X3
3 5
X1 v X2 v X3
X1 v ~X2
X2 v ~X3
X3 v ~X1
~X1 v ~X2 v ~X3

out:
satisfiable
unsatisfiable

"""

def sat(clauses: list[list[int]], remaining: list[int], current: int, variables: int) -> bool:
    if len(remaining) == 0:
        return True
    if current == variables:
        return False
    
    true_remaining = list()
    false_remaining = list()

    for clause_index in remaining:
        if clauses[clause_index][current] == 0:
            true_remaining.append(clause_index)
            false_remaining.append(clause_index)
        elif clauses[clause_index][current] == 1:
            false_remaining.append(clause_index)
        elif clauses[clause_index][current] == -1:
            true_remaining.append(clause_index)

    if sat(clauses, true_remaining, current + 1, variables):
        return True
    elif sat(clauses, false_remaining, current + 1, variables):
        return True
    else:
        return False

if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split(" "))

        clauses = list()

        for _ in range(m):
            clause = [0] * n

            for literal in input().split(" v "):
                if literal[0] == "~":
                    if clause[int(literal[2:]) - 1] != 0:
                        clause[int(literal[2:]) - 1] = 2
                    else:
                        clause[int(literal[2:]) - 1] = -1
                else:
                    if clause[int(literal[1:]) - 1] != 0:
                        clause[int(literal[1:]) - 1] = 2
                    else:
                        clause[int(literal[1:]) - 1] = 1
            
            clauses.append(clause)

        if sat(clauses, [*range(len(clauses))], 0, n):
            print("satisfiable")
        else:
            print("unsatisfiable")