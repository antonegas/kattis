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
from math import acos, cos, sin, sqrt
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
        return sqrt(self.x**2 + self.y**2)
    
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

def max_colinear(points: list[Point]) -> int:
    """
    Given a list of points find the maximum number of colinear points.

    algorithm: Calculate the slope between each pair of points (p, q) going in the 
    right direction. If two points q1 and q2 has the same slope with p they are 
    both in the same line with p. Hash this slope to keep count of how many points 
    are in the same line.
    time complexity: O(n^3) or Theta(n^2)
    where:
    - n is the number of points
    why:
    - O(n^2) from looping over every pair of points.
    - O(n) from worst case hashmap insertion and lookup.
    - Theta(1) from best case hashmap insertion and lookup.
    reference: https://math.stackexchange.com/a/20260

    parameters:
    - points: a list of points to find the maximum number of colinear points for.
    returns:
    - The maximum number of colinear points.
    """

    # If there are two or less points the maximum number of colinear points is equal 
    # to the number of points.
    if len(points) <= 2:
        return len(points)
    
    maximum = 1

    # Loop over every pair of points.
    for i in range(len(points)):
        p = points[i]

        # Initialize count to one for every slope since p is in every line.
        count = defaultdict(lambda: 1)
        
        for j in range(i + 1, len(points)):
            q = points[j]

            key = float("inf")

            # Check which order of the points results in a slope going in the 
            # right direction.
            if p.x < q.x:
                key = (q.y - p.y) / (q.x - p.x)
            elif p.x > q.x:
                key = (p.y - q.y) / (p.x - q.x)

            # Increase the count for the slope. If the count is larger than the current 
            # maximum update it.
            count[key] += 1
            maximum = max(maximum, count[key])

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
