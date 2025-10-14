# 10/14/2025 class session

class Car:
    wheel = 4 # class variable / property / attribute (all correct terms)
    # shared by all instances of the class
    def __init__(self, color, model, speed=0):
        self.color = color
        self.model = model
        self.speed = speed
    def __str__(self):
        return f"The color of this car is {self.color} and the model is {self.model}"
    def moving(self, val):
        self.speed = val

c = Car("red", "2020")
d = Car("blue", "2021")

# print(f"{c.color}, {c.model}")
# print(f"{d.color}, {d.model}")
# print(c)
# print(d)

# c.moving(25)
# print(f"The speed of the car is {c.speed} mph")

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

# We will talk about overriding methods soon

class Cat(Animal):
    def speak(self):
        return "Meow Meow!"
    pass

dog1 = Dog("Buddy", 3, "brown")
dog2 = Dog("Lucy", 5, "black")
print(f"Look, it's dog #1! {dog1}")
print(f"Look, it's dog #2! {dog2}")
print(dog1.speak()) 
cat1 = Cat("Kitty", 2, "white")
print(f"Look, it's cat #1! {cat1}")
print(cat1.speak())