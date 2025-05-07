"""
author: Anton Nilsson
testcase 1:
in:
2
4
-5 -5
5 -5
5 5
-5 5
4
-10 -10
-10 10
10 10
10 -10
3
0 0
1 0
1 1
5
3 -3
3 3
-4 2
-1 -1
-2 -2

out:
2.5
0.70710678

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

def white_water(inner: list[Point], outer: list[Point]) -> float:
    best = float("inf")

    for p1, p2 in zip(outer, outer[1:] + [outer[0]]):
        for q1, q2 in zip(inner, inner[1:] + [inner[0]]):
            distance = segment_distance((p1, p2), (q1, q2))

            best = min(best, distance)
    
    return best / 2

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()[1:]

    index = 0

    while index < len(lines):
        n = int(lines[index])
        index += 1

        inner = list()

        for _ in range(n):
            x, y = map(int, lines[index].split(" "))
            inner.append(Point(x, y))

            index += 1

        m = int(lines[index])
        index += 1

        outer = list()

        for _ in range(m):
            x, y = map(int, lines[index].split(" "))
            outer.append(Point(x, y))

            index += 1

        print(white_water(inner, outer))

    open(1, "w").write("\n".join(output))