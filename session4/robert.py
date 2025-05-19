"""
author: Anton Nilsson
testcase 1:
in:
2
2 2
-1 -2

out:
5.0

testcase 2:
in:
5
-4 1
-100 0
0 4
2 -3
2 300

out:
316.86590223

"""

from __future__ import annotations
from math import acos
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
        
def closest_pair_init(points: list[Point]) -> tuple[Point, Point]:
    return closest_pair(sorted(points, key=lambda p:(p.x, p.y)), 0, len(points))

def closest_pair(points: list[Point], left: int, right: int) -> tuple[Point, Point]:
    if right - left < 4:
        longest = (Point(float("inf"), float("inf")), Point(0, 0))
        
        for i in range(left, right):
            for j in range(i + 1, right):
                longest = min(longest, (points[i], points[j]), key=lambda x:x[0].distance(x[1]))

        return longest
    
    middle = (left + right) // 2

    longest_left = closest_pair(points, left, middle)
    longest_right = closest_pair(points, middle, right)

    longest = max(longest_left, longest_right, key=lambda x:x[0].distance(x[1]))
    distance = longest[0].distance(longest[1])

    strip = list()

    for i in range(left, right):
        if abs(points[i].x - points[middle].x) > distance:
            strip.append(points[i])

    strip.sort(key=lambda p:p.y)

    for i in range(len(strip)):
        for j in range(-1, i, -1):
            if strip[j].y - strip[i].y < distance:
                break

            longest = max(longest, (strip[i], strip[j]), key=lambda x:x[0].distance(x[1]))

    return longest

if __name__ == "__main__":
    n = int(input())
    points = [Point(*map(int, input().split())) for _ in range(n)]

    p, q = closest_pair_init(points)

    print(p.distance(q))