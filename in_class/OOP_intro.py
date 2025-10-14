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
print(c)
print(d)

c.moving(25)
print(f"The speed of the car is {c.speed} mph")