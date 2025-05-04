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

from __future__ import annotations

class Rational:
    def __init__(self, numerator: int, denominator: int):
        """
        Creates a rational number on reduced form.

        time complextiy: O(log(min(a,b)))
        why:
        - O(log(min(a,b))) from getting the greatest common divisor.
        """
        if denominator == 0:
            raise ZeroDivisionError
        
        self.numerator = numerator
        self.denominator = denominator

        self._simplify()
    
    def _simplify(self):
        common_divisor = self._gcd(self.numerator, self.denominator)

        self.numerator = self.numerator // common_divisor
        self.denominator = self.denominator // common_divisor

        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def _gcd(self, a: int, b: int) -> int:
        """
        Calculates the greatest common divisor for two numbers.

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

        return abs(old_r) 
    
    def __add__(self, other: Rational) -> Rational:
        """
        Calculates the sum of two rational numbers.

        time complextiy: O(log(min(a,b)))
        why:
        - O(log(min(a,b))) from simplifying the fraction.
        """
        if type(other) is not Rational:
            raise TypeError(f"unsupported operand type(s) for +: 'Rational' and '{type(other).__name__}'")

        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator

        return Rational(numerator, denominator)
    
    def __sub__(self, other: Rational) -> Rational:
        """
        Calculates the difference of two rational numbers.

        time complextiy: O(log(min(a,b)))
        why:
        - O(log(min(a,b))) from simplifying the fraction.
        """
        if type(other) is not Rational:
            raise TypeError(f"unsupported operand type(s) for -: 'Rational' and '{type(other).__name__}'")

        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator

        return Rational(numerator, denominator)

    def __mul__(self, other: Rational) -> Rational:
        """
        Calculates the product of two rational numbers.

        time complextiy: O(log(min(a,b)))
        why:
        - O(log(min(a,b))) from simplifying the fraction.
        """
        if type(other) is not Rational:
            raise TypeError(f"unsupported operand type(s) for *: 'Rational' and '{type(other).__name__}'")

        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator

        return Rational(numerator, denominator)
    
    def __truediv__(self, other: Rational) -> Rational:
        """
        Calculates the quotient of two rational numbers.

        time complextiy: O(log(min(a,b)))
        why:
        - O(log(min(a,b))) from simplifying the fraction.
        """
        if type(other) is not Rational:
            raise TypeError(f"unsupported operand type(s) for /: 'Rational' and '{type(other).__name__}'")

        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator

        return Rational(numerator, denominator)
    
    def __lt__(self, other: Rational) -> bool:
        """
        Checks if a rational number is strictly less than another.

        time complexity: O(1)
        """
        if type(other) is not Rational:
            raise TypeError(f"'<' not supported between instances of 'Rational' and '{type(other).__name__}'")

        return self.numerator * other.denominator < other.numerator * self.denominator

    def __gt__(self, other: Rational) -> bool:
        """
        Checks if a rational number is strictly greater than another.

        time complextiy: O(1)
        """
        if type(other) is not Rational:
            raise TypeError(f"'>' not supported between instances of 'Rational' and '{type(other).__name__}'")

        return self.numerator * other.denominator > other.numerator * self.denominator
    
    def __le__(self, other: Rational) -> bool:
        """
        Checks if a rational number is less than or equal to another.

        time complextiy: O(1)
        """
        if type(other) is not Rational:
            raise TypeError(f"'<=' not supported between instances of 'Rational' and '{type(other).__name__}'")

        return self.numerator * other.denominator <= other.numerator * self.denominator
    
    def __ge__(self, other: Rational) -> bool:
        """
        Checks if a rational number is greater than or equal to another.

        time complextiy: O(1)
        """
        if type(other) is not Rational:
            raise TypeError(f"'>=' not supported between instances of 'Rational' and '{type(other).__name__}'")

        return self.numerator * other.denominator >= other.numerator * self.denominator
    
    def __eq__(self, other: Rational) -> bool:
        """
        Checks if a rational number is less than or equal to another.

        time complexity: O(1)
        """
        if type(other) is not Rational:
            return False

        return self.numerator * other.denominator == other.numerator * self.denominator
    
    def __ne__(self, other: Rational) -> bool:
        """
        Checks if a rational number is less than or equal to another.

        time complexity: O(1)
        """
        if type(other) is not Rational:
            return False

        return self.numerator * other.denominator != other.numerator * self.denominator
    
    def __str__(self):
        """
        Converts a rational number to a string representation.
        """
        return f"{self.numerator} / {self.denominator}"
    
    @staticmethod
    def from_string(string: str) -> Rational:
        """
        Converts a string representation of a rational number to a rational number.

        time complexity: O(1)
        """
        numerator, denominator = map(int, string.split(" / "))

        return Rational(numerator, denominator)

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()[1:]

    for x1, y1, operator, x2, y2 in map(lambda x: x.split(" "), lines):
        a = Rational(int(x1), int(y1))
        b = Rational(int(x2), int(y2))
        c = Rational(1, 1)

        match operator:
            case "+":
                c = a + b
            case "-":
                c = a - b
            case "*":
                c = a * b
            case "/":
                c = a / b

        output.append(str(c))

    open(1, "w").write("\n".join(output))