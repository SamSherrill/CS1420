# 10/14/2025 class session

class Car:
    wheel = 4 # class variable / property / attribute (all correct terms)
    # shared by all instances of the class
    def __init__(self, color, model):
        self.color = color
        self.model = model

c = Car("red", "2020")
d = Car("blue", "2021")

print(c.color)
print(d.color)

