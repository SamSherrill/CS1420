# 10//23/25 class

import math

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
    def __str__(self):
        return f"Triangle (base={self.base}, height={self.height})"

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
    def __str__(self):
        return f"Square (side={self.side})"
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius * self.radius
    def __str__(self):
        return f"Circle (radius={self.radius})"

t = Triangle(3,5)
print(t)
print(f"Triangle area: {t.area()}")  # Output: 7.5

s = Square(4)
print(s)
print(f"Square area: {s.area()}")  # Output: 16

c = Circle(2)
print(c)
print(f"Circle area: {c.area()}")  # Output: 12.566370614359172

print(isinstance(t, Shape))  # True
print(isinstance(t, Triangle))  # True
print(isinstance(t, Circle))  # False
print(issubclass(Triangle, Shape))  # True