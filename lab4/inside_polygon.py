"""
author: Anton Nilsson
testcase 1:
in:
3
0 0
10 0
0 10
3
4 5
5 5
6 5
5
41 -6
-24 -74
-51 -6
73 17
-30 -34
2
-12 -26
39 -8
0

out:
in
on
out
out
in

"""

from __future__ import annotations
from math import acos, pi

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
    
    def dot(self, other: Point) -> float:
        return self.x * other.x + self.y * other.y
    
    def cross(self, other: Point) -> float:
        return self.x * other.y - self.y * other.x
    
    def distance(self, other: Point) -> float:
        return abs(self - other)
    
    def angle(self, other: Point) -> float:
        angle = acos(self.dot(other) / (abs(self) * abs(other)))

        if self.cross(other) > 0:
            return -angle
        else:
            return angle
    
    def __str__(self):
        return f"({self.x},{self.y})"

def inside_polygon(point: Point, vertices: list[Point]) -> int:
    """
    Given a point and a the vertices of a polygon determines if the point is inside of the polygon

    algorithm: The algorithm used is counting the sum of the angles between the neighboring vertices 
    and the point. If the sum equal to two pi the point is inside of the polygon and if it is zero 
    the point is outside of the polygon.
    time complexity: O(n)
    where:
    - n is the number of vertices in the polygon.
    why:
    - O(n) from looping over the vertices in the polygon.
    reference: https://www.eecs.umich.edu/courses/eecs380/HANDOUTS/PROJ2/InsidePoly.html

    parameters:
    - point: the point which is check if it is inside of the polygon or not.
    - vertices: the ordered vertices of the polygon.
    returns:
    - If the point is inside of the polygon or not.
    """

    EPSILON = 1e-7

    angle_sum = 0

    for vertex1, vertex2 in zip(vertices, vertices[1:] + [vertices[0]]):
        if point == vertex1 or point == vertex2:
            return 0

        angle = (vertex1 - point).angle(vertex2 - point)

        if abs(angle - pi) < EPSILON:
            return 0

        angle_sum += angle
    
    if abs(angle_sum) > pi:
        return 1
    else:
        return -1

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

        m = int(lines[index])
        index += 1

        for _ in range(m):
            x, y = map(int, lines[index].split(" "))
            index += 1

            result = inside_polygon(Point(x, y), vertices)

            if result == 1:
                output.append("in")
            elif result == 0:
                output.append("on")
            else:
                output.append("out")

    open(1, "w").write("\n".join(output))