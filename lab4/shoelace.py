"""
author: Anton Nilsson
testcase 1:
in:
3
0 0
10 0
0 10
5
41 -6
-24 -74
-51 -6
73 17
-30 -34
0

out:
CCW 50.0
CW 3817.5

"""

from __future__ import annotations
from math import acos

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
    
    def __mul__(self, scalar) -> Point:
        if type(scalar) is Point:
            return Point(self.x * scalar.x, self.y * scalar.y)
        if type(scalar) is float and type(scalar) is int:
            return Point(self.x * scalar, self.y + scalar)
        
        raise TypeError(f"unsupported operand type(s) for *: 'Point' and '{type(scalar).__name__}'")
    
    def __truediv__(self, scalar: float) -> Point:
        if type(scalar) is Point:
            return Point(self.x / scalar.x, self.y / scalar.y)
        if type(scalar) is float and type(scalar) is int:
            return Point(self.x / scalar, self.y / scalar)
        
        raise TypeError(f"unsupported operand type(s) for *: 'Point' and '{type(scalar).__name__}'")
    
    def __floordiv__(self, scalar: float) -> Point:
        if type(scalar) is Point:
            return Point(self.x // scalar.x, self.y // scalar.y)
        if type(scalar) is float and type(scalar) is int:
            return Point(self.x // scalar, self.y // scalar)
        
        raise TypeError(f"unsupported operand type(s) for *: 'Point' and '{type(scalar).__name__}'")
    
    def __eq__(self, other: Point) -> bool:
        return self.x == other.x and self.y == other.y
    
    def __abs__(self) -> float:
        return (self.x**2 + self.y**2)**0.5
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
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

def shoelace(vertices: list[Point]) -> float:
    """
    Given a list of vertices in a polygon calculates the area of the polygon.

    algorithm: The formula used is Gauss' shoelace formula.
    time complexity: O(n)
    where:
    - n is the number of vertices in the polygon.
    why:
    - O(n) from looping over the vertices in the polygon.
    reference: https://gamedev.stackexchange.com/a/151036

    parameters:
    - vertices: a list of ordered vertices in the polygon.
    returns:
    - If the vertices are given in clockwise order: the negative area of the polygon.
    - If the vertices are given in counter clockwise order: the area of the polygon.
    """
    area = 0

    for vertex1, vertex2 in zip(vertices, vertices[1:] + [vertices[0]]):
        area += vertex1.x * vertex2.y - vertex1.y * vertex2.x

    return area / 2

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()[:-1]

    index = 0

    while index < len(lines):
        n = int(lines[index])
        index += 1

        vertices = list()

        for _ in range(n):
            x, y = map(int, lines[index].split(" "))
            index += 1

            vertices.append(Point(x, y))

        area = shoelace(vertices)
        direction = "CCW" if area > 0 else "CW"

        output.append(f"{direction} {abs(area)}")

    open(1, "w").write("\n".join(output))