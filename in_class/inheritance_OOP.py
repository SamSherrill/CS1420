# 10/21/25 class

class Animal:
    name = ""
    age = 0
    color = ""
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    def __str__(self):
        return f"Its name is {self.name}, its age is {self.age}, and its color is {self.color}"

class Dog(Animal):
    def speak(self):
        return "Woof Woof!"
    pass

class Cat(Animal):
    def speak(self):
        return "Meow Meow!"
    pass

d = Dog("Rex", 4, "golden")
print(d.speak())
c = Cat("Mittens", 3, "black")
print(c.speak())

# We will talk about overriding methods soon

