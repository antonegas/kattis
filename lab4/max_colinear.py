"""
author: Anton Nilsson
testcase 1:
in:
3
0 0
10 0
0 10
1
20 20
6
50 50
60 55
70 60
80 65
50 40
50 30
0

out:
2
1
4

"""

from __future__ import annotations
from math import acos, cos, sin
from typing import Union
from collections import defaultdict

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: Point) -> Point:
        if type(other) is not Point:
            raise TypeError(f"unsupported operand type(s) for +: 'Point' and '{type(other).__name__}'")

        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: Point) -> Point:
        if type(other) is not Point:
            raise TypeError(f"unsupported operand type(s) for -: 'Point' and '{type(other).__name__}'")
        
        return Point(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar: Union[Point, float, int]) -> Point:
        if type(scalar) is Point:
            return Point(self.x * scalar.x, self.y * scalar.y)
        if type(scalar) is float or type(scalar) is int:
            return Point(self.x * scalar, self.y * scalar)
        
        raise TypeError(f"unsupported operand type(s) for *: 'Point' and '{type(scalar).__name__}'")
    
    def __truediv__(self, scalar: Union[Point, float, int]) -> Point:
        if type(scalar) is Point:
            return Point(self.x / scalar.x, self.y / scalar.y)
        if type(scalar) is float or type(scalar) is int:
            return Point(self.x / scalar, self.y / scalar)
        
        raise TypeError(f"unsupported operand type(s) for *: 'Point' and '{type(scalar).__name__}'")
    
    def __floordiv__(self, scalar: Union[Point, float, int]) -> Point:
        if type(scalar) is Point:
            return Point(self.x // scalar.x, self.y // scalar.y)
        if type(scalar) is float or type(scalar) is int:
            return Point(self.x // scalar, self.y // scalar)
        
        raise TypeError(f"unsupported operand type(s) for *: 'Point' and '{type(scalar).__name__}'")
    
    def __eq__(self, other: Point) -> bool:
        return self.x == other.x and self.y == other.y
    
    def __abs__(self) -> float:
        return (self.x**2 + self.y**2)**0.5
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def __repr__(self):
        return str(self)
    
    def dot(self, other: Point) -> float:
        return self.x * other.x + self.y * other.y
    
    def cross(self, other: Point) -> float:
        return self.x * other.y - self.y * other.x
    
    def distance(self, other: Point) -> float:
        return abs(self - other)
    
    def angle(self, other: Point) -> float:
        ratio = self.dot(other) / (abs(self) * abs(other))

        if ratio > 1:
            ratio = 1
        elif ratio < -1:
            ratio = -1

        angle = acos(ratio)

        if self.cross(other) > 0:
            return -angle
        else:
            return angle
        
    def rotate(self, angle: float) -> Point:
        return Point(self.x * cos(angle) - self.y * sin(angle), self.x * sin(angle) + self.y * cos(angle))
    
    def normalize(self) -> Point:
        if self == Point(0, 0):
            return Point(0, 0)

        return self / abs(self)
    
    def __hash__(self) -> int:
        normalized = self.normalize()

        return hash((normalized.x, normalized.y))

def max_colinear(points: list[Point]) -> int:
    """
    XXX description XXX

    algorithm: XXX
    time complexity: O(XXX)
    space complexity: O(XXX)
    where:
    - n is the XXX
    why:
    - XXX
    reference: XXX

    parameters:
    - XXX
    returns:
    - XXX
    """

    if len(points) == 1:
        return 1
    
    maximum = 1

    for p in points:
        count = defaultdict(lambda: 1)
        for q in points:
            if p == q:
                continue

            key = float("inf")

            if p.x < q.x:
                key = (q.y - p.y) / (q.x - p.x)
            elif p.x > q.x:
                key = (p.y - q.y) / (p.x - q.x)

            count[key] += 1

        maximum = max(maximum, *count.values())

    return maximum

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()[:-1]

    index = 0

    while index < len(lines):
        n = int(lines[index])
        index += 1

        points = list()

        for _ in range(n):
            x, y = map(int, lines[index].split(" "))
            points.append(Point(x, y))

            index += 1

        output.append(str(max_colinear(points)))

    open(1, "w").write("\n".join(output))
