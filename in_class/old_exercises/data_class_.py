# Class 11/4/25 about typing, etc

from dataclasses import dataclass

@dataclass(order=True)
class Person:
    # with order=True, objects are sorted by the first field, then second field, etc.
    # Additionallly, order=True automatically adds comparison methods
    name: str
    age: int
    # The init method is taken care of by the dataclass decorator using the lines above
    # def __init__(self, name: str, age: int) -> None:
    #     self.name = name
    #     self.age = age
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"
    
a = Person("Alice", 30)
b = Person("Bob", 25)
print(a)
print(b)
persons = []
persons.append(a)
persons.append(b)
print(persons)

# Next time we'll discuss how sorting works with dataclass