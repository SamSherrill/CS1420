# Class 10/30/25

from typing import Protocol, runtime_checkable

# Make a protocol class Swimable and two classes that implement it
@runtime_checkable
class Swimable(Protocol):
    def swim(self):
        ...

@runtime_checkable
class Flyable(Protocol):
    def fly(self):
        ...

class Fish:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def swim(self):
        return f"{self.name} the {self.species} is swimming"
    
class Penguin:
    def __init__(self, name):
        self.name = name

    def swim(self):
        return f"{self.name} the penguin is swimming"


class Bird:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def fly(self):
        return f"{self.name} can fly"
    
class Helicoptor:
    def __init__(self, make, power):
        self.make = make
        self.power = power

    def fly(self):
        return f"{self.make} helicopter can fly ...mph"

def make_swim(item: Swimable) -> None:
    item.swim()

def make_fly(item: Flyable) -> None:
    item.fly()

f = Fish("Nemo", "Clownfish")
p = Penguin("Pingu")

make_swim(f)
make_swim(p)

b = Bird("Polly", "Green")
h = Helicoptor("Bell", 5000)

make_fly(b)
make_fly(h)