"""
author: Anton Nilsson
testcase 1:
in:
2
1.12 0
0 0.51
3
158 12
123 15
1859 -1489
3
21.12 -884.2
18.18 43.34
21.12 -884.2
0

out:
0.0 0.51 1.12 0.00
123 15 158 12.00
21.12 -884.20 21.12 -884.20

testcase 2:
in:
5
1 1
1 1
1 1
1 1
1 2
0

out:
1.00 1.00 1.00 1.00

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
    """
    Handles the initialization needed for the closest pair of points algorithm.

    parameters:
    - points: the points to find the closest pair of points for.
    returns:
    - The pair of points with the shortest distance between them.
    """

    return closest_pair(sorted(points, key=lambda p:(p.x, p.y)), 0, len(points))

def closest_pair(points: list[Point], left: int, right: int) -> tuple[Point, Point]:
    """
    Given a list of points finds the pair of points with the shortest distance between them.

    algorithm: XXX
    time complexity: O(n*logn)
    where:
    - n is the number of points.
    why:
    - XXX
    reference: https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/

    parameters:
    - XXX
    returns:
    - XXX
    """

    if right - left < 4:
        shortest = (Point(float("inf"), float("inf")), Point(0, 0))
        
        for i in range(left, right):
            for j in range(i + 1, right):
                shortest = min(shortest, (points[i], points[j]), key=lambda x:x[0].distance(x[1]))

        return shortest
    
    middle = (left + right) // 2

    shortest_left = closest_pair(points, left, middle)
    shortest_right = closest_pair(points, middle, right)

    shortest = min(shortest_left, shortest_right, key=lambda x:x[0].distance(x[1]))
    distance = shortest[0].distance(shortest[1])

    strip = list()

    for i in range(left, right):
        if abs(points[i].x - points[middle].x) < distance:
            strip.append(points[i])

    strip.sort(key=lambda p:p.y)

    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if strip[j].y - strip[i].y >= distance:
                break

            shortest = min(shortest, (strip[i], strip[j]), key=lambda x:x[0].distance(x[1]))

    return shortest
 
def strict_formatting(point: Point):
    return "{0:.2f}".format(point.x + 0.0) + " " + "{0:.2f}".format(point.y + 0.0)   

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()[:-1]

    index = 0

    while index < len(lines):
        n = int(lines[index])

        index += 1

        points = list()

        for _ in range(n):
            x, y = map(float, lines[index].split(" "))

            points.append(Point(x, y))

            index += 1

        point1, point2 = closest_pair_init(points)

        output.append(f"{strict_formatting(point1)} {strict_formatting(point2)}")

    open(1, "w").write("\n".join(output))
