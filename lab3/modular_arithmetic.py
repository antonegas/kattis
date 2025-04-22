"""
author: Anton Nilsson
testcase 1:
in:
1000 3
1 / 999
1 / 998
578 * 178
13 4
7 / 9
9 * 3
0 - 9
10 + 10
0 0

out:
999
-1
884
8
1
4
7

"""

def modular_inverse(a: int, b: int) -> int:
    """
    Calculates the modular inverse of a for the divisor n. Gives -1 if there is no modular inverse.

    time complexity: O(log(min(a,b)))
    Reference: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
    """
    old_r = a
    r = b
    old_s = 1
    s = 0
    old_t = 0
    t = 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    if old_r != 1:
        return -1

    return old_s % b

def modular_add(a: int, b: int, n: int) -> int:
    """
    Calculates the sum of two numbers modolo n.

    time complexity: O(1)
    """
    return (a + b) % n

def modular_subtract(a: int, b: int, n: int) -> int:
    """
    Calculates the difference between two numbers modolo n.

    time complexity: O(1)
    """
    return (a - b) % n

def modular_multiply(a: int, b: int, n: int) -> int:
    """
    Calculates the product of two numbers modolo n.

    time complexity: O(1)
    """
    return (a * b) % n

def modular_divide(a: int, b: int, n: int) -> int:
    """
    Calculates the quotient of two numbers modolo n.

    time complexity: O(log(min(a,b)))
    why:
    - O(log(min(a,b))) from running the extended Euclidean algorithm to find the modular inverse.
    """
    b_inverse = modular_inverse(b, n)

    # Negative one indicates that there is no modular inverse for b in modolo n.
    if b_inverse == -1:
        return -1
    
    return (a * b_inverse) % n

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()[:-1]

    index = 0

    while index < len(lines):
        n, t = map(int, lines[index].split(" "))

        index += 1

        for _ in range(t):
            x, operator, y = lines[index].split(" ")

            index += 1

            a = int(x)
            b = int(y)
            c = -1

            match operator:
                case "+":
                    c = modular_add(a, b, n)
                case "-":
                    c = modular_subtract(a, b, n)
                case "*":
                    c = modular_multiply(a, b, n)
                case "/":
                    c = modular_divide(a, b, n)

            output.append(str(c))

    open(1, "w").write("\n".join(output))