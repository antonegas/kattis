"""
author: Anton Nilsson
testcase 1:
in:
2 0
10 0
10 10

out:
14.14

testcase 2:
in:
2 1
10 0
10 10
9 1

out:
18.11

"""

from __future__ import annotations
from math import acos, cos, sin
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
        
    def rotate(self, angle: float) -> Point:
        return Point(self.x * cos(angle) - self.y * sin(angle), self.x * sin(angle) + self.y * cos(angle))

def barking(toys: list[Point], trees: list[Point]) -> float:
    """
    reference: https://gamedev.stackexchange.com/a/1342
    """
    longest_length = 0
    
    rope = [Point(0, 0)]
    rope_length = [0.0]

    current = toys[0]

    for toy in toys[1:]:
        while current != toy:
            collision_point = toy
            collision_angle = float("inf")
            collision_progress = 1

            for tree in trees:
                op = tree - rope[-1]
                oa = current - rope[-1]
                ob = toy - rope[-1]

                if oa.cross(op) == 0 or op.cross(ob) == 0 or oa.cross(ob) == 0:
                    continue

                sign1 = oa.cross(op) / abs(oa.cross(op))
                sign2 = op.cross(ob) / abs(op.cross(ob))
                sign3 = oa.cross(ob) / abs(oa.cross(ob))

                if sign1 != sign2 or sign2 != sign3:
                    continue

                ab = toy - current
                
                path_progress = (rope[-1] - current).cross(op) / ab.cross(op)
                relative_distance = (rope[-1] - current).cross(ab) / ab.cross(op)

                if abs(relative_distance) < 1:
                    continue

                if abs(oa.angle(op)) < collision_angle:
                    collision_point = tree
                    collision_angle = abs(oa.angle(op))
                    collision_progress = path_progress

            should_combine = False

            if len(rope) >= 2:
                oa = current - rope[-1]
                ob = collision_point - rope[-1]
                qo = rope[-1] - rope[-2]

                sign1 = 1
                sign2 = -sign1

                if qo.cross(oa) != 0 and qo.cross(ob) != 0:
                    sign1 = qo.cross(oa) / abs(qo.cross(oa))
                    sign2 = qo.cross(ob) / abs(qo.cross(ob))

                should_combine = sign1 != sign2

            if should_combine:
                rope.pop()
                rope_length.pop()
                ab = toy - current
                collision_progress = (rope[-1] - current).cross(qo) / ab.cross(qo)
            elif collision_point != toy:
                rope.append(collision_point)
                rope_length.append(rope_length[-1] + abs(rope[-1] - rope[-2]))

            current = current + (toy - current) * collision_progress
        
        longest_length = max(longest_length, rope_length[-1] + abs(toy - rope[-1]))

    return longest_length

def strict_formatting(length: float):
    return "{0:.2f}".format(length)

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()

    n, m = map(int, lines[0].split(" "))
    
    index = 1

    toys = list()

    for _ in range(n):
        x, y = map(int, lines[index].split(" "))
        toys.append(Point(x, y))

        index += 1

    trees = list()

    for _ in range(m):
        x, y = map(int, lines[index].split(" "))
        trees.append(Point(x, y))

        index += 1

    length = barking(toys, trees)
    output.append(strict_formatting(length))

    open(1, "w").write("\n".join(output))