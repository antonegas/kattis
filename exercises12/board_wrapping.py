"""
author: Anton Nilsson
testcase 1:
in:
1
4
4 7.5 6 3 0
8 11.5 6 3 0
9.5 6 6 3 90
4.5 3 4.4721 2.2361 26.565

out:
64.3 %

"""

from __future__ import annotations
from math import acos, cos, sin, pi
from typing import Union
from functools import cmp_to_key

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
        
def orientation(a: Point, b: Point, c: Point):
    v = a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y)
    if v < 0:
        return -1
    if v > 0:
        return 1
    return 0

def is_clockwise(a: Point, b: Point, c: Point, include_colinear: bool):
    o = orientation(a, b, c)
    return o < 0 or (include_colinear and o == 0)

def is_colinear(a: Point, b: Point, c: Point):
    return orientation(a, b, c) == 0

def compare_angle(a: Point, b: Point, c: Point) -> int:
    o = orientation(a, b, c)
    if o == 0:
        if a.distance(b) < a.distance(c):
            return -1
        else:
            return 1
    
    if o < 0:
        return -1
    return 1

def graham_scan(points: list[Point], include_colinear: bool) -> list[Point]:
    p0 = min(points, key=lambda p:(p.y, p.x))
    points = sorted(points, key=cmp_to_key(lambda x, y: compare_angle(p0, x, y)))

    if include_colinear:
        i = len(points) - 1
        while i >= 0 and is_colinear(p0, points[i], points[-1]):
            i -= 1
        points[i + 1:] = reversed(points[i + 1:])

    stack = list()

    for point in points:
        while len(stack) > 1 and not is_clockwise(stack[-2], stack[-1], point, include_colinear):
            stack.pop()

        stack.append(point)

    return stack

def shoelace(vertices: list[Point]) -> float:
    area = 0

    for vertex1, vertex2 in zip(vertices, vertices[1:] + [vertices[0]]):
        area += vertex1.x * vertex2.y - vertex1.y * vertex2.x

    return area / 2

def board_wrapping(boards: list[tuple[float, float, float, float, float]]):
    points = list()

    boards_area = 0

    for x, y, width, height, angle in boards:
        boards_area += width * height

        p0 = Point(x, y)

        # Goind clockwise starting in bottom left.
        p1 = Point(x - width / 2, y - height / 2)
        p2 = Point(x - width / 2, y + height / 2)
        p3 = Point(x + width / 2, y + height / 2)
        p4 = Point(x + width / 2, y - height / 2)

        # Do the rotation.
        p1 = (p1 - p0).rotate(-angle) + p0
        p2 = (p2 - p0).rotate(-angle) + p0
        p3 = (p3 - p0).rotate(-angle) + p0
        p4 = (p4 - p0).rotate(-angle) + p0

        points.extend([p1, p2, p3, p4])
    
    convex_hull = graham_scan(points, False)
    total_space = abs(shoelace(convex_hull))

    return boards_area / total_space

def strict_formatting(percentage: float):
    return "{0:.1f}".format(percentage)

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()[1:]

    index = 0

    while index < len(lines):
        n = int(lines[index])
        index += 1

        boards = list()

        for _ in range(n):
            x, y, w, h, v = map(float, lines[index].split(" "))
            boards.append((x, y, w, h, v * pi / 180))

            index += 1

        percentage = board_wrapping(boards)

        output.append(f"{strict_formatting(percentage * 100)} %")

    open(1, "w").write("\n".join(output))