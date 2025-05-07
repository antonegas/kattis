"""
author: Anton Nilsson
testcase 1:
in:
8
0 0 0 4 1 2
1 1 1 4 3 2
2 2 2 4 4 3
3 3 3 4 5 3
4 4 4 5 5 6
5 5 5 6 6 5
6 6 6 7 6 8
7 7 7 7 7 7

out:
Case #1: isosceles obtuse triangle
Case #2: scalene acute triangle
Case #3: isosceles acute triangle
Case #4: scalene right triangle
Case #5: scalene obtuse triangle
Case #6: isosceles right triangle
Case #7: not a triangle
Case #8: not a triangle

"""

from __future__ import annotations
from math import acos, pi
from typing import Union

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

def triangle_type(a: Point, b: Point, c: Point) -> tuple[int, int]:
    if abs(a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y)) == 0:
        return 0, 0
    
    ab = b - a
    ac = c - a
    bc = b - c

    ab2 = ab * ab
    ac2 = ac * ac
    bc2 = bc * bc

    x = ab2.x + ab2.y
    y = ac2.x + ac2.y
    z = bc2.x + bc2.y

    xyz = sorted([x, y, z])
    
    edge_type = 2

    if xyz[0] == xyz[1] or xyz[1] == xyz[2]:
        edge_type = 1

    angle_type = 1

    if xyz[0] + xyz[1] < xyz[2]:
        angle_type = 2

    if xyz[0] + xyz[1] == xyz[2]:
        angle_type = 3

    return edge_type, angle_type

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()

    index = 1

    while index < len(lines):
        x1, y1, x2, y2, x3, y3 = map(int, lines[index].split(" "))
        
        a = Point(x1, y1)
        b = Point(x2, y2)
        c = Point(x3, y3)

        edge_type, angle_type = triangle_type(a, b, c)

        edge_identifiers = ["not", "isosceles", "scalene"]
        angle_identifiers = ["a", "acute", "obtuse", "right"]

        output.append(f"Case #{index}: {edge_identifiers[edge_type]} {angle_identifiers[angle_type]} triangle")

        index += 1

    open(1, "w").write("\n".join(output))