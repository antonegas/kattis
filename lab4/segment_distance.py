"""
author: Anton Nilsson
testcase 1:
in:
5
-10 0 10 0 0 -10 0 10
-10 0 10 0 -5 0 5 0
1 1 1 1 1 1 2 1
1 1 1 1 2 1 2 1
1871 5789 216 -517 189 -1518 3851 1895

out:
0.00
0.00
0.00
1.00
713.86

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
        
def point_on_segment(segment: tuple[Point, Point], c: Point) -> bool:
    a, b = segment

    ac = c - a
    ab = b - a

    if ab.cross(ac) != 0:
        return False
    
    return ac.dot(ab) >= 0 and ac.dot(ab) <= a.distance(b)**2

def segment_intersection(segment1: tuple[Point, Point], segment2: tuple[Point, Point]) -> list[Point]:
    p1, p2 = segment1
    q1, q2 = segment2

    r = p2 - p1
    s = q2 - q1

    o = Point(0, 0)

    if r == o or s == o:
        if r == o and s == o:
            return [p1] if p1 == q1 else []
        
        point = p1
        segment = segment2

        if s == o:
            point = q1
            segment = segment1

        return [point] if point_on_segment(segment, point) else []

    if r.cross(s) == 0:        
        if (p1 - q1).cross(r) != 0:
            return []
        
        t0 = (q1 - p1).dot(r) / r.dot(r)
        t1 = t0 + s.dot(r) / r.dot(r)

        if s.dot(r) < 0:
            t0, t1 = t1, t0

        if t1 < 0 or 1 < t0:
            return []

        start = p1 + r * max(0, t0)
        end = p1 + r * min(1, t1)

        if start == end:
            return [start]
        else:
            return [start, end]
    
    t = (q1 - p1).cross(s) / r.cross(s)
    u = (p1 - q1).cross(r) / s.cross(r)

    if 0 <= t <= 1 and 0 <= u <= 1:
        return [p1 + r * t]
    
    return []

def clamp(value: float, min_value: float, max_value: float) -> float:
    return min(max(value, min_value), max_value)

def segment_distance(segment1: tuple[Point, Point], segment2: tuple[Point, Point]) -> float:
    """
    Given two line segments returns the shortest distance between them.

    algorithm: XXX
    time complexity: O(1)
    why:
    - O(1) from all constant time operations.
    reference: https://stackoverflow.com/a/2824596

    parameters:
    - segment1: the first line segment.
    - segment2: the second line segment.
    returns:
    - The shortest distance between the two line segments.
    """
    
    if segment_intersection(segment1, segment2):
        return 0.0

    p1, p2 = segment1
    q1, q2 = segment2

    segment_point_pairs = [
        (segment1, q1),
        (segment1, q2),
        (segment2, p1),
        (segment2, p2)
    ]
    
    shortest_distance = float("inf")

    for segment, point in segment_point_pairs:
        p, q = segment

        if p == q:
            shortest_distance = min(point.distance(p), shortest_distance)
            continue

        dx = q.x - p.x
        dy = q.y - p.y

        t = ((point.x - p.x) * dx + (point.y - p.y) * dy) / (dx**2 + dy**2)

        t = clamp(t, 0, 1)
        
        distance = ((point.x - p.x - t * dx)**2 + (point.y - p.y - t * dy)**2)**0.5
        shortest_distance = min(shortest_distance, distance)

    return shortest_distance

def strict_formatting(value: float):
    return "{0:.2f}".format(value + 0.0)

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()[1:]

    index = 0

    while index < len(lines):
        px1, py1, px2, py2, qx1, qy1, qx2, qy2 = map(int, lines[index].split(" "))
        
        p1 = Point(px1, py1)
        p2 = Point(px2, py2)
        q1 = Point(qx1, qy1)
        q2 = Point(qx2, qy2)

        output.append(strict_formatting(segment_distance((p1, p2), (q1, q2))))

        index += 1

    open(1, "w").write("\n".join(output))