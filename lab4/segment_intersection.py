"""
author: Anton Nilsson
testcase 1:
in:
5
-10 0 10 0 0 -10 0 10
-10 0 10 0 -5 0 5 0
1 1 1 1 1 1 2 1
1 1 1 1 2 1 2 1
1871 5789 216 -517 189 -518 3851 1895

out:
0.00 0.00
-5.00 0.00 5.00 0.00
1.00 1.00
none
221.33 -496.70

testcase 2:
in:
4
0 0 10 0 5 0 15 0
10 0 0 0 5 0 15 0
0 0 10 0 15 0 5 0
10 0 0 0 15 0 5 0

out:
5.00 0.00 10.00 0.00
5.00 0.00 10.00 0.00
5.00 0.00 10.00 0.00
5.00 0.00 10.00 0.00

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
    """
    Determines if a point is on a line segment.

    algorithm: A point is on a line segment if it is on the same line as the line 
    segment and its between the points making the line segment.
    time complexity: O(1)
    why:
    - O(1) from all constant time operations.
    reference: https://stackoverflow.com/a/328122

    parameters:
    - segment: the line segment to check if the point is on.
    - c: the point to check if it is on the line segment.
    returns:
    - If the point is on the line segment or not.
    """
    
    a, b = segment

    ac = c - a
    ab = b - a

    # The point c is not on the segment if it is not on the same line as a and b.
    if ab.cross(ac) != 0:
        return False
    
    # The point c is between a and b if the dot product between ac and ab is between
    # 0 and the squared length of ab.
    return ac.dot(ab) >= 0 and ac.dot(ab) <= a.distance(b)**2

def segment_intersection(segment1: tuple[Point, Point], segment2: tuple[Point, Point]) -> list[Point]:
    """
    Finds the intersection point or line segment between two line segment if there is one.

    algorithm: The intersection point or line segment can be determined using linear algebra. 
    A line segment is a point if the difference between its points is the zero vector. 
    If both segments are points they intersect if they are equal. If one segment is a point 
    they intersect if the point is on the other segment. The two segments are parallel or 
    colinear if the cross prodcut of their direction vectors are zero. If they overlap can 
    then be determined by expressing the points in one segment by the starting point and 
    direction vector of the other. If the line segments are not parallel or colinear they 
    either don't intersect or intersect in a point. If there is an intersection point it can 
    be determined by solving p1 + t * (p2 - p1) = q1 + u * (q2 - q1). If both t and u are 
    between zero and one there is an intersection point.
    - The lines for the line segments are parallel or colinear if their cross product is zero.
    time complexity: O(1)
    why:
    - O(1) from all constant time operations.
    reference: https://stackoverflow.com/a/565282

    parameters:
    - segment1: the first line segment.
    - segment2: the second line segment.
    returns:
    - If there is not intersection: an empty list.
    - If there is a point intersection: a list with the intersection point.
    - If there is a line segment intersection: a list with the points of the intersecting line segment.
    """
    
    p1, p2 = segment1
    q1, q2 = segment2

    r = p2 - p1
    s = q2 - q1

    o = Point(0, 0)

    # Handle the case where atleast line segment is a point.
    if r == o or s == o:
        # If both segments are points they intersect if they are equal.
        if r == o and s == o:
            return [p1] if p1 == q1 else []
        
        # If one segment is a point they intersect if the point is on the other segment.
        point = p1
        segment = segment2

        if s == o:
            point = q1
            segment = segment1

        return [point] if point_on_segment(segment, point) else []

    # Lines are parallel or colinear.
    if r.cross(s) == 0:        
        # Lines are parallel.
        if (p1 - q1).cross(r) != 0:
            return []
        
        t0 = (q1 - p1).dot(r) / r.dot(r)
        t1 = t0 + s.dot(r) / r.dot(r)

        if s.dot(r) < 0:
            t0, t1 = t1, t0

        # Lines are colinear but segments are non-overlapping.
        if t1 < 0 or 1 < t0:
            return []
        
        # Calculate the overlapping segment.
        start = p1 + r * max(0, t0)
        end = p1 + r * min(1, t1)

        # Check if the overlapping segment is a point.
        if start == end:
            return [start]
        else:
            return [start, end]
    
    # Lines either interect in a point or not at all.
    t = (q1 - p1).cross(s) / r.cross(s)
    u = (p1 - q1).cross(r) / s.cross(r)

    # If t and u are between 0 and 1 there is an intersection point.
    if 0 <= t <= 1 and 0 <= u <= 1:
        return [p1 + r * t]
    
    return []

def strict_formatting(point: Point):
    return "{0:.2f}".format(point.x + 0.0) + " " + "{0:.2f}".format(point.y + 0.0)

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

        intersection = segment_intersection((p1, p2), (q1, q2))

        if len(intersection) == 0:
            output.append("none")
        elif len(intersection) == 1:
            p = intersection[0]
            output.append(strict_formatting(p))
        else:
            p, q = intersection
            if q.x < p.x or (q.x == p.x and q.y < p.y):
                p, q = q, p
            output.append(strict_formatting(p) + " " + strict_formatting(q))

        index += 1

    open(1, "w").write("\n".join(output))