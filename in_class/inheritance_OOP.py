# 10/21/25 class

# class Animal:
#     name = ""
#     age = 0
#     color = ""
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#     def __str__(self):
#         return f"Its name is {self.name}, its age is {self.age}, and its color is {self.color}"

# class Dog(Animal):
#     def __init__(self, name, age, color, strength):
#         super().__init__(name, age, color)
#         self.strength = strength
#     def speak(self):
#         return "Woof Woof!"
#     pass

# class Cat(Animal):
#     def speak(self):
#         return "Meow Meow!"
#     pass

# d = Dog("Rex", 4, "golden", "very strong")
# print(d.speak())
# c = Cat("Mittens", 3, "black")
# print(c.speak())

# We will talk about overriding methods soon

class A:
    def __init__(self,name):
        self.name = name
    def parent(self):
        print("I am from parent 1")

class B:
    def __init__(self,age):
        self.age = age
    def parent(self):
        print("I am from parent 2")

class C(A,B):
    def __init__(self,name,age,gender):
        A.__init__(self,name)
        B.__init__(self,age)
        self.gender = gender
    def child(self):
        print("I am from child class")

c = C("Alice", 10, 'F')
# print(c.name)
# print(c.age)
# print(c.gender)
# c.parent() # When inherited methods match, the first parent in the inheritance list is called
print(C.__mro__)  # Method Resolution Order
print(isinstance(c, A))  # True
print(isinstance(c, B))  # True
print(issubclass(C, A))  # True
print(issubclass(C, B))  # True