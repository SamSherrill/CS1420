# 10//23/25 class, more added on 10/28/25 to discuss polymorphism

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
    def __add__(self, other):
        if isinstance(other, Circle):
            new_radius = self.radius + other.radius
            return Circle(new_radius)
    def __str__(self):
        return f"Circle (radius={self.radius})"

# t = Triangle(3,5)
# print(t)
# print(f"Triangle area: {t.area()}")  # Output: 7.5

# s = Square(4)
# print(s)
# print(f"Square area: {s.area()}")  # Output: 16

# c = Circle(2)
# print(c)
# print(f"Circle area: {c.area()}")  # Output: 12.566370614359172

# print(isinstance(t, Shape))  # True
# print(isinstance(t, Triangle))  # True
# print(isinstance(t, Circle))  # False
# print(issubclass(Triangle, Shape))  # True

""" We're starting to discuss polymorphism and abstract base classes."""

class Dog:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"Dog (name={self.name})"

def main():
    # t = Triangle(3,5)
    # s = Square(4)
    c1 = Circle(2)
    c2 = Circle(3)
    c3 = c1 + c2
    print(type(c3))
    print(c3)
    # d = Dog("Rex")
    # items = []
    # items.append(t)
    # items.append(s)
    # items.append(c)
    # items.append(d)
    # for i in items:
    #     if isinstance(i, Shape):
    #         print(f"{i} has area {i.area()}")

if __name__ == "__main__":
    main()