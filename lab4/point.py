"""
author: Anton Nilsson
"""

from __future__ import annotations
from math import acos

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
    
    def __abs__(self) -> float:
        return (self.x**2 + self.y**2)**0.5
    
    def dot(self, other: Point) -> float:
        return self.x * other.x + self.y * other.y
    
    def cross(self, other: Point) -> float:
        return self.x * other.y - self.y * other.x
    
    def distance(self, other: Point) -> float:
        return abs(self - other)
    
    def angle(self, other: Point) -> float:
        return acos(self.dot(other) / (abs(self) * abs(other)))