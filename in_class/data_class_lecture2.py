# Class 11/6/25
# Prof did a UML diagram on the white board. It included:
# A parent class for Person, which had 2 child classes: Student and Faculty.
# Student and Faculty will be related to a Course class.
# Students can take 0-5 courses; Faculty can teach 1-* courses.
# Courses can have 10-30 students and 1-* faculty member.

from dataclasses import dataclass, field

@dataclass(order=True)
class Person:
    sort_index: int = field(init=False, repr=False)
    # field(init=False) means this field is not wanted when creating each object
    name: str
    age: int

    # This method runs automatically after the __init__ method created by dataclass
    def __post_init__(self):
        # Set the sort_index to the age of the person
        self.sort_index = self.age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"
    # repr not (usually) needed once dataclass is used; it auto provides one
    # def __repr__(self):
    #     return f"Person(name={self.name}, age={self.age})"

a = Person("Alice", 20)
b = Person("Bob", 21)
c = Person("Charlie", 23)
persons = [a, b, c]
persons.sort()  # works because dataclass auto provides comparison methods
print(persons)