"""
author: Anton Nilsson
testcase 1:
in:
6 2
0 0 0
0 3 3
-2 5 5
0 7 7
2 5 9
0 3 11

out:
18.60752550117103

"""

from __future__ import annotations
from math import acos, cos, sin, sqrt
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

def gps_samples(positions: list[Point], times: list[int], sample_rate: int) -> list[Point]:
    samples = [positions[0]]

    i = 1
    t = sample_rate
    
    while t < times[-1]:
        while t > times[i]:
            i += 1

        p = positions[i]
        q = positions[i - 1]
        dt = times[i] - times[i - 1]
        r = q + (p - q) * ((t - times[i - 1]) / dt)

        samples.append(r)

        t += sample_rate

    samples.append(positions[-1])

    return samples

def total_distance(positions: list[Point]) -> float:
    distance = 0

    for p, q in zip(positions, positions[1:]):
        distance += p.distance(q)

    return distance

if __name__ == "__main__":
    n, t = map(int, input().split())

    positions = list()
    times = list()

    for _ in range(n):
        x, y, time = map(int, input().split())
        positions.append(Point(x, y))
        times.append(time)

    gps_positions = gps_samples(positions, times, t)
    actual = total_distance(positions)
    gps = total_distance(gps_positions)

    diff = abs(actual - gps)

    print((diff / actual) * 100)