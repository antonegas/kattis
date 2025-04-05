"""
author: Anton Nilsson
testcase 1:
in:
4
1 3 + 1 2
1 3 - 1 2
123 287 / 81 -82
12 -3 * -1 -1

out:
5 / 6
-1 / 6
-82 / 189
-4 / 1

"""

from math import gcd

def rational_create(numerator: int, denominator: int) -> tuple[int, int]:
    """
    Creates a rational number on reduced form.
    """
    if denominator == 0:
        raise ZeroDivisionError
    
    common_divisor = gcd(numerator, denominator)

    if numerator < 0 and denominator < 0:
        return (-numerator // common_divisor, -denominator // common_divisor)
    if denominator < 0:
        return (-numerator // common_divisor, -denominator // common_divisor)

    return (numerator // common_divisor, denominator // common_divisor)

def rational_add(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    """
    Calculates the sum of two rational numbers.
    """
    a_numerator, a_demoninator = a
    b_numerator, b_denominator = b

    numerator = a_numerator * b_denominator + b_numerator * a_demoninator
    denominator = a_demoninator * b_denominator

    return rational_create(numerator, denominator)

def rational_subtract(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    """
    Calculates the difference of two rational numbers.
    """
    a_numerator, a_demoninator = a
    b_numerator, b_denominator = b

    numerator = a_numerator * b_denominator - b_numerator * a_demoninator
    denominator = a_demoninator * b_denominator
    
    return rational_create(numerator, denominator)

def rational_multiply(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    """
    Calculates the product of two rational numbers.
    """
    a_numerator, a_demoninator = a
    b_numerator, b_denominator = b

    numerator = a_numerator * b_numerator
    denominator = a_demoninator * b_denominator
    
    return rational_create(numerator, denominator)

def rational_divide(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    """
    Calculates the quotient of two rational numbers.
    """
    a_numerator, a_demoninator = a
    b_numerator, b_denominator = b

    numerator = a_numerator * b_denominator
    denominator = a_demoninator * b_numerator
    
    return rational_create(numerator, denominator)

def rational_less_than(a: tuple[int, int], b: tuple[int, int]) -> bool:
    """
    Checks if a rational number is strictly less than another.
    """
    a_numerator, a_demoninator = a
    b_numerator, b_denominator = b

    return a_numerator * b_denominator < b_numerator * a_demoninator

def rational_greater_than(a: tuple[int, int], b: tuple[int, int]) -> bool:
    """
    Checks if a rational number is strictly greater than another.
    """
    a_numerator, a_demoninator = a
    b_numerator, b_denominator = b

    return a_numerator * b_denominator > b_numerator * a_demoninator

def rational_less_equal(a: tuple[int, int], b: tuple[int, int]) -> bool:
    """
    Checks if a rational number is less than or equal to another.
    """
    a_numerator, a_demoninator = a
    b_numerator, b_denominator = b

    return a_numerator * b_denominator <= b_numerator * a_demoninator

def rational_greater_equal(a: tuple[int, int], b: tuple[int, int]) -> bool:
    """
    Checks if a rational number is greater than or equal to another.
    """
    a_numerator, a_demoninator = a
    b_numerator, b_denominator = b

    return a_numerator * b_denominator >= b_numerator * a_demoninator

def rational_equal(a: tuple[int, int], b: tuple[int, int]) -> bool:
    """
    Checks if a rational number is less than or equal to another.
    """
    a_numerator, a_demoninator = a
    b_numerator, b_denominator = b

    return a_numerator * b_denominator == b_numerator * a_demoninator

def rational_not_equal(a: tuple[int, int], b: tuple[int, int]) -> bool:
    """
    Checks if a rational number is less than or equal to another.
    """
    a_numerator, a_demoninator = a
    b_numerator, b_denominator = b

    return a_numerator * b_denominator != b_numerator * a_demoninator

def rational_string(rational: tuple[int, int]) -> str:
    """
    Converts a rational number to a string representation.
    """
    numerator, denominator = rational

    return f"{numerator} / {denominator}"

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()[1:]

    for x1, y1, operator, x2, y2 in map(lambda x: x.split(" "), lines):
        a = rational_create(int(x1), int(y1))
        b = rational_create(int(x2), int(y2))
        c = (-1, -1)

        match operator:
            case "+":
                c = rational_add(a, b)
            case "-":
                c = rational_subtract(a, b)
            case "*":
                c = rational_multiply(a, b)
            case "/":
                c = rational_divide(a, b)

        output.append(rational_string(c))

    open(1, "w").write("\n".join(output))